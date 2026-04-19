from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, ContentBox
from .forms import ProjectForm, ContentBoxForm
from django.db.models import Count

@login_required
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'manager/dashboard.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'manager/project_form.html', {'form': form, 'action': 'Criar'})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'manager/project_form.html', {'form': form, 'action': 'Editar'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'manager/confirm_delete.html', {'object': project, 'back_url': 'dashboard'})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    content_boxes = project.content_boxes.all()
    return render(request, 'manager/project_detail.html', {'project': project, 'content_boxes': content_boxes})

@login_required
def contentbox_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk, user=request.user)
    if request.method == 'POST':
        form = ContentBoxForm(request.POST)
        if form.is_valid():
            contentbox = form.save(commit=False)
            contentbox.project = project
            contentbox.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ContentBoxForm()
    return render(request, 'manager/contentbox_form.html', {'form': form, 'project': project, 'action': 'Criar'})

@login_required
def contentbox_edit(request, pk):
    contentbox = get_object_or_404(ContentBox, pk=pk, project__user=request.user)
    if request.method == 'POST':
        form = ContentBoxForm(request.POST, instance=contentbox)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=contentbox.project.pk)
    else:
        form = ContentBoxForm(instance=contentbox)
    return render(request, 'manager/contentbox_form.html', {'form': form, 'project': contentbox.project, 'action': 'Editar'})

@login_required
def contentbox_delete(request, pk):
    contentbox = get_object_or_404(ContentBox, pk=pk, project__user=request.user)
    project_pk = contentbox.project.pk
    if request.method == 'POST':
        contentbox.delete()
        return redirect('project_detail', pk=project_pk)
    return render(request, 'manager/confirm_delete.html', {'object': contentbox, 'back_url': f'/projeto/{project_pk}/'})

@login_required
def contentbox_detail(request, pk):
    contentbox = get_object_or_404(ContentBox, pk=pk, project__user=request.user)
    return render(request, 'manager/contentbox_detail.html', {'contentbox': contentbox})

@login_required
def report_view(request):
    total_projects = Project.objects.filter(user=request.user).count()
    total_contents = ContentBox.objects.filter(project__user=request.user).count()
    return render(request, 'manager/report.html', {
        'total_projects': total_projects,
        'total_contents': total_contents
    })
