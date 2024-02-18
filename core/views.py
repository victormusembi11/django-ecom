"""Core views."""

from django.shortcuts import render, redirect

from item.models import Category, Item
from core.forms import SignupForm


def index(request):
    """View for home page."""
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    """View for contact page."""
    return render(request, "core/contact.html")


def signup(request):
    """View for signup page."""
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})
