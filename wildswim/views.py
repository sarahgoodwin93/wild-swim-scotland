from django.shortcuts import render


# Handle 404 Error
def handle404View(request, exception):
    return render(request, '404.html', status=404)


# Handle 500 Error
def handle500View(request):
    return render(request, '500.html', status=500)
