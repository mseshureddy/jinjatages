from django.shortcuts import render

# Create your views here.
def fun1(request):
    d={'a':'seshu'}
    return render(request,'jinga.html',d)

def condtion(request):
    d1={'a': 56}
    return render(request,'condtion.html',d1)