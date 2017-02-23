
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from app.models import Rule, RuleType

# Serializers define the API representation.
class RuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = ('url', 'type', 'mark', 'uri', 'method', 'createtime', 'expired', 'action', 'response', 'duration', 'domain')

class RuleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RuleType
        fields = ('url', 'name', 'priority', 'lamda', 'enable', 'optional', 'domain')


# ViewSets define the view behavior.
class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class RuleTypeViewSet(viewsets.ModelViewSet):
    queryset = RuleType.objects.all()
    serializer_class = RuleTypeSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'apis/rules', RuleViewSet)
router.register(r'apis/rule_types', RuleTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

