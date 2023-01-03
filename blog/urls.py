from django.urls import path
from rest_framework import routers
from .views import CategoryView

router=routers.DefaultRouter()
router.register("category",CategoryView)

urlpatterns = [
    # path('category/',)
]