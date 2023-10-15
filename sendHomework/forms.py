from django import forms
from django.utils import timezone

class SendForm(forms.Form):
    grade = forms.IntegerField(required=True)
    class_num = forms.IntegerField(required=True)
    number = forms.IntegerField(required=True)
    file = forms.FileField(required=True)
class classForm(forms.Form):
    grade = forms.IntegerField(required=False)
    class_num = forms.IntegerField(required=False)
    date = forms.DateField(initial = timezone.now)
