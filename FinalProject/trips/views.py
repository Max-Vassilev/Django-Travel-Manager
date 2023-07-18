from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from FinalProject.trips.forms import AddEditTripForm
from FinalProject.trips.models import VisitedPlace

UserModel = get_user_model()


class VisitedPlacesView(LoginRequiredMixin, views.DetailView):
    template_name = 'trips/visited-places.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visited_places'] = self.request.user.visitedplace_set.all()

        return context


class TripAddView(LoginRequiredMixin, views.CreateView):
    form_class = AddEditTripForm
    template_name = 'trips/add-trip.html'

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy("visited places", args=[user_pk])

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@login_required
def trip_delete(request, pk):
    trip = VisitedPlace.objects.filter(pk=pk).first()

    trip.delete()
    user_pk = request.user.pk
    return redirect("visited places", pk=user_pk)


@login_required
def trip_edit(request, pk):
    trip = VisitedPlace.objects.filter(pk=pk).first()
    form = AddEditTripForm(instance=trip)

    if request.method == "POST":
        form = AddEditTripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            user_pk = request.user.pk
            return redirect("visited places", pk=user_pk)

    context = {
        "form": form,
        "trip": trip
    }

    return render(request, "trips/edit-trip.html", context)
