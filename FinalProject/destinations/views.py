from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from FinalProject.destinations.forms import AddEditDestinationForm
from FinalProject.destinations.models import DreamDestination
from FinalProject.trips.models import VisitedPlace

UserModel = get_user_model()


class DreamDestinationsView(LoginRequiredMixin, views.DetailView):
    template_name = 'destinations/dream-destinations.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dream_destinations'] = self.request.user.dreamdestination_set.all()

        return context


class DestinationAddView(LoginRequiredMixin, views.CreateView):
    form_class = AddEditDestinationForm
    template_name = 'destinations/add-destination.html'

    def get_success_url(self):
        user_pk = self.request.user.pk

        return reverse_lazy('dream destinations', args=[user_pk])


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@login_required
def destination_delete(request, pk):
    destination = DreamDestination.objects.filter(pk=pk).first()

    destination.delete()

    user_pk = request.user.pk
    return redirect("dream destinations", pk=user_pk)


@login_required
def destination_edit(request, pk):
    destination = DreamDestination.objects.filter(pk=pk).first()
    form = AddEditDestinationForm(instance=destination)

    if request.method == "POST":
        form = AddEditDestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            user_pk = request.user.pk
            return redirect("dream destinations", pk=user_pk)

    context = {
        "form": form,
    }

    return render(request, "destinations/edit-destination.html", context)


@login_required
def i_went_there_view(request, pk):
    destination = DreamDestination.objects.filter(pk=pk).first()

    visited_place = VisitedPlace(location=destination.location, place_photo=destination.place_photo, user=request.user)
    visited_place.save()

    destination.delete()

    user_pk = request.user.pk
    return redirect("visited places", pk=user_pk)
