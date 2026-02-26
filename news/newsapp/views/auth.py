from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password', 'avatar']
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('home')


class Logout(LogoutView):
    next_page = reverse_lazy('home')