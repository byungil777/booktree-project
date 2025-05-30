from django.contrib import admin
from django.urls import path
from backend.mainpage.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # 메인 페이지 연결
]
