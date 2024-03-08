from rest_framework.generics import ListAPIView

from apps.settings.models import Settings
from apps.settings.serializers import SettingSerializer

# Create your views here.
class SettingAPI(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingSerializer