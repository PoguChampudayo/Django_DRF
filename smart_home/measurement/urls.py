from django.urls import path

from .views import AddSensorView, SingleSensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('admin/', admin.site.urls)
    path('sensors/', AddSensorView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
