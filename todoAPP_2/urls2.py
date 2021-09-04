from django.urls import path

from todoAPP_2 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.page_2, name='page 2'),
    path('base', views.base, name='base'),
    path('delete/<int:my_note_id>/', views.delete, name='delete'),
]
