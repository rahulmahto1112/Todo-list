from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("task/add/", views.TaskCreateView.as_view(), name="task_create"),
    path("task/edit/<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("task/toggle/<int:pk>/", views.toggle_task_status, name="task_toggle"),
    path("task/update-status/<int:pk>/", views.update_task_status, name="task_update_status"),
    path("search/", views.task_search, name="task_search"),
]
