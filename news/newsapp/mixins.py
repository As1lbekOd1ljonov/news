from .models import News

class SongiYangilikMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songi_yangilik'] = News.objects.order_by('-published')[:11]
        return context


class NewsListMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dolzarb_xabarlar'] = (
            News.objects
            .filter(is_featured=True)
            .order_by('-published')[:5]
        )

        context['songi_yangilik'] = (
            News.objects
            .filter(is_featured=False)
            .order_by('-published')[:11]
        )

        context['popular_news'] = (
            News.objects
            .order_by('-view')[:5]
        )

        return context
