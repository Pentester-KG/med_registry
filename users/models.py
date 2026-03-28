from django.contrib.auth.models import User
from django.db import models
from users.constants import SPECIALIZATION_CHOICES




class Doctor(User):
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    cabinet = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f"Dr. {self.get_full_name()} — {self.specialization}"

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        app_label = 'users'  #

class DoctorSchedule(models.Model):
    DAYS = [(0,"Пн"),(1,"Вт"),(2,"Ср"),(3,"Чт"),(4,"Пт"),(5,"Сб"),(6,"Вс")]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="schedules")
    weekday = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(default=30)

    class Meta:
        unique_together = ("doctor", "weekday")

class Patient(User):
    genders = [('M', 'Мужской'), ('F', 'Женский')]
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=1, choices=genders, blank=True)

    def __str__(self):
        return f"{self.get_full_name()})"