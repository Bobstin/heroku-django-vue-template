from django.shortcuts import render


# Create your views here.
def example_page(request):
    example_django_variable = "Django is great for backend development!"
    return render(request, "example_app/example_page.html", {'example_django_variable': example_django_variable})
