from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ="index"),
    path('about/', about, name = "about"),
    path('index_1/', index_1, name = "index_1"),
    path('contact/', contact, name = "contact"),
    #path('main/', main, name = "main"),
    path('blog/', blog, name = "blog"),
    path('prevention/', prevention, name = "prevention"),
    path('single/', single, name = "single"),
    path('symptoms/', symptoms, name = "symptoms"),
    path('how_to_prevent/', how_to_prevent, name="prevention"),
]