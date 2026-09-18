from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def tours(request):
    return render(request,'tours/list.html')


@login_required
def requests(request):
    return render(request, 'tours/requests.html')


@login_required
def create(request):
    return render(request, 'tours/create.html')

@login_required
def details(request, id):
    return render(request, 'tours/details.html')