from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from flights.forms import LoginForm, FlightForm, PassengerForm
from flights.models import Flight, Passenger


@login_required
def index(request):
    flights = Flight.objects.all()
    if q := request.GET.get('q'):
        try:
            q = int(q)
            flights = flights.filter(
                Q(price__lte=q)
            )
        except:
            flights = flights.filter(
                Q(origin__city__name__icontains=q) |
                Q(destination__city__name__icontains=q)
            )

    return render(request, 'flights/index.html', {
        'flights': flights
    })


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        #
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        #
        # user = authenticate(request, username=username, password=password)
        # if user:
        #     login(user)
        #     return redirect('flights:index')

        if form.is_valid():
            if user := authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            ):
                login(request, user)
                return redirect('flights:index')

    return render(request, 'flights/login.html', {
        'form': form,
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('flights:index')


@login_required
def flight_create(request):
    flight_form = FlightForm()

    if request.method == 'POST':
        flight_form = FlightForm(request.POST)
        if flight_form.is_valid():
            flight_form.save()
            return redirect('flights:index')

    return render(request, 'flights/flight_create.html', {
        'flight_form': flight_form,
    })


@login_required
def passenger_create(request):
    passenger_form = PassengerForm()

    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)
        if passenger_form.is_valid():
            passenger_form.save()
            return redirect('flights:index')

    return render(request, 'flights/passenger_create.html', {
        'passenger_form': passenger_form,
    })


@login_required
def flight_update(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    flight_form = FlightForm(instance=flight)

    if request.method == 'POST':
        flight_form = FlightForm(request.POST, instance=flight)
        if flight_form.is_valid():
            flight_form.save()
            return redirect('flights:index')

    return render(request, 'flights/flight_update.html', {
        'flight_form': flight_form,
        'flight': flight
    })


@login_required
def passenger_list(request):
    passengers = Passenger.objects.all()
    if q := request.GET.get('q'):
        passengers = passengers.filter(
            Q(first__icontains=q) |
            Q(last__icontains=q)
        )

    return render(request, 'flights/passenger_list.html', {
        'passengers': passengers,
    })


@login_required
def passenger_update(request, passenger_id):
    passenger = get_object_or_404(Passenger, id=passenger_id)

    passenger_form = PassengerForm(instance=passenger)

    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST, instance=passenger)
        if passenger_form.is_valid():
            passenger_form.save()
            return redirect('flights:passenger-list')

    return render(request, 'flights/passenger_update.html', {
        'passenger_form': passenger_form,
        'passenger': passenger,
    })
