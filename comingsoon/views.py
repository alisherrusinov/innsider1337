from django.shortcuts import render
from .models import submitmodel

def home(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        model = submitmodel(text=email)
        model.save()
        template = 'comingsoon/home.html'
        return render(request, template)
    else:
        context = {}
        template = 'comingsoon/home.html'
        return render(request, template, context)

