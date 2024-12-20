
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forms/', views.form_list, name='form_list'),
    path('form/<int:form_id>/', views.form_detail, name='form_detail'),
    path('form/<int:form_id>/submissions/', views.submission_list, name='submission_list'),
    path('map/', views.map_view, name='map_view'),

]
