from django.shortcuts import render, redirect

from tasks.forms import TaskForm

tasks = ['buy milk', 'buy juice']

def index(request):
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():

            print(request.POST.get('name'))
            print(task_form.cleaned_data['name'])

            # tasks.append(task_form.cleaned_data['name'])
            # task = request.POST.get('name')

            return redirect('tasks:index')

    return render(request, 'tasks/index.html', {
        'task_form': task_form,
        'tasks': tasks,
    })
