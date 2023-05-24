from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "IceCream Admin"
admin.site.site_title = "Icecream Portal"
admin.site.index_title = "Welcome to IceCream Research Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]


