"""Core app Url patterns"""

from core import views as core_views
from django.urls import path

urlpatterns = [
    path("demo/", core_views.DemoViewset.as_view()),
    path("sign-up/", core_views.SignUpViewSet.as_view()),
    path('sign-in/', core_views.SignInViewset.as_view()),
    path("get-activities/", core_views.ActivitiesViewSet.as_view())
]
