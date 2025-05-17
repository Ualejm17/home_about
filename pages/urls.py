# configurar un parametro
from django.urls import path
from .views import HomePageView
# el punto es para i

urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
]
# urlpatterns es una lista de rutas
# primero creamos template, luego se agrega a settings.py,
# luego se crea la vista en views.py, y se agrega a urls.py el path