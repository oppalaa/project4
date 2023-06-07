from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20,}
    return render(request, 'condition.html',context=d)
def condition1(request):
    d={'a':10,'b':20}
    return render(request, 'condition1.html',context=d)
def condition2(request):
    d={'a':40,'b':60,'c':10}
    return render(request, 'condition2.html',context=d)
def condition3(request):
    d={'a':50,'b':90,'c':100}
    return render(request,'condition3.html',context=d)
def condition4(request):
    d={'name':'tiru'}
    return render(request, 'condition4.html',context=d)
