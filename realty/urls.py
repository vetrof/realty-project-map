
from django.urls import path
from realty.views import detail_views, index_views

# main_page/
urlpatterns = [
    path('', index_views),
    path('realty/<int:id>/', detail_views, name='detail'),

]

