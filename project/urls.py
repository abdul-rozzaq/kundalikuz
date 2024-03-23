from django.urls import path

from project.views import home_page, day_page, login, logout, register, delete_content, delete


urlpatterns = [
    path('', home_page, name='home'),
    path('day/<uuid:pk>/', day_page, name='day'),
    
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    
    path('delete-content/<uuid:pk>/', delete_content, name='delete_content'),
    path('delete/<uuid:pk>/', delete, name='delete')
]