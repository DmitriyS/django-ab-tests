from django.contrib import admin
from django.urls import path

from ab_tests.views import ExperimentListView, GroupListView


urlpatterns = [
    path('experiments/', ExperimentListView.as_view()),
    path('groups/', GroupListView.as_view()),
    #
    path('admin/', admin.site.urls),
]
