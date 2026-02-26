from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView

from ..models import News, Like, SavedNews


class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)

        like_obj, created = Like.objects.get_or_create(
            user=request.user,
            news=news
        )

        if not created:
            like_obj.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({
            "liked": liked,
            "count": news.likes.count()
        })


class ToggleSaveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        news = get_object_or_404(News, pk=pk)

        obj, created = SavedNews.objects.get_or_create(user=request.user, news=news)

        if not created:
            obj.delete()
            saved = False

        else:
            saved = True

        return JsonResponse({'save':saved})


class SavedNewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = "saved_news.html"
    context_object_name = "saved_news"

    def get_queryset(self):
        return News.objects.filter(saved_by__user=self.request.user).order_by("-published")