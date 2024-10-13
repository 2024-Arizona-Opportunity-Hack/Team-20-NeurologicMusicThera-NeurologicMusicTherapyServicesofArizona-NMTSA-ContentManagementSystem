import re
from django.shortcuts import redirect
from contentManagementPortal.models import Group

def mandate_login_middleware(get_response):
    # Define your URLs directly or fetch from settings
    urls = [
        r'^/cms/.*$'
    ]
    check_urls = [re.compile(url) for url in urls]

    def middleware(request):
        path = request.path_info
        if not any(url.match(path) for url in check_urls):
            if request.user.is_authenticated:
                response = get_response(request)
                return response
            else:
                return redirect("accounts:signUp")
        response = get_response(request)
        return response
    return middleware

def check_admin_group(get_responsse):
    urls = [
        r'^/cms/dashboard/admin$'
    ]
    check_urls = [re.compile(url) for url in urls]

    def middleware(request):
        path = request.path_info
        if any(url.match(path) for url in check_urls):
            try:
                group = Group.objects.get(users=request.user, name="admin")
                response = get_response(request)
                return response
            except Group.ObjectDoesNotExist:
                return redirect("accounts:signUp")
        response = get_response(request)
        return response
    return middleware