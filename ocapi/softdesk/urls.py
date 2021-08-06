from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_nested import routers
from . import views


router = routers.SimpleRouter()
router.register(r'projects', views.ProjectsViewSet)
contributor_router = routers.NestedSimpleRouter(router, r'projects',
                                                lookup='project')
contributor_router.register(r'users', views.ContributorsViewSet,
                            basename='contributors')
issue_router = routers.NestedSimpleRouter(router, r'projects',
                                          lookup='project')
issue_router.register(r'issues', views.IssuesViewSet,
                      basename='issues')
comment_router = routers.NestedSimpleRouter(issue_router,
                                            r'issues', lookup='issues')
comment_router.register(r'comments', views.CommentsViewSet,
                        basename='comments')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(contributor_router.urls)),
    path('', include(issue_router.urls)),
    path('', include(comment_router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('signup/', views.RegisterUser().as_view(),
         name='register_user'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
