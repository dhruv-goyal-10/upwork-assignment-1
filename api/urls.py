from django.urls import path
from api.views import UnitListView, UnitVisitView

urlpatterns = [
    path("units/", UnitListView.as_view()),
    path("unit/visit/", UnitVisitView.as_view()),
]
