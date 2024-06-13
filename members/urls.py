from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('magazin',views.magazin ,name='magazin'),
    path('magazin/SportsterS',views.sportsters, name='sportsters'),
    path('magazin/Softail',views.softail, name='softail'),
    path('magazin/Street-Glide',views.street, name='street'),
    path('magazin/Forty-Eight',views.forty, name='forty'),
    path('shop',views.order,name='shop'),
    path('signup',views.signup,name='signup'),
    path('login',views.login, name='login'),
]