from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def index(request):
    return rental_review(request)

def rental_review(request):
    #post request -> form contents -> thank you
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            #dictionary form i.e. {"first_name:"John}
            form.save()
            return redirect(reverse("cars:thank_you"))
    # else render form
    else:
        form = ReviewForm()
    return render(request, "cars/rental_review.html", context={"form": form})

def thank_you(request):
    return render(request, "cars/thank_you.html")