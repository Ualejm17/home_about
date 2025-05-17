# configurar un parametro
from django.urls import path
from .views import HomePageView
from .views import AboutPageView


urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
# urlpatterns es una lista de rutas
# primero creamos template, luego se agrega a settings.py,
# luego se crea la vista en views.py, y se agrega a urls.py el path

# para crear una vista de un nuevo template, se crea el template
# se crea la vista en views.py, y se agrega a urls.py el path, luego se agrega eso a urls.py de django_base