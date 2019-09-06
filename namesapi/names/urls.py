from django.urls import path

from .views import NameList, names_list, NameDetail

app_name = 'names'

urlpatterns = [
    path("", NameList.as_view(), name="name_list"),
    path("<int:pk>/", NameDetail.as_view(), name="name_detail"),
]


