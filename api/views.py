from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from api.models import Worker, Unit
from api.serializers import UnitSerializer, VisitSerializer


class UnitListView(ListAPIView):

    serializer_class = UnitSerializer

    def get_queryset(self):
        worker_phone_number = self.request.GET.get("phone_number", None)
        return Unit.objects.filter(worker__phone_number=worker_phone_number)


class UnitVisitView(APIView):

    def post(self, request):
        # Check the errors in the request body
        serializer = VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        worker_phone_number = request.GET.get("phone_number", None)
        worker = Worker.objects.filter(phone_number=worker_phone_number).first()
        if not worker:
            return Response({"success": False, "error": "Worker not found"}, status=400)

        unit = Unit.objects.filter(id=request.data.get("unit"), worker=worker).first()
        if not unit:
            return Response(
                {
                    "success": False,
                    "error": "Unit does not belong to worker",
                },
                status=400,
            )
        serializer.save()
        return Response({"success": True, "data": serializer.data})
