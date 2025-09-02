# Django Todo List Application

A feature-rich task management application built with Django that helps you organize your tasks with a beautiful, intuitive interface.

![Task Management App](static/img/app-preview.png)

## Features

- ✨ Clean, modern interface with Bootstrap styling
- 📱 Fully responsive design
- 🎯 Three-state task management (Todo, In Progress, Completed)
- 🔄 Drag-and-drop task reordering
- 🎨 Visual status indicators and animations
- ⚡ Real-time status updates
- 📅 Due date tracking
- 🏷️ Priority levels (High, Medium, Low)
- 🔍 Task filtering and search functionality

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation

1. **Clone the repository** (or download the ZIP file):
   ```bash
   git clone https://github.com/yourusername/todo-list.git
   cd todo-list
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/MacOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and navigate to: `http://127.0.0.1:8000`

## Usage

### Creating Tasks

1. Click the "Add New Task" button
2. Fill in the required fields:
   - Title (required)
   - Description (optional)
   - Due Date (optional)
   - Priority (required)
3. Click "Create Task"

### Managing Tasks

- **Change Task Status**:
  - Edit the task and use the status switches (Todo/In Progress/Completed)
  - Or drag and drop tasks between columns

- **Edit Task**:
  - Click the edit (pencil) icon on any task
  - Modify the task details
  - Click "Save Changes"

- **Delete Task**:
  - Click the delete (trash) icon on any task
  - Confirm deletion

### Task Properties

- **Priority Levels**:
  - High (Red)
  - Medium (Yellow)
  - Low (Green)

- **Status Options**:
  - Todo (Default for new tasks)
  - In Progress
  - Completed

### Filtering and Search

- Use the search bar to find specific tasks
- Filter tasks by:
  - Status
  - Priority
  - Due Date

## Project Structure

```
todo-list/
├── manage.py
├── requirements.txt
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       └── task_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── static/
    ├── css/
    └── js/
```

## Customization

### Changing the Theme

1. Update the Bootstrap classes in templates
2. Modify the CSS in static/css/

### Adding New Features

1. Create new models in `tasks/models.py`
2. Create corresponding forms in `tasks/forms.py`
3. Add new views in `tasks/views.py`
4. Update templates in `tasks/templates/tasks/`

## Common Issues and Solutions

### Task Creation Issues
- Ensure all required fields are filled
- Check for proper date format in the due date field

### Status Update Issues
- Verify proper click on status switches
- Check network connectivity for AJAX updates

### Database Issues
- Run `python manage.py migrate` after model changes
- Check database file permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, email your-email@example.com or create an issue in the GitHub repository.

## Acknowledgments

- Django Framework
- Bootstrap
- Font Awesome
- SortableJS for drag-and-drop functionality
