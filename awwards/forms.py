from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth.models import User
from django import forms

from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField

from awwards.models import Project,Category,Tags, Vote
class CustomAuthForm(AuthenticationForm):  
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'placeholder':'Password'})
        

    

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'E-mail'})
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat Password'})




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {"tags":CheckboxSelectMultiple(),}
        fields = ['sitename','url','description','image','designer_name','designer_url','country','tags']


    def __init__(self, *args, **kwargs):
        
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = Tags.objects.all()


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['design','usability','content']




