from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Notice
from category.models import Category

# Create your views here.
def notice_list(request):
    first_notice = Notice.objects.first()
    notice_list = Notice.objects.all()[1:]

    paginator = Paginator(notice_list, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    return render(request, 'notice_list.html', {'notices': notices, 'first_notice': first_notice})


def show_notice(request, id):
    notice = Notice.objects.get(id=id)

    return render(request, 'notice.html', {'notice': notice})


def show_notice_for_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    notice_list = Notice.objects.filter(category=category)

    first_notice = notice_list.first()
    notices = notice_list[1:]

    paginator = Paginator(notices, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    return render(request, 'notice_list.html', {'notices': notices, 'first_notice': first_notice})