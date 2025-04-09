from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('view_supplier/', views.view_supplier, name='view_supplier'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    # path('manage_account/', views.manage_account, name='manage_account'),
    # path('add_water_bottles/', views.add_water_bottles, name='add_water_bottles'),
]