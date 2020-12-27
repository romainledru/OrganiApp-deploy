from django.forms import TextInput, ModelForm, DateField, DateInput, SelectDateWidget
from .models import Item
from django.forms.utils import ErrorList
from django import forms
from django.db import models


class inputItem(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'date_limit']
        widgets = {
            'name': TextInput(attrs={
                'class': 'search-txt',
                'placeholder': 'Task here ...',
                }),
            'date_limit': SelectDateWidget(attrs={'class': 'date'}),
        }

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])