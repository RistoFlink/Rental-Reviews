from django import forms
from .models import Review
from django.forms import ModelForm

""" 
class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Please write your review here", widget=forms.Textarea(attrs={"class":"myform"})) """

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {
            "first_name":"YOUR FIRST NAME",
            "last_name":"Last Name",
            "stars":"Rating:"
        }

        error_messages = {
            "stars":{
                "min_value":"Surely it was not that bad?",
                "max_value":"Can't be greater than 5 stars!"
            }
        }