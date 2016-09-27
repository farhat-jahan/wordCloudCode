from django.db import models

# Create your models here.

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()




     
#     class Meta:
#         widgets = {
#             'title' : forms.TextInput(attrs={'style' : "opacity: 0.8; float: left; height: 20px"}),
#             'file' : forms.FileInput(attrs={'style' : "opacity: 0.8; float: left; height: 20px"}),
#         }
    