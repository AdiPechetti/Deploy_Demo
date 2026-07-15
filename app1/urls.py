from django.urls import path
from . import views

urlpatterns =  [
    path('create/',views.create),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('read/',views.read)
]