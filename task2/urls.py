from django.urls import path
from .views import ClassView, func_view

urlpatterns = [
    path('class/', ClassView.as_view(), name='class_view'),
    path('func/', func_view, name='func_view'),
]
