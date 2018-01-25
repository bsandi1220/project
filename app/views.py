from django.shortcuts import render
from django.http import HttpResponse
from app.models import User
# Create your views here.

#Home
def index (request):
    return render(request,'app/index.html')


def user (request):
    list_user = User.objects.order_by('first_name')
    my_dict = {'records':list_user}
    return render(request,'app/user.html',context=my_dict)
