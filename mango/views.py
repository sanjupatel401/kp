from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import product
from django.contrib import messages

# Create your views here.


def home(request):

    pro=product.objects.all()
    return render(request,'index.html',{'product':pro})

def allprod(request):
    return redirect(home)

def clouth(request):
    cl=product.objects.filter(category='clouth')
    return render(request,'index.html',{'clouths':cl})

def electronic(request):
    el=product.objects.filter(category='electronic') 
    return render(request,'index.html',{'electronic':el}) 

def mobile(request):
    m=product.objects.filter(category='mobile') 
    return render(request,'index.html',{'mobile':m})   


def adminpannel(request):

    pro =product.objects.all()
    return render(request,'admin.html',{'products':pro})


def addproduct(request):
    if request.method =='POST':
        fm=request.POST
        name=fm.get('proname')
        price=fm.get('proprice')
        details=fm.get('prodetails')
        brand_name=fm.get('probrand')
        link=fm.get('prolink')
        category=fm.get('procategory')
        image=request.FILES['proimage']


 

        pro=product(name=name,price=price,details=details,brand_name=brand_name,link=link,category=category,image=image)

        pro.save()  

        return HttpResponse('product add successflly')
      
 
      
    else:
        return HttpResponse('this request not vaild')


def search(request):
    search_qurry=request.GET['search']
    products=product.objects.filter(name__icontains=search_qurry)
    allproduct={'allproduct':products}
    return render(request,'index.html',allproduct)

def delete(request,  id=""):
    del_product=product.objects.all(pk=id)
    del_product.delete()
    return redirect(adminpannel)
