from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,DetailView
from django.views.generic.edit import DeleteView,UpdateView


from django.template.defaultfilters import slugify
# Create your views here.
from . models import Student, Course,Group,Teacher

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AdminDashboardView(View):
    

    def get(self, request):
        return render(request, 'index.html')


class LeadsView(ListView):
    model = Student
    template_name = 'leads.html'
    paginate_by = 15


    def get_queryset(self):
        return self.model.objects.filter(status='lead')
    
    def post(self, request):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        phone = request.POST.get('phone')
        Student.objects.create(first_name=fname, last_name=lname, phone=phone, status='lead')
        messages.success(request, 'Lid muvaffaqiyatli qo\'shildi !')
        return redirect(self.request.META.get('HTTP_REFERER'))


def lead_delete_view(request,pk):
    lead = Student.objects.get(status="lead", id=pk)
    lead.delete()
    messages.success(request, "Lid muvaffaqiyatli o'chirildi !")
    return redirect(request.META.get('HTTP_REFERER'))




class GroupsView(View):

    def get(self,request):
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        groups = Group.objects.all()
        data = {
            "courses":courses,
            "teachers":teachers,
            "groups":groups
            }
        return render(request,"group.html", context=data)


class GroupDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'

def create_group(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course_id = request.POST.get("course")
        teacher_id = request.POST.get("teacher")
        lesson_days = request.POST.get("lesson_days")
        lesson_start_time = request.POST.get("lesson_start_time")
        lesson_end_time = request.POST.get("lesson_end_time")
        print(course_id,teacher_id)
        course = Course.objects.get(id=int(course_id))
        teacher = Teacher.objects.get(id=int(teacher_id))
        Group.objects.create(
            name=name,
            slug=slugify(name),
            course=course,
            teacher=teacher ,
            lesson_days=lesson_days,
            lesson_start_time=lesson_start_time,
            lesson_end_time=lesson_end_time
        )
        messages.success(request, 'Guruh muvaffaqiyatli qo\'shildi !')

    return redirect(request.META.get('HTTP_REFERER'))

def group_delete(request,pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def create_course(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        duration = request.POST.get("duration")
        Course.objects.create(title=title,slug=slugify(title),price=price,duration=duration)
        messages.success(request, 'Kurs muvaffaqiyatli qo\'shildi !')

    return redirect(request.META.get('HTTP_REFERER'))

class GroupUpdateView(UpdateView):
    model = Group
    fields = ("name","course","teacher","lesson_days","lesson_start_time","lesson_end_time")
    success_url = "/groups"
    success_message = "Guruh muvaffaqiyatli yangilandi !"
    extra_context = {"info":"Guruhni yangilash"}
    template_name = "edit_form.html"

class CourseUpdateView(UpdateView):
    model = Course 
    fields = ("title","price","duration")
    success_url = "/groups"
    success_message = "Kurs muvaffaqiyatli yangilandi !"
    extra_context = {"info":"Kursni yangilash"}
    template_name = "edit_form.html"


class CourseDeleteView(DeleteView):
    model = Course
    extra_context = {"info":"Kursni o'chirish", "extra_info":"Tanlangan kurs ma'lumotlar omboridan o'chiri yuboriladi, rozimisiz ?"}
    success_url = "/groups"
    template_name = "edit_form.html"



class TeachersView(ListView):
    model = Teacher
    template_name = "mentor.html"

    def get_queryset(self):
        return super().get_queryset()
    

def teacher_delete(request,pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    return redirect(request.META.get('HTTP_REFERER'))


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = "/teachers"
    success_message = "Ustoz muvaffaqiyatli yangilandi !"
    extra_context = {"info":"Ustozni yangilash"}
    template_name = "edit_form.html"


class TeacherCreateView(CreateView):
    model = User
    template_name = "edit_form.html"
    form_class = UserCreationForm
    success_url = "/teachers"
    success_message = "Ustoz muvaffaqiyatli qo'shildi !"
    extra_context = {"info":"Ustozni qo'shish"}

    def form_valid(self, form): # new
        
        return super().form_valid(form)
