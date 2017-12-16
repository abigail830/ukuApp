from django.shortcuts import render
from django.http import HttpResponse
from ukuApp.models import Activity
from ukuApp.models import SignupInfo


# Create your views here.
def home(request):
    all_activities = Activity.objects.all().values('id','title_text', 'desc_text', 'agreement__desc_text')
    context = {
        "all_activities": all_activities,
    }
    return render(request, "home.html", context)


def signup(request):
    return render(request, "signup.html", {"act_id":request.GET['act_id']})


def confirmation(request):
    context = {
        "name": request.POST['name'],
        "phoneNum": request.POST['phoneNum'],
        "school": request.POST['school'],
        "address": request.POST['address'],
        "idNum": request.POST['idNum'],
        "act_id": request.POST['act_id'],
        "remark": request.POST['remark']
    }
    return render(request, "confirmation.html", context)


def signup_submit(request):
    activity = Activity.objects.get(pk=request.POST['act_id'])
    s = SignupInfo(name=request.POST['name'],
                   phoneNum=request.POST['phoneNum'],
                   school=request.POST['school'],
                   address=request.POST['address'],
                   idNum=request.POST['idNum'],
                   remark=request.POST['remark'],
                   activity = activity
                   )
    s.save()
    return render(request, "signupSuccess.html")
