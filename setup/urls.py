from django.contrib import admin 
from django.urls import path 
from ninja import NinjaAPI
from core.api import router as core_router 

api = NinjaAPI(title="API SEPLAN-PI")
api.add_router("/", core_router)

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('api/' , api.urls),
]
