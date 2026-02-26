from django.shortcuts import render

class CustomErrorMiddleware:
    """
    DEBUG True yoki False bo'lishidan qat'iy nazar
    xatolarni custom template orqali chiqaradi.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.status_code == 404:
                return render(request, '404.html', {'error': 'Sahifa topilmadi.'}, status=404)
            if response.status_code == 403:
                return render(request, '403.html', {'error': 'Sizda bu sahifaga kirish ruxsati yo‘q.'}, status=403)
            if response.status_code == 500:
                return render(request, '500.html', {'error': 'Serverda xato yuz berdi.'}, status=500)
            return response
        except Exception as e:
            return render(request, '500.html', {'error': 'Serverda xato yuz berdi.'}, status=500)
