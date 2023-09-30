from . import views
from django.urls import path, include
app_name = 'storeapp'
urlpatterns = [

    path('',views.allprodca,name='allprodca'),
    path('<slug:c_slug>/',views.allprodca,name='products_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetail,name='prodcadetail')
]
