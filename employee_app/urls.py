from django.contrib import admin
from django.urls import path

from employee_app import views

urlpatterns=[
    path('employees/',views.emlpoyeelistview.as_view(), name="employee_list"),
    path('employees/<int:pk>/detail/',views.emlpoyeedetailview.as_view(),name="employee_detail"),
    path('employees/create/',views.emlpoyeecreateview.as_view(),name="employee_create"),
    path('employees/<int:pk>/update/',views.emlpoyeeupdateview.as_view(),name="employee_update"),
    path('employees/<int:pk>/delete/',views.emlpoyeedeletelview.as_view(),name="employee_delete"),

]