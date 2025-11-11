from django.urls import path
from .views import CurrentDateView, RandomNumberView, HelloWorldView, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view(), name='current_datetime'),
    path('random/', RandomNumberView.as_view(), name='random_number'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('', IndexView.as_view(), name='other_index'),
]