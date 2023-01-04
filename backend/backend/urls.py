from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="COLVA OCR Swagger API",
        default_version='v1',
        description="2022-Winter-Bootcamp-Team-C",
        terms_of_service="https://github.com/2022-Winter-Bootcamp-Team-C",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin', admin.site.urls),
    path('api/', include(('sample_swagger.urls', 'api'))),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
