from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone

from .models import Post, Category


def index(request):
    template_name = 'blog/index.html'

    post_list = Post.objects.all()
    post_list = post_list.filter(
        Q(is_published=True)
        & Q(pub_date__lt=timezone.now())
        & Q(category__is_published=True)
    ).order_by(
        '-pub_date'
    )[:5]

    context = {
        'post_list': post_list
    }

    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.filter(
            Q(is_published=True)
            & Q(pub_date__lt=timezone.now())
            & Q(category__is_published=True)
        ),
        pk=id
    )

    context = {
        'post': post
    }

    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_list = Post.objects.filter(
        Q(is_published=True)
        & Q(pub_date__lt=timezone.now())
        & Q(category__pk=category.pk)
        & Q(category__pk=category.pk)
    )

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template_name, context)
