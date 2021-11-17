from django.urls import path
from . import views

urlpatterns = [

    path('att-list/', views.ShowAll, name='att-list'),
    # path('time-range/<int:pk>/', views.Viewtime, name='time-range'),
    # path('att-create/', views.CreateAtt, name='att-create'),
    path('att-delete/<int:pk>/', views.deleteAtt, name='att-delete'),

]
