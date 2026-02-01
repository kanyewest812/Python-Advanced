from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer


@api_view(["GET", "POST"])
def items_api(request):
    if request.method == "GET":
        qs = Item.objects.all().order_by("-created")
        return Response(ItemSerializer(qs, many=True).data)

    if request.method == "POST":
        ser = ItemSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def item_api(request, pk):
    try:
        obj = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(ItemSerializer(obj).data)

    if request.method == "PUT":
        ser = ItemSerializer(obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
