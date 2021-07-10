from django.shortcuts import render

# Create your views here.
from .forms import FormSumbit
from .models import TestModel

def formSubmit(request):
    form = FormSumbit(request.POST)
    allData = TestModel.objects.all()
    if request.method == "POST":
        if form.is_valid():
            input1 = form.cleaned_data['input1']
            input2 = form.cleaned_data['input2']
            form.save()
    return render(request, "form.html", {"form" : form, 'allData': allData})