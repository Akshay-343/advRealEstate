from django.shortcuts import render, redirect
from .forms import PropertyListingForm
from django.views.generic import ListView
from .models import OmahaEvent, PropertyListing


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


class OmahaEventListView(ListView):
    model = OmahaEvent
    template_name = 'omaha_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return OmahaEvent.objects.all()


def Listings(request):
    # Get all PropertyListing objects
    property_listings = PropertyListing.objects.all()

    # Pass the queryset to the template
    context = {'property_listings': property_listings}
    return render(request, 'listings.html', context)


def AddListing(request):
    if request.method == 'POST':
        form = PropertyListingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other appropriate action
            return redirect('listings.html')  # Change 'success_page' to your success URL
    else:
        form = PropertyListingForm()

    return render(request, 'add_listing.html', {'form': form})
