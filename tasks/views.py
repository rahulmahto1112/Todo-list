from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Task
from .forms import TaskForm, TaskSearchForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all().order_by('status', '-priority', 'due_date')
        
        # Get filter parameters
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        query = self.request.GET.get('query')

        if status:
            queryset = queryset.filter(status=status)

        if priority:
            queryset = queryset.filter(priority=priority)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm(self.request.GET)
        context['today'] = timezone.now().date()
        return context

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.status = 'todo'  # Set default status for new tasks
        self.object = form.save()
        messages.success(self.request, 'Task created successfully!')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Handle status changes
        if 'status' in request.POST:
            new_status = request.POST.get('status')
            if new_status in ['todo', 'in_progress', 'completed']:
                self.object.status = new_status
                self.object.save()
                messages.success(request, f'Task moved to {self.object.get_status_display()}')
                return redirect('tasks:task_list')
            
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task updated successfully!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_edit'] = True
        return context

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)

from django.http import JsonResponse

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Cycle through statuses: todo -> in_progress -> completed -> todo
    if task.status == 'todo':
        task.status = 'in_progress'
    elif task.status == 'in_progress':
        task.status = 'completed'
    else:
        task.status = 'todo'
    
    task.save()
    
    messages.success(request, f'Task marked as {task.status}!')
    return redirect('tasks:task_list')

def update_task_status(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        new_status = request.POST.get('status')
        
        # Handle the case where in_progress comes from JS as in-progress
        if new_status == 'in-progress':
            new_status = 'in_progress'
            
        if new_status in ['todo', 'in_progress', 'completed']:
            task.status = new_status
            task.save()
            messages.success(request, f'Task "{task.title}" moved to {task.get_status_display()}')
            return JsonResponse({
                'status': 'success',
                'new_status': new_status,
                'message': f'Task moved to {task.get_status_display()}'
            })
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid status value'
        }, status=400)

def task_search(request):
    search_form = TaskSearchForm(request.GET)
    tasks = Task.objects.all()

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        status = search_form.cleaned_data.get('status')
        priority = search_form.cleaned_data.get('priority')

        if query:
            tasks = tasks.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        if status:
            is_completed = status == 'completed'
            tasks = tasks.filter(status=is_completed)

        if priority:
            tasks = tasks.filter(priority=priority)

    context = {
        'tasks': tasks,
        'search_form': search_form,
        'today': timezone.now().date(),
    }
    return render(request, 'tasks/task_list.html', context)
