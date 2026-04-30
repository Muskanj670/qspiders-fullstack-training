from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.forms import SignUpForm, LoginForm, TODOForm
from myapp.models import TODOModel

def home_view(request):
    return render(request, 'myapp/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            messages.success(request, 'Signed up successfully.')
            return redirect("login")
        messages.error(request, 'Please fix the errors below.')
    else:
        form = SignUpForm()
    return render(request, "myapp/signup.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                messages.success(request, 'Logged in successfully.')
                login(request, user)
                return redirect('task')
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required(login_url='login')
def task_view(request):
    tasks = TODOModel.objects.all().order_by('status', 'due_date', '-created_at')
    form = TODOForm()

    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task')
        messages.error(request, 'Please fix the errors below.')

    return render(request, 'myapp/task.html', {'form': form, 'tasks': tasks})

@login_required(login_url='login')
def update_task_view(request, pk):
    task = get_object_or_404(TODOModel, pk=pk)

    if request.method == 'POST':
        form = TODOForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = TODOForm(instance=task)

    tasks = TODOModel.objects.all().order_by('status', 'due_date', '-created_at')
    return render(request, 'myapp/task.html', {'form': form, 'tasks': tasks, 'editing_task': task})

@login_required(login_url='login')
def complete_task_view(request, pk):
    task = get_object_or_404(TODOModel, pk=pk)
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.save()
    return redirect('task')

@login_required(login_url='login')
def delete_task_view(request, pk):
    task = get_object_or_404(TODOModel, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('task')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')
