from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def index(request):
    lower=request.POST.get("lower","")
    upper=request.POST.get("upper","")
    number=request.POST.get("number","")
    symbol=request.POST.get("symbol","")
    print(lower,upper,number,symbol)
    
    lowers= "abcdefghijklmnopqrstuvwxyz"
    uppers= "ABCDEFGHIIKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[J00*:/,.--"
    all = lower+ upper + number + symbol
    length = 16
    password ="".join (random. sample (all, length))
    print(password)
    return render(request,'index.html',{'password':password}) 







    #  lower= "abcdefghijklmnopqrstuvwxyz"
    # upper= "ABCDEFGHIIKLMNOPQRSTUVWXYZ"
    # numbers = "0123456789"
    # symbols = "[J00*:/,.--"
    # all = lower+ upper + numbers +symbols
    # length = 16
    # password ="".join (random. sample (all, length))
    # print(password)
