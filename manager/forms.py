from django import forms
from manager.models import BorrowList
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

class BorrowForm(forms.Form):
    pieces = forms.IntegerField()
    borrower_id = forms.IntegerField()
