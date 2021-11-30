from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectsForm
from .utils import searchProjects


def projects(request):
    projects, search_query = searchProjects(request)

    context = {'projects': projects,
               'search_query': search_query}

    # all_projects = Projects.objects.all()
    # context = {'projects': all_projects}
    return render(request, 'projects/projects.html', context)


def project_detail(request, project_id):
    project = Projects.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'projects/single-project.html', context)


def create_project(request):
    form = ProjectsForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project-form.html', context)


def edit_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    form = ProjectsForm(instance=project)
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project-form.html', context)
