from django import forms
from django.forms import ModelForm
from .models import UploadImage

class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = "__all__"
        labels = {
            'user':'',
            'image':'',
        }
       # widgets = {
          #  'user': forms.TextInput(attrs= {'class : form-control'}),
           # 'image': forms.ImageField(attrs= {'class : form-control'}),

        #}

