from django import forms

from checkbookprice.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
        widgets = {     # default값 변경시 작성
            'image': forms.FileInput(attrs={'class': 'file', 'onchange': 'imageView(this)'}),
        }
