from django.urls import path
from .views import login_views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # login/
    path('', login_views)
]
