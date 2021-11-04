from django.urls  import path
from . import views




urlpatterns = [
    path('',views.home,name='home'),
    path('clouth/',views.clouth,name='clouthus'),
    path('electronic/',views.electronic,name='eletronicus'),
    path('mobile/',views.mobile,name='mobileus'),
    path('allprod/',views.allprod,name='allprod'),
    path('adminpannel/',views.adminpannel,name='admin'),
    path('adminpannel/addpro/',views.addproduct,name='addproduct'),
    path('search',views.search,name='search_result'),
    path('delete/<int:id>/',views.delete,name='delete_product'),

  
]