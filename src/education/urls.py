from django.urls import path
from education import views

app_name = 'education'
urlpatterns = [
    path('english_institude_register/', views.english_institude_register, name='english_institude_register'),
    path('forms_list/', views.forms_list, name='froms_list'),
]