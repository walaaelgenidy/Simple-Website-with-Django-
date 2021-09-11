from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from product.models import Department


def listproduct(request):
    # return HttpResponse("welcome new path")

    return render(request, "product/allproduct.html")


# Create your views here.

# def detialsproduct(request):
#     #return HttpResponse("test new route")
#     return render(request, "product/detialsproduct.html")

def aboutus(request):
    return render(request, "product/aboutus.html")


def contctus(request):
    return render(request, "product/contctus.html")


def newcourses(request):
    return render(request, "product/newcourses.html")


def az(request):
    return render(request, "product/az.html")


def cka(request):
    return render(request, "product/cka.html")


def aws(request):
    return render(request, "product/aws.html")


def devops(request):
    return render(request, "product/devops.html")


def detialsproduct(request):
    products = [
        {"name": "AZ-104: Microsoft Azure Administrator", "image": "01-az.png", "cost": "$80 USD"},
        {"name": "Certified Kubernetes Administrator (CKA)", "image": "02-cka.png", "cost": "$375 USD"},
        {"name": "AWS Certified Solutions Architect – Associate", "image": "03-aws.png", "cost": "$150 USD"},
        {"name": "AWS Certified DevOps Engineer - Professional", "image": "04-aws.png", "cost": "$300 USD"},
    ]

    productmember = Product.objects.all()

    # return HttpResponse(productmember)

    context = {"productdetials": productmember}

    return render(request, "product/detialsproduct.html", context)


def productprofile(request, product_id):
    # return HttpResponse(product_id)

    ## first way
    # product = Product.objects.filter(id=product_id)
    # # return HttpResponse(product)
    # context = {"product": product[0]}
    # return render(request, "product/productprofile.html", context)

    ## Second way
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "product/productprofile.html", context)


def addcourse(request):
    # print(request.POST["email"])
    #
    # name = request.POST["name"]
    # email = request.POST["email"]

    department = Department.objects.all()
    # print(department)
    context = {"department": department}

    print(request.POST)

    if request.POST:
        name = request.POST["name"]
        image = request.POST["image"]
        dept = Department.objects.get(pk=request.POST["dept"])
        print(type(dept))

        prd = Product()
        prd.name = request.POST["name"]
        prd.image = request.POST["image"]
        prd.email = request.POST["email"]
        prd.gender = request.POST["gender"]
        prd.details = request.POST["details"]
        prd.cost = request.POST["cost"]
        prd.dept = dept

        prd.save()
        return redirect("detials_product")

    return render(request, "product/addcourse.html", context)
