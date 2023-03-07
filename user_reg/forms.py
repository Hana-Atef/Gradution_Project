from django import forms
# from .models import User


# class UserForm(forms.ModelForm):
#   # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}))
#   class Meta:
#     model = User
#     fields = ('firstname','lastname','mobile','password','relation','gender')
#     labels = {
#       'firstname' : 'First Name',
#       'lastname' : 'Last Name',
#       'password': 'Password',
#       'gender' : 'Gender',
#     }
#     widgets = {
#           "password": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
#     }
#   def __init__(self,*args,**kwargs):
#     super(UserForm,self).__init__(*args,**kwargs)
#     self.fields['relation'].empty_label = "Select"    
#     self.fields['gender'].empty_label = "Select"    

    # self.fields['password'].required = False