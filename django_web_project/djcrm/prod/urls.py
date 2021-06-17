from django.urls import path
from . import views

urlpatterns=[

    path("p_a/",views.a),
    path("p_b/",views.b),

]