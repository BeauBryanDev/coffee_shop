from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.views import View

# Create your views here.

class LogoutView(View):
    """Handle logout with confirmation page"""

    def get(self, request):
        """Show logout confirmation page"""
        return render(request, 'users/logout.html')

    def post(self, request):
        """Actually logout the user"""
        logout(request)
        return redirect('home')
