from .models import CategoryNews

def category_list(request):
    return {
        'category_list': CategoryNews.objects.all()
    }