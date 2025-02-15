from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    duration = models.IntegerField(help_text="Kurs davomiyligi oylarda kiritiladi.")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

LESSON_DAYS = (
    ('toq',"Dushanba Chorshanba Juma"),
    ('juft',"Seshanba Payshanba Shanba"),
    ('harkuni',"Yakshanbadan tashqari harkuni."),
)

class Teacher(models.Model):
    CONTRACT_TYPE = (
        ('percent',"Foiz"),
        ('student',"Talaba soniga qarab"),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250,blank=True, null=True)
    last_name = models.CharField(max_length=250,blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True,blank=True, null=True)
    phone = models.CharField(max_length=250,blank=True, null=True)
    address = models.CharField(max_length=250,blank=True, null=True)
    contract_type = models.CharField(max_length=250, choices=CONTRACT_TYPE, default='percent')
    contract_percent_value = models.PositiveIntegerField(default=0)
    contract_student_value = models.PositiveIntegerField(default=0, help_text="O'quvchi sonidan to'lov.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return self.first_name + " " + self.last_name

class Group(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='groups')
    lesson_start_time = models.TimeField(blank=True, null=True) 
    lesson_end_time = models.TimeField(blank=True, null=True) 
    lesson_started_date = models.DateField(blank=True, null=True)
    lesson_days = models.CharField(max_length=250, choices=LESSON_DAYS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teacher_groups')

    def __str__(self):
        return self.name

STUDENT_STATUS = (
    ('lead',"Lead"),
    ('testing_period',"Testing Period"),
    ('active',"Active"),
    ('frozen',"Frozen"),
    ('archived',"Archived"),
)

class Student(models.Model):
    first_name = models.CharField(max_length=250,blank=True, null=True)
    last_name = models.CharField(max_length=250,blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True,blank=True, null=True)
    phone = models.CharField(max_length=250,blank=True, null=True)
    parents_phone = models.CharField(max_length=250,blank=True, null=True)
    address = models.CharField(max_length=250,blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='students',blank=True, null=True)
    status = models.CharField(max_length=250, choices=STUDENT_STATUS, default='lead')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
