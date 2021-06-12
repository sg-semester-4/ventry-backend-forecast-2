from django.urls import include, path
from rest_framework import routers
from .views import SalesForecast, ControlsForecast, StocksForecast


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<str:item_id>/sales', SalesForecast.as_view()),
    path('<str:item_id>/controls', ControlsForecast.as_view()),
    path('<str:item_id>/stocks', StocksForecast.as_view()),
]
