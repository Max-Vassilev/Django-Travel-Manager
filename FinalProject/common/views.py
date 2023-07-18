from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as views
from FinalProject.common.forms import SharePostForm
from FinalProject.common.models import Post


class HomePageView(views.TemplateView):
    template_name = 'core/base.html'


class AboutPageView(views.TemplateView):
    template_name = 'common/about.html'


class GalleryView(LoginRequiredMixin, views.TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


@login_required
def add_post_view(request):
    form = SharePostForm()

    if request.method == "POST":
        form = SharePostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by_user = request.user
            post.save()
            print(post.posted_by_user)
            return redirect('gallery page')

    context = {
        "form": form
    }

    return render(request, 'gallery/gallery_share_post.html', context=context)


@login_required
def post_delete(request, pk):
    post = Post.objects.filter(pk=pk).first()

    post.delete()
    user_pk = request.user.pk
    return redirect("gallery page")
