from django.shortcuts import render
from django.http import HttpResponse
from ukuApp.models import Activity, SignupInfo, Product


# Create your views here.
def home(request):
    all_activities = Activity.objects.all().values('id', 'title_text', 'desc_text', 'agreement__desc_text')
    context = {
        "all_activities": all_activities,
    }
    return render(request, "home.html", context)


def signup(request):
    activity = Activity.objects.get(pk=request.GET['act_id'])
    product_set = activity.products.all()
    context = {
        "activity": activity,
        "productList": product_set,
    }
    return render(request, "signup.html", context)


def confirmation(request):

    if(request.POST.__contains__('product_id')):
        product = Product.objects.get(pk=request.POST.get('product_id'))
        product_name = product.title_text
    else:
        product_name = ''


    context = {
        "name": request.POST['name'],
        "sex": request.POST['sex'],
        "sex_str": '男孩子' if request.POST['sex'] == 'M' else '女孩子',
        "phoneNum": request.POST['phoneNum'],
        "school": request.POST['school'],
        "address": request.POST['address'],
        "idNum": request.POST['idNum'],
        "act_id": request.POST['act_id'],
        "remark": request.POST['remark'],
        "product_id": product.id if request.POST.__contains__('product_id') else '',
        "product_name": product_name
    }
    return render(request, "confirmation.html", context)


def signup_submit(request):
    activity = Activity.objects.get(pk=request.POST['act_id'])

    if (request.POST.get('product_id')==''):
        product = None
    else:
        product = Product.objects.get(pk=request.POST['product_id'])

        s = SignupInfo(name=request.POST['name'],
                   sex=request.POST['sex'],
                   phoneNum=request.POST['phoneNum'],
                   school=request.POST['school'],
                   address=request.POST['address'],
                   idNum=request.POST['idNum'],
                   remark=request.POST['remark'],
                   activity=activity,
                   product=product
                   )
        s.save()

    return render(request, "signupSuccess.html")
