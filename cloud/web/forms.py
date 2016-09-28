from django.db import models

# Create your models here.

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    image = forms.ImageField()




     
#     class Meta:
#         widgets = {
#             'title' : forms.TextInput(attrs={'style' : "opacity: 0.8; float: left; height: 20px"}),
#             'file' : forms.FileInput(attrs={'style' : "opacity: 0.8; float: left; height: 20px"}),
#         }
    