from django.shortcuts import render
from django.http import HttpResponse
from ukuApp.models import Activity

# Create your views here.
def home(request):
    all_activities = Activity.objects.all().values('title_text','desc_text','agreement__desc_text')
    context = {
        "all_activities": all_activities,
    }
    return render(request, "home.html", context)
