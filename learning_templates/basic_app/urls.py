from django.urls import path, include
from basic_app import views


# For Template Tagging
app_name = 'abcd'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]


