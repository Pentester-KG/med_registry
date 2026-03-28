from django.shortcuts import render
from users.forms import PatientRegistrationForm
# Create your views here.
def index(request):
    form = PatientRegistrationForm()
    form_success = False

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form_success = True
            form = PatientRegistrationForm()  # сбросить форму

    return render(request, 'doctorbase/index.html', {
        'form': form,
        'form_success': form_success,
    })
