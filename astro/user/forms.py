from django import forms
from .models import register,Feedback


class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = "__all__"
        exclude = {"registrationtime"}
        labels = {"name": "FullName", "gender": "Gender", "email": "Email", "contact": "Phone Number"}
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'query']
