from django.urls import path
from . import views

urlpatterns = [
    path('car/', views.index, name="car"),
    path('page/<int:id>', views.page, name="page"),
    path('pages/', views.pages, name="pages"),
   
]
