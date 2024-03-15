
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation
from .models import CustomUser, KYC, Customer


class KYCForm(forms.ModelForm): 
    class Meta:
        model = KYC
        fields = ('__all__')


        widgets= {
            'image':forms.FileInput(attrs={'accept':"image/*", "type":"file", 'capture':"camera", 'class':'form-control  custom-input mt-2', 'id':'image-upload' ,'onchange':"showImage(this)", 'required':False}),
            'country':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Australia' }),
            'address':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'123 Smith Street, Richmond, Victoria'}),
            'state':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Victoria'}),
            'city':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'Melbourne'}),
            'postal_address':forms.TextInput(attrs={'class':'form-control mt-2', 'placeholder':'14428. Melbourne, VIC 8001'}),
            'number':forms.NumberInput(attrs={'class':'form-control mt-2', 'placeholder':'98418161716'}),
            'gender':forms.Select(attrs={'class':'form-control mt-2'}),
            'document_type':forms.Select(attrs={'class':'form-control mt-2', 'hidden':True}),
            'date_of_birth':forms.DateInput(attrs={'type':'date','class':'form-control mt-2'}),
            
            # Licence
            'document_number':forms.NumberInput(attrs={'class':'form-control mt-2', 'placeholder':'01245422354','value':'{{cm.licence_number}}'}),
            'document_front_image':forms.FileInput(attrs={'accept':"image/*", 'capture':"camera", 'class':'form-control mt-2','onchange':"showFrontImage(this);"}),
            'document_back_image':forms.FileInput(attrs={'accept':"image/*", 'capture':"camera", 'class':'form-control mt-2','onchange':"showBackImage(this);"}),
            'issue_date' : forms.DateInput(attrs={'type':'date','class':'form-control mt-2','value':'{{cm.issue_date}}'}),
            'expiry_date' : forms.DateInput(attrs={'type':'date','class':'form-control mt-2','value':'{{cm.expiry_date}}'}),   
            
          
        }

class CustomerForm(forms.ModelForm):
   
    class Meta:
      
        model = Customer

        fields = ('__all__')

        widgets = {
            'number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'+61 4 91 575 789'}),
            'mail_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'14428. Melbourne, VIC 8001'}),
            'state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Victoria'}),
            # 'zip_code' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'30001'}),
            'city' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Melbourne'}),
            'country' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Australia'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'123 Smith Street, Richmond, Victoria'}),
            'profil_pic' : forms.FileInput(attrs={'accept':"image/*", 'class':'form-control', 'placeholder':'Profile Picture'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation

class PasswordChangeFormUpdate(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'placeholder':'Enter New Password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'placeholder':'Enter New Password Again'}),
    )
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True , 'class':'form-control', 'placeholder':'Enter Your Old Password'}
        ),
    )