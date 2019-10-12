from django.urls import path
from api.views import SuggestView

# namespacing app
app_name = 'api'

urlpatterns = [
    path('suggest-movie', SuggestView.as_view(), name='suggest-movie'),
]
