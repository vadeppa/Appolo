from django.shortcuts import render,HttpResponseRedirect
from .models import patient

from .forms import Register
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):

    return render(request,'about.html')
def doct(request):
    if request.method == 'POST':

        form = Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['patient_name']
            phono = form.cleaned_data['patient_phono']
            age = form.cleaned_data['patient_age']
            pbm=form.cleaned_data['patient_problm']
            dob=form.cleaned_data['patient_dob']

            reg = patient(patient_name=name, patient_phono=phono,patient_age=age,patient_problm=pbm,patient_dob=dob)
            reg.save()
            form = Register()

            # return HttpResponse('<h1>Thanks</h1>')

    else:
        form = Register()
    stud = patient.objects.all()

    return render(request, 'doctors.html', {'form1': form, 'stu': stud})


def patient(request):
    if request.method=='POST':
        fm=Register(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your booking successfully')
            #return HttpResponseRedirect('/patients/')
    else:
        fm=Register()
        # return HttpResponseRedirect('/patients/')

    return render(request,'patient.html',{'form':fm})



