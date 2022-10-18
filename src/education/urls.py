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
    path('none_profit_form_register/', views.none_profit_form_register, name='none_profit_form_register'),
    path('delete_nonprofit_institute_forms_list/<int:id>', views.delete_nonprofit_institute_forms_list, name='delete_nonprofit_institute_forms_list'),
    path('send_nonprofit_institute_forms_list/<int:id>', views.send_nonprofit_institute_forms_list, name='send_nonprofit_institute_forms_list'),
    path('none_profit_form_edit/<int:id>', views.none_profit_form_edit, name='none_profit_form_edit'),


    # Admin English Institute Urls
    path('admin_forms_list/', views.admin_forms_list, name='admin_forms_list'),
    path('admin_rejected_forms_list/<int:id>', views.admin_rejected_forms_list, name='admin_rejected_forms_list'),
    path('admin_accepted_forms_list/<int:id>', views.admin_accepted_forms_list, name='admin_accepted_forms_list'),

    # Admin Profit Institute Urls
    path('admin_nonprofit_institute_rejected_forms_list/<int:id>', views.admin_nonprofit_institute_rejected_forms_list, name='admin_nonprofit_institute_rejected_forms_list'),
    path('admin_nonprofit_institute_accepted_forms_list/<int:id>', views.admin_nonprofit_institute_accepted_forms_list, name='admin_nonprofit_institute_accepted_forms_list'),
]