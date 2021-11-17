from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),

    path('att-list/', views.ShowAll, name='att-list'),
    path('att-detail/<int:pk>/', views.ViewAtt, name='att-detail'),
    path('att-create/', views.CreateAtt, name='att-create'),
    path('att-update/<int:pk>/', views.updateAtt, name='att-update'),
    path('att-delete/<int:pk>/', views.deleteAtt, name='att-delete'),

]
