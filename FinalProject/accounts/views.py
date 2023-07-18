from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views, login, get_user_model  # login, logout
from django.urls import reverse_lazy
from django.views import generic as views  # register view
from FinalProject.accounts.forms import RegisterUserForm
from FinalProject.destinations.models import DreamDestination
from FinalProject.trips.models import VisitedPlace
from FinalProject.common.models import Post


class RegisterUserView(views.CreateView):
    template_name = 'user/register-user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy("home page")

    def form_valid(self, form):  # login
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user/login-user.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfilePageUserView(views.TemplateView):
    template_name = 'user/profile-page-user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        dream_destinations_count = DreamDestination.objects.filter(user=user).count()
        visited_places_count = VisitedPlace.objects.filter(user=user).count()
        user_posts_count = Post.objects.filter(posted_by_user=user).count()

        context['dream_destinations_count'] = dream_destinations_count
        context['visited_places_count'] = visited_places_count
        context['user_posts_count'] = user_posts_count

        return context
