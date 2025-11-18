from django.shortcuts import render

def homepage_view(request):
    return render(request, 'store/home_page.html')
