from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ..mixins import SongiYangilikMixin
from ..models import News, Like, CategoryNews


class CategoryNewsListView(SongiYangilikMixin, ListView):
    model = News
    template_name = 'news_category.html'
    context_object_name = 'category_news'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['liked_posts'] = set(
                Like.objects.filter(user=self.request.user).values_list('news_id', flat=True)
            )
        else:
            context['liked_posts'] = set()
        return context


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CategoryNews
    fields = ['title']
    template_name = 'category_create.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user.is_staff


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CategoryNews
    fields = ['title']
    template_name = 'category_create.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user.is_staff


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CategoryNews
    template_name = 'category_delete.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user.is_staff