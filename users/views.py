# views.py
from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientRegistrationView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

# views.py
from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        print("POST данные:", request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']            
            if Patient.objects.filter(username=phone).exists():
                form.add_error('phone', 'Пациент с таким номером уже зарегистрирован.')
            else:
                patient = form.save(commit=False)
                patient.username = phone
                patient.save()
                return redirect('home')
        else:
            print("Ошибки формы:", form.errors)
    else:
        form = PatientRegistrationForm()

    return render(request, 'users/register.html', {'form': form})