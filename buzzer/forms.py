from django import forms
from .models import Buzz

class BuzzForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter Your Buzz!",
                "class":"form-control",
            }
        ),
        label="",
    )

    class Meta:
        model = Buzz
        exclude = ("user",)   