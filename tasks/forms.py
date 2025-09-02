from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task title',
            'required': True,
            'autofocus': True
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter task description'
        })
        self.fields['due_date'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-control',
            'required': True
        })

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or not title.strip():
            raise forms.ValidationError('Title is required')
        return title.strip()
        fields = ['title', 'description', 'due_date', 'priority', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter task description'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title is required')
        return title

class TaskSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search tasks...'})
    )
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('todo', 'To Do'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        initial=''
    )
    priority = forms.ChoiceField(
        required=False,
        choices=[('', 'All')] + list(Task.PRIORITY_CHOICES),
        initial=''
    )
