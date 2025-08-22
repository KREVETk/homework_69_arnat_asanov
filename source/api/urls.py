from django.urls import path
from .views import calculate

urlpatterns = [
    path("add/", lambda r: calculate(r, "add")),
    path("subtract/", lambda r: calculate(r, "subtract")),
    path("multiply/", lambda r: calculate(r, "multiply")),
    path("divide/", lambda r: calculate(r, "divide")),
]
