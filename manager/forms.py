from django import forms
from landing.models import Course, Category
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'category', 'image' ,'scholorship', 'short_description', 'description','course_duration', 'credit_hour', 'entry_requirement', 'intake', 'time', 'accrediation', 'time')
        exclude = ('id',)

        labels = {
            'name':'Title of course', 
            'category':'Category', 
            'image':'Image' , 
            'short_description':'Short Description', 
            'description':'Description', 
           
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the course'}), 
            'category':forms.Select(attrs={'class':'form-control'}), 
            'image':forms.FileInput(attrs={'class':'form-control'}) , 
            'short_description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'A short description'}),
            'description':forms.Textarea(attrs = {'class':'form-control', 'placeholder':'A full description'}), 
            'scholorship':forms.Select(attrs={'class':'form-control'}), 
            'course_duration':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Total Course Duration'}),
            'credit_hour':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Total Credit Hour'}),
            'entry_requirement':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Entry requirement'}),
            'intake':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Fall, Spring'}),
            'accrediation':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Accrediation/ Associated University'}),
            'time':forms.TextInput(attrs = {'class':'form-control mt-3','placeholder':'Morning, Evening'}),

          
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        exclude = ('id',)

        labels ={
            'name':'Name',
           
        }

        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Name of category (BSCsIT).'}),
           
        }




# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username','email','password')

#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

