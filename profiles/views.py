from django.shortcuts import render

from profiles.models import Profile


def index(request):
    """
    Renders the index page displaying a list of profiles.

    Args:
        request: HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renders the profile page for the specified user.

    Args:
        request: HttpRequest object representing the HTTP request.
        username (str): Username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: Rendered HTML response.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)


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
