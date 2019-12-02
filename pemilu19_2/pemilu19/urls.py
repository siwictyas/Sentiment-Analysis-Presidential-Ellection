from django.contrib import admin
from django.urls import path, include

from . import views
from jokowi import views as jokowiViews
from prabowo import views as prabowoViews

# from about import views as aboutViews

urlpatterns = [
    path('',views.index), #home ambil data views.index (yg ada indo_pos dll buat grafik)
    path('prabowo/',views.index02), #prabowo ambil data khusus utk 02 di hlm topmodel
    path('jokowi/',views.index01),
    # path('admin/', admin.site.urls),
    # path('blog/',pemiluViews.index), #biar dia tau blog itu punya views. biar ga tabrakan
    #ambil views di project pemilu, yg index
    # path('about/', aboutViews, index),
    # path('jokowi/',include('jokowi.urls')),
    # path('prabowo/',include('prabowo.urls')),
    # path('api/data/',views.get_data), 
    # path('about/',aboutViews.index),
]
