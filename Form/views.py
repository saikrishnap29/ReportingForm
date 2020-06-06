from django.shortcuts import render,HttpResponse,redirect
from.forms import *

def home(request):
    Reporting_form = ReportingForm()
    if request.method == "POST":
        form = ReportingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "index.html", {"Reporting_form": Reporting_form})
