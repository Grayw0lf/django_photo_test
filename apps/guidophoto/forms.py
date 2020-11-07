from django import forms
from .models import UPhoto
from typing import Type, List, Dict


class UPhotoForm(forms.ModelForm):

    class Meta:
        model: Type[UPhoto] = UPhoto
        fields: List = ["comment", "photo"]

        widgets: Dict = {
            "comment": forms.Textarea(attrs={
                "class": "form-control", "id": "exampleFormControlTextarea1",
                "placeholder": "Input comment, i'm wait", "rows": "8"}),
            "photo": forms.FileInput(attrs={"class": "btn btn-dark"})}

        labels: Dict = {
            "comment": False,
            "photo": False}
