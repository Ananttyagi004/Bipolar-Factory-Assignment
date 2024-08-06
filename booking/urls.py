from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_ticket, name='book_ticket'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
     path('addflight/', views.add_flight, name='add_flight'),
    path('removeflight/<int:flight_id>/', views.remove_flight, name='remove_flight'),
    path('removeflight/', views.remove_flight, name='remove_flight'),
]