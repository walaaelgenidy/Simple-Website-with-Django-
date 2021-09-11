
from django.contrib import admin
from django.urls import path
from product.views import listproduct, detialsproduct, aboutus, contctus, newcourses, az, cka, aws, devops, productprofile, addcourse

#from product.views import listproduct

urlpatterns = [
    path("product/", listproduct),
    path("detialsproduct/", detialsproduct, name="detials_product"),
    path("aboutus/", aboutus),
    path("contctus/", contctus),
    path("newcourses/", newcourses),
    path("az/", az),
    path("cka/", cka),
    path("aws/", aws),
    path("devops/", devops),
    path('<int:product_id>', productprofile),
    path('add', addcourse, name="add_course"),

]
