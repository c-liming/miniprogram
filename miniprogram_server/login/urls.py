from django.urls import path
from .views import login_views


urlpatterns = [
    # login/
    path('', login_views)
]
