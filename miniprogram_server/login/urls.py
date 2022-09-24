from django.urls import path
from .views import load_wmsinfo, login_views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # login/
    path('', login_views),
    path('/dowload', load_wmsinfo)
]
