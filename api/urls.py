from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Example App API",
        default_version='0.0.1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Put your API url patterns here
urlpatterns = [

]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

