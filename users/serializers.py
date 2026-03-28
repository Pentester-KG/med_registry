# serializers.py
import re
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'gender', 'phone']

    def validate_phone(self, value):
        cleaned = re.sub(r'[\s\-\(\)]', '', value)
        if cleaned.startswith('0'):
            cleaned = '+996' + cleaned[1:]
        elif cleaned.startswith('996') and not cleaned.startswith('+'):
            cleaned = '+' + cleaned
        if not re.match(r'^\+996\d{9}$', cleaned):
            raise serializers.ValidationError(
                'Введите корректный кыргызский номер: +996500123456'
            )
        return cleaned

    def validate_username(self, value):
        if not re.match(r'^[А-Яа-яЁёA-Za-z\-]+$', value):
            raise serializers.ValidationError('Имя может содержать только буквы и дефис.')
        return value.strip().title()
