from django.urls import path

from users.views import UserDetail

urlpatterns = [
    path('detail', UserDetail.as_view(), name='detail')
]
