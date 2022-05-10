from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.


def hotelview(request):
    form = hotelform()
    if request.method == "POST":
        form = hotelform(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/waiter/")
    else:
        form = hotelform()
    con = {"form": form}
    print(con,"ssssssssssssssssss")
    return render(request, "hotel.html", con)


def palceview(request):
    form = palceform()
    if request.method == "POST":
        form = palceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hotel/")
    else:
        form = palceform()
    con = {"form": form}
    return render(request, "place.html", con)


def waiterview(request):
    form = waiterform()
    if request.method=="POST":
        form = waiterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hotel/")
    else:
        form =waiterform()
    con = {"form":form}
    return render(request, "waiter.html",con)
