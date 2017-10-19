from django.forms import ModelForm, DateInput, Select, EmailInput, FileInput, TextInput, NumberInput, \
    SelectMultiple, NullBooleanSelect, CheckboxInput
from django import forms

from parse.models import DayHistory


class DayHistoryForm(forms.ModelForm):

    class Meta:
        model = DayHistory
        fields = '__all__'