from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'contributors', views.ContributorsViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'issues', views.IssuesViewSet)
router.register(r'comments', views.CommentsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
