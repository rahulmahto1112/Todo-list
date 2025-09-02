from django.db import migrations

def forward_func(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")
    # Update any tasks that might have invalid status
    Task.objects.filter(status="").update(status="todo")
    Task.objects.filter(status__isnull=True).update(status="todo")
    Task.objects.exclude(status__in=["todo", "in_progress", "completed"]).update(status="todo")

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]
