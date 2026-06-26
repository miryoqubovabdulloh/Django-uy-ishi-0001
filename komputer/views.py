from django.shortcuts import render

# Create your views here.
def kp_list(request):
    return render(request, 'komputer.html')