from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.home, name='home'),
    path('Rofficer/', views.Rofficer, name='rofficer'),
    path('Services/', views.Services, name='Services'),
    path('About/', views.About, name='About'),
    

    
    path('personal_info/', views.personal_info, name='personal_info'), 
    path('personal_info_list/', views.personal_info_list, name='personal_info_list'),
    path('personal_info/<int:pk>/', views.personal_info_detail, name='personal_info_detail'),
    
    path('personal_info/<int:pk>/update/', views.update_personal_info, name='update_personal_info'),
    path('personal_info/<int:pk>/delete/', views.delete_personal_info, name='delete_personal_info'),
   
    
    path('id_info/', views.id_info, name='id_info'),
    path('id_list/', views.id_list, name='id_list'),
    path('id_info/<int:pk>/', views.Id_info_detail, name='id_info'),
    
    
    path('house_info/', views.house_info, name='house_info'),
    
    path('Marriage_info/', views.Marriage_info, name='marriage_info'),
    

]


