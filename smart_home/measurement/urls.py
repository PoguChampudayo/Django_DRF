from django.urls import path

from .views import SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('admin/', admin.site.urls)
    path('sensors/', SensorView.as_view()),
]
