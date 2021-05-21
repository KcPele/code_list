from django.shortcuts import render

# create your website view
def home(request):
    return render(request, 'base.html')
