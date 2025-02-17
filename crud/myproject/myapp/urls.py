from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('home/',views.home,),
    path("register/",views.register),
    path("addmission/",views.addmission),
    path("student_login/",views.student_login),
    path("admin_login/",views.admin_login),
    path("admin/",views.admin),
    path("add_course/",views.add_course),
    path("course_view/",views.course_view),
    path("course_dekho/",views.course_dekho), 
    path("student/",views.student),
    path("student_list/",views.student_list),
    path("edit_course/<int:id>",views.edit_course),
    path("update_course/<int:id>",views.update_course),
    path("delete_course/<int:id>",views.delete_course),
    path("student_edit/",views.student_edit),
    path("edit_student/<int:id>",views.edit_student),
    path("update_student/<int:id>",views.update_student),
    path("delete_student/<int:id>",views.delete_student),
    path("subject_view/<int:id>",views.subject_view),
    path("add_subject/",views.add_subject),
    path("student_course_view/",views.student_course_view),
]