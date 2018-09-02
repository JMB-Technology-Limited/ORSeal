from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse



def index(request):
    return HttpResponse("Hello, Open Referral Seal.")


def project(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    return render(request, 'project/index.html', {
        'project': project,
    })


def organization_list(request, slug):

    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    organizations = DataOrganization.objects.filter(project=project)

    return render(request, 'project/organizations.html', {
        'organizations': organizations,
        'project': project,
    })


def organization_show(request, slug, id):

    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    try:
        organization = DataOrganization.objects.get(project=project, data_id=id)
    except DataOrganization.DoesNotExist:
        raise Http404("Organization does not exist")

    return render(request, 'project/organization/index.html', {
        'organization': organization,
        'project': project,
    })
