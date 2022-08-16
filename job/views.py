from django.shortcuts import render
from .models import Job
from django.http import HttpResponse

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    print("Test")
    job_detail = Job.objects.get(id=id)
    print(job_detail)
    context = {'job': job_detail}
    return render(request, 'job/job_detail.html', context)
