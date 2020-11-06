from rest_framework.response import Response
from activity.models import ActivityPage as ActivityPageModel
from activity.serializers import ActivitySerializer
# Create your views here.

from rest_framework.views import APIView

class ActivityPageList(APIView):
    def get(self, request):
        querySet = ActivityPageModel.objects.all()
        s = ActivitySerializer(instance=querySet, many=True)
        return Response(s.data)
