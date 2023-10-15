from .forms import SendForm,classForm
from .models import Student,Homework
from django.views import generic
from django.shortcuts import render,redirect
from urllib.parse import urlencode

# Create your views here.
class StudentsSort():
    def __init__(self,grade,_class,number):
        self._class = _class
        self.number = number
    def __lt__(self,other):
        if self.grade != other.grade:
            return self.grade < other.grade
        if self._class != other._class:
            return self._class<other._class
        else:
            return self.number<other.number
def indexView(request):
    if request.method == 'POST':
        form = SendForm(request.POST,request.FILES)
        if form.is_valid():
            student = Student.objects.get(grade = form.cleaned_data["grade"],
                                    class_num = form.cleaned_data["class_num"],
                                    number = form.cleaned_data["number"])
            file = form.cleaned_data['file']
            homework = Homework(student = student,
                                    file = file)
            homework.save()
            return render(request,'sendWork.html',{'form':form})
        return render(request,'sendWork.html',{'form':form})
    form = SendForm()
    return render(
        request,
        'sendWork.html',
        {'form':form})
class showView(generic.TemplateView):
    template_name = 'showWork.html'
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["homeworks"] = Homework.objects.all()
        return ctx
class homeView(generic.TemplateView):
    template_name = 'home.html'
class resultView(generic.TemplateView):
    template_name = "showResult.html"
    def get_context_data(self,**kwargs):
        print("get_context_data was called")
        ctx = super().get_context_data(**kwargs)
        ctx["results"] = []
        if self.request.method!="POST":
            form = classForm()
            ctx["form"] = form
            return ctx
        ctx["form"] = form = classForm(self.request.POST)
        if not form.is_valid():
            return ctx
        completed_students = Homework.objects.all().filter(now_date = form.cleaned_data["date"]).select_related('student').all()
        completed_students = list(filter(self._filter(form.cleaned_data.get("class_num"),form.cleaned_data.get("grade")),completed_students))
        students_all = sorted(Student.objects.all(),key=lambda x:StudentsSort(x.grade,x.class_num,x.number))
        for student in students_all:
            filterd_homework = list(filter(lambda x:x.student==student,completed_students))
            files = list(map(lambda x:x.file,filterd_homework))
            ctx["results"].append(Result(student,files))
        return ctx
    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return self.render_to_response(ctx)
    def _filter(self,class_num,grade):
        if class_num is None and grade is None:
            return lambda x:True
        elif class_num is None:
            return lambda x:x.student.grade == grade
        elif grade is None:
            return lambda x:x.student.class_num == class_num
        else:
            return lambda x:x.student.grade==grade and x.student.class_num == class_num
class Result():
    def __init__(self,student,files):
        self.student = student
        self.files = files
        self.files_count = len(self.files)