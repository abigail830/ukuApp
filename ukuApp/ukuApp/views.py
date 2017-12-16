from django.shortcuts import render
from django.http import HttpResponse
from ukuApp.models import Activity

# Create your views here.
def home(request):
    first_activty = Activity.objects.first()
    context = {
        'title': first_activty.title_text,
        'desc' : first_activty.desc_text,
        'agreement': first_activty.agreement,
    }
    return render(request, "home.html", context)
