from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='dashboard'),
    # LEADS START
    path('leads/', views.LeadsView.as_view(), name='leads'),
    path('lead/delete/<pk>', views.lead_delete_view, name='lead_delete'),
    # LEADS  END
    # GROUPS 
    path('groups', views.GroupsView.as_view(), name="groups"),
    path("group/add", views.create_group, name="group_add"),
    path("group/delete/<pk>", views.group_delete, name="group_delete"),
    path("group/update/<pk>", views.GroupUpdateView.as_view(), name="group_update"),
    path("group/<pk>", views.GroupDetailView.as_view(), name="group_detail"),
    # COURSES 
    path("course/add", views.create_course, name="course_add"),
    path("course/edit/<pk>", views.CourseUpdateView.as_view(), name="course_update"),
    path("course/delete/<pk>", views.CourseDeleteView.as_view(), name="course_delete"),
    # TEACHERS 
    path("teachers/", views.TeachersView.as_view(), name="teacher_list"),
    path("teacher/update/<pk>", views.TeacherUpdateView.as_view(), name="teacher_update"),
    path("teacher/delete/<pk>", views.teacher_delete, name="teacher_delete"),
    # path("teacher/create", views.TeacherCreateView.as_view(), name="create_teacher"),
]