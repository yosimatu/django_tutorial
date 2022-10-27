from django.contrib import admin
from django.urls import include, path
#  path(アクセスするアドレス、呼び出す処理)
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
