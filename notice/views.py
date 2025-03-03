from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Notice
from .forms import CommentForm
from category.models import Category
from taggit.models import Tag
from django.db.models import Q


# Create your views here.
def notice_list(request):
    notice_list = Notice.objects.all()
    first_notice = Notice.objects.first()

    paginator = Paginator(notice_list, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    context = {
        'notices': notices,
        'first_notice': first_notice,
    }

    return render(request, 'notice_list.html', context)


def search_notices(request):
    query = request.GET.get('q', '')
    notices = Notice.objects.none()

    if query:
        notices = Notice.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    paginator = Paginator(notices, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    context = {
        'notices': notices,
        'query': query,
        'is_searching': bool(query),
    }

    return render(request, 'search_results.html', context)



def show_notice(request, id):
    notice = get_object_or_404(Notice, id=id)
    comments = notice.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = notice
            comment.user = request.user
            comment.save()
            return redirect('notice', id=notice.id)
    
    context = {
        'notice': notice,
        'comments': comments,
        'form': form,
    }

    return render(request, 'notice.html', context)


def show_notice_for_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    notice_list = Notice.objects.filter(category=category)

    first_notice = notice_list.first()
    notices = notice_list[1:]

    paginator = Paginator(notices, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    return render(request, 'notice_list.html', {'notices': notices, 'first_notice': first_notice})


def tagged_notices(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    notices = Notice.objects.filter(tags__in=[tag])

    paginator = Paginator(notices, 4)
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)

    context = {
        'notices': notices,
    }

    return render(request, 'tagged_notices.html', context)