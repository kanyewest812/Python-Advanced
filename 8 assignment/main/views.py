from django.shortcuts import render, get_object_or_404
from .models import Item

def home_page(request):
    return render(request, "main/home.html")

def items_page(request):
    data = Item.objects.all()
    return render(request, "main/list.html", {"records": data})

def item_page(request, pk):
    one = get_object_or_404(Item, pk=pk)
    return render(request, "main/detail.html", {"record": one})


