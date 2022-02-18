from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path

from ab_tests.views import ExperimentListView, GroupListView


urlpatterns = [
    path('experiments/', ExperimentListView.as_view()),
    path('groups/', GroupListView.as_view()),
    #
    path('admin/', admin.site.urls),
]


admin.autodiscover()
site: AdminSite = admin.site
site.enable_nav_sidebar = False
