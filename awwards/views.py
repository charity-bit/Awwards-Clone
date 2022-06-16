
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView


from .forms import CustomAuthForm,RegistrationForm,ProjectForm,ProfileForm,VoteForm
from .models import Project,User,Profile, Vote






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
    form = ProfileForm

    voted_objects = Vote.objects.filter(user = user).order_by('-date_voted').all()

    context={
        'projects':projects,
        'voted_objects':voted_objects,
        'user':user,
        'form':form
    }

    return render(request,'awwards/profile.html',context)


class AddProjectView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'awwards/submit.html'
    form_class = ProjectForm


    def get_success_url(self):
        return reverse_lazy('profile',kwargs={
            'username':self.request.user
        })

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProjectView,self).form_valid(form)

class ProjectDetailsView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'awwards/project_detail.html'
    context_object_name = 'project'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VoteForm()

        return context
  

def rate(request):

        if request.method == 'POST':
            state = 0
            project_id = request.POST.get('project')
            project = Project.objects.filter(id = project_id).first()
            user_id = request.user

            if Vote.objects.filter(project = project,user = request.user).exists():
                Vote.objects.filter(project = project,user = request.user).delete()
                state = 0     
            else:
                state = 1
            design = request.POST.get('design')
            usability = request.POST.get('usability')
            content = request.POST.get('content')
            average_s = (int(design)+int(usability)+int(content))/3
            new_vote = Vote(user = request.user,project=project,average_score = average_s,design = int(design),usability=int(usability),content=int(content))
            new_vote.save()
            
            a_s = new_vote.average_score
            d = new_vote.design
            u = new_vote.usability
            c = new_vote.content
            user = request.user.id

        return JsonResponse({'average':a_s,'design':d,'usability':u,'content':c,'state':state,'user':user})


def update(request):
    if request.method == 'POST':
        profile = Profile.objects.filter(user=request.user)
        if profile.exists:
            profile.delete()
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                print(form.cleaned_data['bio'])
                form.save()
                return JsonResponse({'errors':True})
            else:
                return JsonResponse({'errors':True})
        else:
            return JsonResponse({'none':'No such profile'})

    else:
        form = ProfileForm()

    
    return JsonResponse({'saved':'saved'})


# def update(request):
#     bio = request.POST.get('bio')
#     profile_image = request.FILES.get('profile_pic')
#     country = request.POST.get('country')

#     if Profile.objects.filter(user = request.user).exists():
#         user_profile = Profile.objects.filter(user = request.user).first()
#         if bio:
#             user_profile.bio = bio
#         if profile_image:
#             user_profile.profile_pic = profile_image
#         if country:
#             user_profile.country = country
#         user_profile.save()

#     return JsonResponse({'success':True})
