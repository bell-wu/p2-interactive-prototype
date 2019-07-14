from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
  
def touch(request):
  return render(request, 'coloring/touch.html')