from django.shortcuts import redirect
from django.urls import reverse

class RedirectAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_index_url = reverse('admin:index')

        if (
            request.user.is_authenticated and
            request.path == admin_index_url and
            not request.session.get('visited_custom_dashboard')
        ):
            request.session['visited_custom_dashboard'] = True
            return redirect('/custom_dashboard/')

        return self.get_response(request)
