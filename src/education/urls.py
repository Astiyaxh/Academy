from django.urls import path
from education import views

app_name = 'education'
urlpatterns = [
    # English Institute Urls
    path('english_institute_register/', views.english_institute_register, name='english_institute_register'),
    path('english_institute_edit/<int:id>', views.english_institute_edit, name='english_institute_edit'),
    path('english_institute_forms_list/', views.english_institute_forms_list, name='english_institute_forms_list'),
    path('delete_english_institute_forms_list/<int:id>', views.delete_english_institute_forms_list, name='delete_english_institute_forms_list'),
    path('send_english_institute_forms_list/<int:id>', views.send_english_institute_forms_list, name='send_english_institute_forms_list'),

    # None Profit institute urls 
    path('nonprofit_form_register/', views.nonprofit_form_register, name='nonprofit_form_register'),
    path('nonprofit_form_edit/<int:id>', views.nonprofit_form_edit, name='nonprofit_form_edit'),
    path('send_nonprofit_institute_forms_list/<int:id>', views.send_nonprofit_institute_forms_list, name='send_nonprofit_institute_forms_list'),
    path('delete_nonprofit_institute_forms_list/<int:id>', views.delete_nonprofit_institute_forms_list, name='delete_nonprofit_institute_forms_list'),

    # Supervisor form list Urls
    path('supervisor_forms_list/', views.supervisor_forms_list, name='supervisor_forms_list'),

    # Supervisor English Institute Urls
    path('supervisor_rejected_english_institute_forms_list/<int:id>', views.supervisor_rejected_english_institute_forms_list, name='supervisor_rejected_english_institute_forms_list'),
    path('supervisor_accepted_english_institute_forms_list/<int:id>', views.supervisor_accepted_english_institute_forms_list, name='supervisor_accepted_english_institute_forms_list'),

    # Supervisor Profit Institute Urls
    path('supervisor_nonprofit_institute_rejected_forms_list/<int:id>', views.supervisor_nonprofit_institute_rejected_forms_list, name='supervisor_nonprofit_institute_rejected_forms_list'),
    path('supervisor_nonprofit_institute_accepted_forms_list/<int:id>', views.supervisor_nonprofit_institute_accepted_forms_list, name='supervisor_nonprofit_institute_accepted_forms_list'),
]