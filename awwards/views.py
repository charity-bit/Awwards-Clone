from django.shortcuts import render,redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from .forms import CustomAuthForm,RegistrationForm

from .models import Project,User,Profile

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
    projects = Project.objects.all().order_by('-date_submited')
    user = request.user
    context = {
        'projects':projects,
        'user':user
    }
    return render(request,'awwards/index.html',context)


