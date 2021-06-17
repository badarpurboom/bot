from django.urls import path
from . import views

urlpatterns=[

    path("l_a/",views.a),
    path("l_b/",views.b),
]