from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from ..models import News, CategoryNews


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_staff:
            context['news_list'] = News.objects.all().order_by('-published')
            context['categories'] = CategoryNews.objects.all().order_by('-id')
        else:
            context['news_list'] = None

        return context



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'avatar']
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user