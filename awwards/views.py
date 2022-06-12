from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from .forms import CustomAuthForm,RegistrationForm

from .models import Project,User,Profile, Vote

from django.views.generic.edit import FormView


# Create your views here.


class CustomLoginView(LoginView):  
    template_name = 'awwards/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse_lazy('home')




class RegisterView(FormView):
    template_name = 'awwards/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


    def form_valid(self,form):
        user = form.save()
        return super(RegisterView,self).form_valid(form)


    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        
        return super(RegisterView,self).get(*args,**kwargs)



@login_required(login_url='/')
def home(request):
    if request.method == 'GET':
        projects = Project.objects.all().order_by('-date_submited')
        search_input = request.GET.get('search-area') or ''
        if search_input:
            projects = projects.filter(sitename__icontains= search_input)
        
        
        user = request.user
    context = {
        'projects':projects,
        'user':user,
        'search_input':search_input
    }
    return render(request,'awwards/index.html',context)

@login_required(login_url='/')
def profile(request,username):
    user = get_object_or_404(User,username = username)
    projects = Project.objects.filter(user=request.user)

    voted_objects = Vote.objects.filter(user = user).order_by('-date_voted')
    voted_projects = []

    for project in Project.objects.all():
        for voted_project in voted_objects:
            if project.id == voted_project.project.id:
                voted_projects.append(project)

   



    context={
        'projects':projects,
        'voted_projects':voted_projects,
        'user':user
    }


    return render(request,'awwards/profile.html',context)


