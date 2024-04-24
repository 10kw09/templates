from django.shortcuts import render
from .models import OpenPosition

def open_positions(request):
    open_positions = OpenPosition.objects.all()
    return render(request, 'open_positions.html', {'open_positions': open_positions})