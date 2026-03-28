from django.contrib import admin
from users.models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialization', 'cabinet', 'phone']
    exclude = ['username']
    def full_name(self, obj):  # ← правильно: full_name с параметром obj
        parts = [obj.last_name, obj.first_name, obj.middle_name]
        return ' '.join(p for p in parts if p).strip()
    full_name.short_description = 'ФИО'

    list_filter = ['specialization']
    search_fields = ['first_name', 'last_name', 'specialization']
    def get_fieldsets(self, request, obj=None):
        if obj is None:  # создание нового доктора
            return (
                ('Личные данные', {
                    'fields': ('first_name', 'last_name', 'middle_name','password')
                }),
                ('Профессиональные данные', {
                    'fields': ('specialization', 'photo', 'cabinet',)
                }),
            )
        else:  # редактирование существующего
            return (
                ('Личные данные', {
                    'fields': ('first_name', 'last_name', 'middle_name',)
                }),
                ('Профессиональные данные', {
                    'fields': ('specialization', 'photo', 'cabinet',)
                }),
            )
    def save_model(self, request, obj, form, change):
        if not change:
            # генерируем уникальный username из имени и фамилии
            base = f"{obj.last_name}_{obj.first_name}".lower()
            username = base
            counter = 1
            while Doctor.objects.filter(username=username).exists():
                username = f"{base}_{counter}"
                counter += 1
            obj.username = username
            obj.set_password(form.cleaned_data['password'])
        obj.save()