from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:book_id>/download/', views.download_book, name='download_book'),
    path('<int:book_id>/read/', views.read_book, name='read_book'),
]