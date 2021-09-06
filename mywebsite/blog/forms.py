from django import  forms
from . import models
class postforms(forms.ModelForm):
    class Meta:
        model = models.postmodel
        fields = [
            'autor',
            'judul',
            'body',
            'category',
        ]
        labels = {
            'autor':'Penulis'
        }

        widgets ={
            'judul': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder':'isi judul'


                }
            ),
            'autor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nama Penulis'

                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Isi Pesan'

                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }