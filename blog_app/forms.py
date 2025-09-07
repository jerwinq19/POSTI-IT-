from django import forms
from .models import BlogPost
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields= ['title','content']
        
        
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter your title...',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter your content...',
                    'rows': 5,   # makes it not too small
                }
            ),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Enter your username'
        })
    )
    
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Enter your password'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password.'
        })
    )
    
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password.'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g JohnDoe123'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g johndoe123@email.com'
            })
        }
    


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label="Date of birth.",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth']
        
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g John Paul'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g Naynes'
            })
        }