from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name = 'root'),
    path('<int:page>', views.main, name = 'root_paginate'),


    path("add_author/", views.add_author, name="add_author"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path('quotes/', login_required(views.main), name='quotes'),
    path('author/<str:author_id>/', views.about, name='author'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),

]
