from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tours.models import Tour
# Create your views here.


@login_required
def tours(request):
    return render(request,'tours/list.html')


@login_required
def requests(request):
    return render(request, 'tours/requests.html')


@login_required
def create(request):
    if(request.method == 'POST'):
        try:
            tour = Tour.objects.create(
                user = request.user,
                title = request.POST.get('title'),
                tour_category = request.POST.get('tour_category'),
                start_location = request.POST.get('start_location'),
                destination = request.POST.get('destination'),
                start_date = request.POST.get('start_date'),
                end_date = request.POST.get('end_date'),
                price_per_person = request.POST.get('price_per_person'),
                seats = request.POST.get('seat'),
                vehicle = request.POST.get('vehicle'),
                descriptions = request.POST.get('descriptions'),
                pickup_point = request.POST.get('pickup_point'),
                latitude = '' or None,
                longitude = '' or None,
            )
            if tour is not None:
                return redirect('/')
        except Exception as ex:
                print(str(ex))
        
    return render(request, 'tours/create.html')

@login_required
def details(request, id):
    return render(request, 'tours/details.html')