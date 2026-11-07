from django.shortcuts import redirect, render


def landing(request):
    return render(request, 'frontend/landing.html')


def login(request):
    if request.method == 'POST':
        return redirect('frontend:dashboard')
    return render(request, 'frontend/login.html')


def signup(request):
    if request.method == 'POST':
        return redirect('frontend:dashboard')
    return render(request, 'frontend/signup.html')



def dashboard(request):
    context = {
        'active_page': 'dashboard',
        'stats': [
            {'label': 'Active Projects', 'value': '8', 'note': '3 due this week'},
            {'label': 'Open Tasks', 'value': '24', 'note': '6 high priority'},
            {'label': 'Team Members', 'value': '12', 'note': '2 new this month'},
            {'label': 'Completion', 'value': '68%', 'note': 'On track'},
        ],
        'recent_projects': [
            {'id': 1, 'name': 'Campus Portal Redesign', 'status': 'In Progress', 'progress': 72},
            {'id': 2, 'name': 'Library Inventory App', 'status': 'Planning', 'progress': 18},
            {'id': 3, 'name': 'Exam Scheduler', 'status': 'In Progress', 'progress': 45},
        ],
        'upcoming_tasks': [
            {'title': 'Prepare UI wireframes', 'due': 'Today', 'priority': 'High'},
            {'title': 'Review sprint notes', 'due': 'Tomorrow', 'priority': 'Medium'},
            {'title': 'Update project timeline', 'due': 'Fri', 'priority': 'Low'},
        ],
    }
    return render(request, 'frontend/dashboard.html', context)


def projects(request):
    context = {
        'active_page': 'projects',
        'projects': [
            {
                'id': 1,
                'name': 'Campus Portal Redesign',
                'owner': 'Aisha Khan',
                'status': 'In Progress',
                'tasks': 16,
                'due': '15 Sep 2026',
            },
            {
                'id': 2,
                'name': 'Library Inventory App',
                'owner': 'Rahul Mehta',
                'status': 'Planning',
                'tasks': 9,
                'due': '30 Sep 2026',
            },
            {
                'id': 3,
                'name': 'Exam Scheduler',
                'owner': 'Priya Sharma',
                'status': 'In Progress',
                'tasks': 12,
                'due': '10 Oct 2026',
            },
            {
                'id': 4,
                'name': 'Event Registration System',
                'owner': 'Vivek Patel',
                'status': 'On Hold',
                'tasks': 7,
                'due': '20 Oct 2026',
            },
        ],
    }
    return render(request, 'frontend/projects.html', context)


def project_detail(request, project_id):
    context = {
        'active_page': 'projects',
        'project': {
            'id': project_id,
            'name': 'Campus Portal Redesign',
            'description': 'A mock project used for layout development. Backend data will replace this later.',
            'owner': 'Aisha Khan',
            'status': 'In Progress',
            'start_date': '01 Aug 2026',
            'due_date': '15 Sep 2026',
            'progress': 72,
            'members': ['Aisha Khan', 'Rahul Mehta', 'Priya Sharma'],
            'tasks': [
                {'title': 'Homepage layout', 'assignee': 'Aisha', 'status': 'Done'},
                {'title': 'Student dashboard', 'assignee': 'Rahul', 'status': 'In Progress'},
                {'title': 'Notice board module', 'assignee': 'Priya', 'status': 'To Do'},
            ],
        },
    }
    return render(request, 'frontend/project_detail.html', context)


def tasks(request):
    context = {
        'active_page': 'tasks',
        'tasks': [
            {'title': 'Prepare UI wireframes', 'project': 'Campus Portal Redesign', 'assignee': 'Aisha', 'due': '02 Sep 2026', 'status': 'In Progress', 'priority': 'High'},
            {'title': 'Create database notes', 'project': 'Library Inventory App', 'assignee': 'Rahul', 'due': '04 Sep 2026', 'status': 'To Do', 'priority': 'Medium'},
            {'title': 'Draft exam conflict rules', 'project': 'Exam Scheduler', 'assignee': 'Priya', 'due': '05 Sep 2026', 'status': 'To Do', 'priority': 'High'},
            {'title': 'Collect sample event data', 'project': 'Event Registration System', 'assignee': 'Vivek', 'due': '08 Sep 2026', 'status': 'On Hold', 'priority': 'Low'},
            {'title': 'Review sprint notes', 'project': 'Campus Portal Redesign', 'assignee': 'Aisha', 'due': '03 Sep 2026', 'status': 'Done', 'priority': 'Medium'},
        ],
    }
    return render(request, 'frontend/tasks.html', context)


def calendar(request):
    context = {
        'active_page': 'calendar',
        'month_label': 'September 2026',
        'calendar_days': range(1, 31),
        'events': [
            {'date': '02 Sep', 'title': 'UI review meeting', 'project': 'Campus Portal Redesign'},
            {'date': '05 Sep', 'title': 'Sprint planning', 'project': 'Exam Scheduler'},
            {'date': '12 Sep', 'title': 'Prototype demo', 'project': 'Library Inventory App'},
            {'date': '15 Sep', 'title': 'Project deadline', 'project': 'Campus Portal Redesign'},
        ],
    }
    return render(request, 'frontend/calendar.html', context)


def ai_assistant(request):
    context = {
        'active_page': 'ai_assistant',
        'sample_messages': [
            {'role': 'user', 'text': 'Summarize the Campus Portal Redesign status.'},
            {'role': 'assistant', 'text': 'This is a placeholder reply. The AI backend will be connected later.'},
        ],
    }
    return render(request, 'frontend/ai_assistant.html', context)


def settings(request):
    context = {
        'active_page': 'settings',
        'profile': {
            'name': 'Demo User',
            'email': 'demo.user@college.edu',
            'role': 'Project Member',
        },
    }
    return render(request, 'frontend/settings.html', context)
