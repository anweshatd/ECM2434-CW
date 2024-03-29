from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#extending the in-built UserCreationForm
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2") #for ordering

    #saving and adding to database
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user