# charts/views.py

from django.shortcuts import render

def chart_view(request):
    return render(request, 'chart_project\charts\chart.html')