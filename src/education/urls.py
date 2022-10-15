from django.urls import path
from education import views

app_name = 'education'
urlpatterns = [
    path('english_institude_register/', views.english_institude_register, name='english_institude_register'),
    path('english_institute_forms_list/', views.english_institute_forms_list, name='english_institute_forms_list'),
    path('delete_english_institute_forms_list/<int:id>', views.delete_english_institute_forms_list, name='delete_english_institute_forms_list'),
    path('send_english_institute_forms_list/<int:id>', views.send_english_institute_forms_list, name='send_english_institute_forms_list'),
]