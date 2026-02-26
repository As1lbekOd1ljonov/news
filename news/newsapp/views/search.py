from django.db.models import Q
from django.views.generic import ListView

from ..mixins import SongiYangilikMixin
from ..models import News


class NewsSearchView(SongiYangilikMixin, ListView):
    model = News
    template_name = 'search.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return News.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).order_by('-published')
        else:
            return News.objects.none()