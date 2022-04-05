from django.urls import path, include
from flights import views

app_name = 'flights'

urlpatterns = [
    path('auth/', include([
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
    ])),

    path('flight/', include([
        path('create/', views.flight_create, name='flight-create'),
        path('update/<flight_id>/', views.flight_update, name='flight-update'),
    ])),

    path('passenger/', include([
        path('list/', views.passenger_list, name='passenger-list'),
        path('create/', views.passenger_create, name='passenger-create'),
        path('update/<passenger_id>/', views.passenger_update, name='passenger-update'),
    ])),

    path('', views.index, name='index')
]
