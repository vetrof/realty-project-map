
from django.urls import path
from realty.views import detail_views

urlpatterns = [
    path('realty/<int:id>/', detail_views, name='detail_view'),

]

