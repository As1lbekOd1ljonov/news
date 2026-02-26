from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..mixins import NewsListMixin, SongiYangilikMixin
from ..models import News


class NewsListView(NewsListMixin, ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        featured_ids = News.objects.filter(
            is_featured=True
        ).values_list('id', flat=True)

        latest_news = (
            News.objects
            .exclude(id__in=featured_ids)
            .order_by('-published')[:11]
        )

        latest_ids = latest_news.values_list('id', flat=True)

        return (
            News.objects
            .exclude(id__in=featured_ids)
            .exclude(id__in=latest_ids)
            .order_by('-published')
        )



class NewsDetailView(SongiYangilikMixin, DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view += 1
        obj.save()
        return obj


class NewsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = News
    fields = ['title', 'description', 'image', 'category', 'is_featured']
    template_name = 'news_create.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff



class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'description', 'image', 'category', 'is_featured']
    template_name = 'news_create.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user.is_staff


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        return self.request.user.is_staff