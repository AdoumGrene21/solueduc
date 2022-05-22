from django.urls import path
from . import views

urlpatterns = [
			path('', views.index, name='dashboard-index'),
			path('formations', views.formations, name='dashboard-formations'),
            path('orientations', views.orientations, name='dashboard-orientions'),
            path('forums', views.forums, name='dashboard-forums'),
            path('activites', views.activites, name='dashboard-activites'),
            path('view_cours/<cour_id>', views.views_formation, name='dashboard-cour'),
		]
