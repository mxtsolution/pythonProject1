from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", views.hem, name="hem"),
    path("bla/", views.bla, name="bla"),
    path('planera/', views.planera, name="planera"),
    path('del/<int:item_id>',views.remove,name="del"),
    path('show/',views.show,name="show"),
    path('skapa/', views.skapa, name="skapa"),
    path('sign/<item_id>/<stats>', views.signering, name="signering"),
    path('uppdatera/<item_id>', views.uppdatera, name="uppdatera"),


]
