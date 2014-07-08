from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth.models import User


def prevent_dupes(backend, uid, user=None, *args, **kwargs):
    email = kwargs.get("details", {}).get("email")
    if email:
        if User.objects.filter(email=email).exists() and user is None:
            messages.warning(
                kwargs.get("request"),
                "It appears you already have an account on this site using another social account."
            )
            return redirect("home")
    return {}
