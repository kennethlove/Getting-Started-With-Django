from django.views.generic import list_detail, date_based

from blog.models import Blog, Post

def blog(request, slug):
    posts_blog = Blog.objects.get(slug=slug)
    queryset = Post.objects.get_visible().filter(blog__slug=slug)

    return date_based.archive_index(request, queryset, date_field="publish_at",
                                    extra_context={ 'blog': posts_blog })

def archive_year(request, slug, y):
    posts_blog = Blog.objects.get(slug=slug)
    queryset = Post.objects.get_visible().filter(blog__slug=slug)

    return date_based.archive_year(request, y, queryset, date_field="publish_at",
                                   make_object_list=True,
                                   extra_context={ 'blog': posts_blog })

def archive_month(request, slug, y, m):
    posts_blog = Blog.objects.get(slug=slug)
    queryset = Post.objects.get_visible().filter(blog__slug=slug)

    return date_based.archive_month(request, y, m, queryset, date_field="publish_at",
                                   month_format="%m",
                                   extra_context={ 'blog': posts_blog })

def post(request, blog, slug):
    queryset = Post.objects.get_visible().filter(blog__slug=blog)

    return list_detail.object_detail(request, queryset, slug=slug)

