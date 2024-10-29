from django import forms
from add_task.models import Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
    def __init__(self,  *args,**kwargs):
        
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs.update({"class":"w-full rounded-md px-2 py-1 mb-1"})
        self.fields['email'].widget.attrs.update({"class":"w-full rounded-md px-2 py-1 mb-1"})
        self.fields['password1'].widget.attrs.update({"class":"w-full rounded-md px-2 py-1 mb-1"})
        self.fields['password2'].widget.attrs.update({"class":"w-full rounded-md px-2 py-1 mb-1"})
        
        #Remove Help Text and error message
        
        for field_name, field in self.fields.items():
            field.help_text=None