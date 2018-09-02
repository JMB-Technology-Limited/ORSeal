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


def organisation_list(request, slug):

    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    organisations = Organisation.objects.filter(project=project)

    return render(request, 'project/organisations.html', {
        'organisations': organisations,
        'project': project,
    })


def organisation_show(request, slug, id):

    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    try:
        organisation = Organisation.objects.get(project=project, standard_id=id)
    except Organisation.DoesNotExist:
        raise Http404("Organisation does not exist")

    return render(request, 'project/organisation/index.html', {
        'organisation': organisation,
        'project': project,
    })
