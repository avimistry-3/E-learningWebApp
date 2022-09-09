from django import forms
from myapp.models import Order

class InterestForm(forms.Form):
    CHOICES = [(1, 'YES'), (0, 'NO')]
    interested = forms.CharField(label='Interested', widget=forms.RadioSelect(choices=CHOICES))
    levels = forms.IntegerField(initial=1,)
    comments = forms.CharField(
            widget=forms.Textarea(attrs={'cols': '30', 'rows':'15'}),
            label='Additional Comments', required=False)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Student', 'course', 'levels', 'order_date']
        widgets = {
            'Student': forms.RadioSelect,
            'order_date': forms.SelectDateWidget
        }

class RegisterForm(forms.Form):
    UserName = forms.CharField(label='UserName',widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}))
    FirstName = forms.CharField(label="FirstName",widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control'}))
    LastName = forms.CharField(label="LastName",widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control'}))
    Email = forms.CharField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control'}))
    Password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    CHOICES = [(1, 'YES'), (0, 'NO')]
    IsStudent = forms.CharField(label='Are you a Student?', widget=forms.RadioSelect(choices=CHOICES))
    

# class DocumentForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )