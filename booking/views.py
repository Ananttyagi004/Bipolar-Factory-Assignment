from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Flight, Booking
from .forms import FlightSearchForm, BookingForm,FlightForm

def search_flights(request):
    form = FlightSearchForm(request.GET or None)
    flights = None
    if form.is_valid():
        departure_city = form.cleaned_data.get('departure_city')
        arrival_city = form.cleaned_data.get('arrival_city')
        departure_date = form.cleaned_data.get('departure_date')

        flights = Flight.objects.filter(
            departure_city__icontains=departure_city,
            arrival_city__icontains=arrival_city,
            departure_time__gte=departure_date
        ).order_by('departure_time')

    return render(request, 'booking/search_flights.html', {'form': form, 'flights': flights})

@login_required
def book_ticket(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.flight = flight
            booking.save()
            flight.seat_count -= 1
            flight.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()
    
    return render(request, 'booking/book_ticket.html', {'form': form, 'flight': flight})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'


@login_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FlightForm()
    return render(request, 'booking/add_flight.html', {'form': form})

@login_required
def remove_flight(request, flight_id=None):
    if request.method == 'POST':
        flight = get_object_or_404(Flight, id=flight_id)
        flight.delete()
        return redirect('remove_flight')
    flights = Flight.objects.all()
    return render(request, 'booking/remove_flight.html', {'flights': flights})