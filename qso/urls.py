from django.urls import path

from . import views 

urlpatterns = [
    path("", views.ApiOverview, name="home"),
    path("create/", views.add_qso, name="create-qso"),
    path("all/", views.list_qso, name="list-qso"),
    path("update/<int:pk>/", views.update_qso, name="update-qso"),
    path('qso/<int:pk/delete', views.delete_qso, name="delete-qso")
]
