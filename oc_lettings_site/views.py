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


# 404 and 500 template redirection
def handler404(request, exception):
    """
    Renders the 404 error page.

    Args:
        request: HttpRequest object representing the HTTP request.
        exception: Exception object.

    Returns:
        HttpResponse: Rendered HTML response for a 404 error.
    """
    return render(request, "404.html")


def handler500(request, exception):
    """
    Renders the 500 error page.

    Args:
        request: HttpRequest object representing the HTTP request.
        exception: Exception object.

    Returns:
        HttpResponse: Rendered HTML response for a 500 error.
    """
    return render(request, "500.html")
