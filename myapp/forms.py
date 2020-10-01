from django import forms

class SampleForm(forms.Form):
    name=forms.CharField(max_length=10,required=True)
