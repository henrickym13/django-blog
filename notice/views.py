from django.shortcuts import render, get_object_or_404
from .models import Notice
from category.models import Category

# Create your views here.
def notice_list(request):
    first_notice = Notice.objects.first()
    notices = Notice.objects.all()[1:]

    return render(request, 'notice_list.html', {'notices': notices, 'first_notice': first_notice})


def show_notice(request, id):
    notice = Notice.objects.get(id=id)

    return render(request, 'notice.html', {'notice': notice})


def show_notice_for_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    notices = Notice.objects.filter(category=category)

    first_notice = notices.first()
    notices = notices[1:]

    return render(request, 'notice_list.html', {'notices': notices, 'first_notice': first_notice})