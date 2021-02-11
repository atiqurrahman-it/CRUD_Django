from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage,name='homepage'),
    path('edit/<int:id>/',views.Edit,name='edit'),
    path('delete/<int:id>/',views.Delete,name='delete'),
]
