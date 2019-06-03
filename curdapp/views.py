from django.shortcuts import render
from .models import ProductData
from .forms import InsertForm,UpdateForm,DeleteForm
from django.http.response import HttpResponse

def main_page_view(request):
    return render(request,'curd_main_page.html')
def create_page_view(request):
    if request.method =="POST":
        cform = InsertForm(request.POST)
        if cform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_cost = request.POST.get('product_cost')
            product_color = request.POST.get('product_color')
            product_class = request.POST.get('product_class')
            customer_name = request.POST.get('customer_name')
            customer_mobile = request.POST.get('customer_mobile')
            customer_email = request.POST.get('customer_email')

            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_color=product_color,
                product_class=product_class,
                customer_name=customer_name,
                customer_mobile=customer_mobile,
                customer_email=customer_email
            )
            data.save()
            cform = InsertForm()
            return render(request,'curd_insert_page.html',{'cform':cform})
        else:
            return HttpResponse("invalid User Data")
    else:
        cform = InsertForm()
        return render(request,'curd_insert_page.html',{'cform':cform})



def retrieve_page_view(request):
    pdata = ProductData.objects.all()
    return render(request,'curd_reterieve_page.html',{'pdata':pdata})


def update_page_view(request):
    if request.method =="POST":
        uform = UpdateForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')
            pid = ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse("Invalid Product Id")
            else:
                pid.update(product_cost=product_cost)
                uform = UpdateForm()
                return render(request,'curd_update_page.html',{'uform':uform})
        else:
            return HttpResponse("Invalid User Data")
    else:
        uform = UpdateForm()
        return render(request,'curd_update_page.html',{'uform':uform})

def delete_page_view(request):
    if request.method == "POST":
        dform = DeleteForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            pid = ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse("Product Id Is Not Available")
            else:
                pid.delete()
                dform = DeleteForm()
                return render(request,'curd_delete_page.html',{'dform':dform})
        else:
            return HttpResponse("Invalid Form")
    else:
        dform = DeleteForm()
        return render(request,'curd_delete_page.html',{'dform':dform})