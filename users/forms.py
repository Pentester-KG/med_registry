# forms.py
import re
from django import forms
from .models import Patient
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class PatientRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя', max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Иван'})
    )
    last_name = forms.CharField(
        label='Фамилия', max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Иванов'})
    )
    # убрали phone_number, оставляем только phone из Meta.fields

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone', 'gender']
        widgets = {
            'gender': forms.RadioSelect(),
        }
        labels = {
            'phone': 'Номер телефона',
        }

    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        if not re.match(r'^[А-Яа-яЁёA-Za-z\-]+$', value):
            raise forms.ValidationError('Только буквы и дефис.')
        return value.strip().title()

    def clean_last_name(self):
        value = self.cleaned_data['last_name']
        if not re.match(r'^[А-Яа-яЁёA-Za-z\-]+$', value):
            raise forms.ValidationError('Только буквы и дефис.')
        return value.strip().title()

    def clean_phone(self):  # ← название метода совпадает с полем
        value = self.cleaned_data['phone']
        cleaned = re.sub(r'[\s\-\(\)]', '', value)
        if cleaned.startswith('0'):
            cleaned = '+996' + cleaned[1:]
        elif cleaned.startswith('996') and not cleaned.startswith('+'):
            cleaned = '+' + cleaned
        if not re.match(r'^\+996\d{9}$', cleaned):
            raise forms.ValidationError('Формат: +996500123456')
        return cleaned