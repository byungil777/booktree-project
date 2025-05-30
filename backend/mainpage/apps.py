from django.apps import AppConfig


class MainpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.mainpage'  # ✅ 전체 경로로 수정
