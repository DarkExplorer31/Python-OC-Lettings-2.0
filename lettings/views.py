from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Renders the index page for lettings.

    Retrieves all lettings from the database and passes them to the template.

    Args:
        request: HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Renders the details page for a specific letting.

    Retrieves the letting with the given ID from the database and passes its
    title and address to the template.

    Args:
        request: HttpRequest object representing the HTTP request.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
