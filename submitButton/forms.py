from django import forms
from django.db import models
from django.forms import fields
from .models import TestModel


class FormSumbit(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
