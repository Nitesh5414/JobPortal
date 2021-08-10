from django.shortcuts import render, redirect
from django.http import HttpResponse
from jobapp.forms import UserRegistrationForm, AddITJobsForm, AddMECHJobsForm, AddCIVILJobsForm, UpdateITJobsForm, UpdateMECHJobsForm, UpdateCIVILJobsForm, AddImageForm
from jobapp.models import ITjobs, MECHjobs, CIVILjobs, ImageTable
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_page(request):
    return render(request, 'jobapp/index.html')


def user_register_view(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'jobapp/register.html', {'form': form})


def home_page_view(request):
    return render(request, 'jobapp/home.html')

@login_required(login_url='/login/')
def add_it_job_view(request):

    if request.method == "POST":
        form = AddITJobsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show_it/')

    else:
        form = AddITJobsForm()

    return render(request, 'jobapp/add_it.html',{'form': form} )

def show_it_jobs_view(request):
    data = ITjobs.objects.all()

    return render(request, "jobapp/show_it.html", {'data': data})

@login_required(login_url='/login/')
def update_it_jobs_view(request, id):
    obj = ITjobs.objects.get(pk=id)
    # form = UpdateITJobsForm(instance=obj)

    if request.method =="POST":
        form = UpdateITJobsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/show_it/')

    else:
        form = UpdateITJobsForm(instance=obj)

    context = {
    'form' : form

    }
    return render(request, 'jobapp/update_it.html', context)

@login_required(login_url='/login/')
def delete_it_jobs_view(request, id):
    obj = ITjobs.objects.get(pk=id)

    obj.delete()
    return redirect('/show_it/')

@login_required(login_url='/login/')
def add_mech_job_view(request):

    if request.method == "POST":
        form = AddMECHJobsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show_mech/')

    else:
        form = AddMECHJobsForm()

    return render(request, 'jobapp/add_mech.html',{'form': form} )

@login_required(login_url='/login/')
def update_mech_jobs_view(request, id):
    obj = MECHjobs.objects.get(pk=id)
    # form = UpdateITJobsForm(instance=obj)

    if request.method =="POST":
        form = UpdateMECHJobsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/show_mech/')

    else:
        form = UpdateMECHJobsForm(instance=obj)

    context = {
    'form' : form

    }
    return render(request, 'jobapp/update_mech.html', context)

@login_required(login_url='/login/')
def delete_mech_jobs_view(request, id):
    obj = MECHjobs.objects.get(pk=id)

    obj.delete()
    return redirect('/show_it/')


def show_mech_jobs_view(request):
    data = MECHjobs.objects.all()

    return render(request, "jobapp/show_mech.html", {'data': data})

@login_required(login_url='/login/')
def add_civil_job_view(request):

    if request.method == "POST":
        form = AddCIVILJobsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show_civil/')

    else:
        form = AddCIVILJobsForm()

    return render(request, 'jobapp/add_civil.html',{'form': form} )

@login_required(login_url='/login/')
def update_civil_jobs_view(request, id):
    obj = CIVILjobs.objects.get(pk=id)
    # form = UpdateITJobsForm(instance=obj)

    if request.method =="POST":
        form = UpdateCIVILJobsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/show_civil/')

    else:
        form = UpdateCIVILJobsForm(instance=obj)

    context = {
    'form' : form

    }
    return render(request, 'jobapp/update_civil.html', context)

@login_required(login_url='/login/')
def delete_civil_jobs_view(request, id):
    obj = CIVILjobs.objects.get(pk=id)

    obj.delete()
    return redirect('/show_civil/')


def show_civil_jobs_view(request):
    data = CIVILjobs.objects.all()

    return render(request, "jobapp/show_civil.html", {'data': data})

def add_image_view(request):
    form = AddImageForm()

    print(request.POST, request.FILES)

    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()


    return render(request, 'jobapp/add_image.html', {'form':form})

def read_image_view(request):
    data = ImageTable.objects.all()
    return render(request, 'jobapp/read_image.html', {'data':data})
