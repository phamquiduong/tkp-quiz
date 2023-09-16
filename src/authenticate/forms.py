from django import forms

from authenticate.models import ClassRoom


class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name']
