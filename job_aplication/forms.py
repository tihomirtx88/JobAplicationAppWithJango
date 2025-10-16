from django import  forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80);
    email = forms.EmailField();
    last_name = forms.CharField(max_length=80);
    date = forms.DateField();
    occupation = forms.CharField(max_length=80);
