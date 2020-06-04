from django.core.paginator import Paginator
from rest_framework.response import Response


def create_response(data, code, message=None, name="data", extra={}):
    """Utility method which could be common to all apis to send response"""

    if not message:
        if code == 400:
            message = "Bad request"

    return Response(
        {name: data, "message": message, "code": code, "extra": extra}, code
    )


def pagination_on_queryset(queryset, page, per_page_items=10):
    """utility method to create paginated response over a queryset
    :returns list of two elements 1: total pages which can be created over provided queryset with per_page_items"""

    p = Paginator(queryset, per_page_items)

    try:
        page_instance = p.page(page)
    except:
        return p.num_pages, []

    return p.num_pages, page_instance.object_list
