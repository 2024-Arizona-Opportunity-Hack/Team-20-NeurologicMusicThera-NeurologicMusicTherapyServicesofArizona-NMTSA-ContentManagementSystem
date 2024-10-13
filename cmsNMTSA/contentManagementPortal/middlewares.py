import re
from django.shortcuts import redirect
from contentManagementPortal.models import AccessGroup
from django.db.models import Q

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

def check_admin_group(get_response):
    urls = [
        r'^/cms/dashboard/admin$'
    ]
    check_urls = [re.compile(url) for url in urls]

    def middleware(request):
        path = request.path_info
        if any(url.match(path) for url in check_urls):
            try:
                group = AccessGroup.objects.get(users=request.user, name="admin")
                response = get_response(request)
                return response
            except AccessGroup.ObjectDoesNotExist:
                return redirect("accounts:signUp")
        response = get_response(request)
        return response
    return middleware

def check_private_group(get_response):
    urls = [
        r'^/cms/dashboard/admin$'
    ]
    check_urls = [re.compile(url) for url in urls]

    def middleware(request):
        path = request.path_info
        if any(url.match(path) for url in check_urls):
            try:
                group = AccessGroup.objects.get(Q(users=request.user) & Q(name__in=["admin", "private"]))
                response = get_response(request)
                return response
            except AccessGroup.ObjectDoesNotExist:
                return redirect("accounts:signUp")
        response = get_response(request)
        return response
    return middleware