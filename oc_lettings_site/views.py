from django.shortcuts import render


def index(request):
    """
    Renders the index page.

    Args:
        request: HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    return render(request, "index.html")
