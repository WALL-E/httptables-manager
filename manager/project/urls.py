
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from app.models import Role, RoleType

# Serializers define the API representation.
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration', 'domain')

class RoleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleType
        fields = ('url', 'name', 'priority', 'lamda', 'enable', 'optional', 'domain')


# ViewSets define the view behavior.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleTypeViewSet(viewsets.ModelViewSet):
    queryset = RoleType.objects.all()
    serializer_class = RoleTypeSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'apis/roles', RoleViewSet)
router.register(r'apis/role_types', RoleTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

