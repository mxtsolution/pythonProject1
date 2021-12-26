from django.urls import path
from . import views

urlpatterns = [

    path("home/", views.home, name="home"),
    path("psfiber/", views.psfiber, name="psfiber"),
    path("nyttpu/", views.nyttpu, name="nyttpu"),
    path('remove/<int:item_id>',views.remove,name="remove"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("redigera/<int:item_id>", views.redigera, name="redigera"),
    path("askande/<int:item_id>", views.skapa_askande, name="skapa_askande"),
    path("vrapport", views.vrapport, name="vrapport"),
    path("skaparapport", views.skaparapport, name="skaparapport"),
]
