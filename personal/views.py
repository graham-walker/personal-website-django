import os
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import UpdateView
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from personal.models import Post, LinkPost, File
from .forms import FileForm
from itertools import chain
import operator


def index(request):
    if (request.user.is_superuser):
        project_post_count = Post.objects.all().filter(Q(category='project')).count() + LinkPost.objects.all().filter(Q(category='project')).count()
        project_posts = Post.objects.all().filter(Q(show_on_homepage=True, category='project'))
        project_linkposts = LinkPost.objects.all().filter(Q(show_on_homepage=True, category='project'))

        blog_post_count = Post.objects.all().filter(Q(category='blog')).count() + LinkPost.objects.all().filter(Q(category='blog')).count()
        blog_posts = Post.objects.all().filter(Q(show_on_homepage=True, category='blog'))
        blog_linkposts = LinkPost.objects.all().filter(Q(show_on_homepage=True, category='blog'))

    else:
        project_post_count = Post.objects.all().filter(Q(category='project', visible=True)).count() + LinkPost.objects.all().filter(Q(category='project')).count()
        project_posts = Post.objects.all().filter(Q(show_on_homepage=True, category='project', visible=True))
        project_linkposts = LinkPost.objects.all().filter(Q(show_on_homepage=True, category='project', visible=True))

        blog_post_count = Post.objects.all().filter(Q(category='blog', visible=True)).count() + LinkPost.objects.all().filter(Q(category='blog')).count()
        blog_posts = Post.objects.all().filter(Q(show_on_homepage=True, category='blog', visible=True))
        blog_linkposts = LinkPost.objects.all().filter(Q(show_on_homepage=True, category='blog', visible=True))

    project_posts = sorted(
        chain(project_posts, project_linkposts),
        key=operator.attrgetter('date_posted'),
        reverse=True
    )

    blog_posts = sorted(
        chain(blog_posts, blog_linkposts),
        key=operator.attrgetter('date_posted'),
        reverse=True
    )

    return render(
        request,
        'personal/index.html',
        {
            'project_posts': project_posts,
            'more_project_posts': project_post_count > len(project_posts),
            'blog_posts': blog_posts,
            'more_blog_posts': blog_post_count > len(blog_posts)
        },
    )


def projects(request):
    if (request.user.is_superuser):
        posts = Post.objects.all().filter(Q(category='project'))
        linkposts = LinkPost.objects.all().filter(Q(category='project'))
    else:
        posts = Post.objects.all().filter(Q(category='project', visible=True))
        linkposts = LinkPost.objects.all().filter(Q(category='project', visible=True))

    posts = sorted(
        chain(posts, linkposts),
        key=operator.attrgetter('date_posted'),
        reverse=True
    )

    paginator = Paginator(posts, per_page=3)

    page = request.GET.get('p')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'personal/projects.html',
        {'project_posts': posts}
    )

def blog(request):
    if (request.user.is_superuser):
        posts = Post.objects.all().filter(Q(category='blog'))
        linkposts = LinkPost.objects.all().filter(Q(category='blog'))
    else:
        posts = Post.objects.all().filter(Q(category='blog', visible=True))
        linkposts = LinkPost.objects.all().filter(Q(category='blog', visible=True))

    posts = sorted(
        chain(posts, linkposts),
        key=operator.attrgetter('date_posted'),
        reverse=True
    )

    paginator = Paginator(posts, per_page=3)

    page = request.GET.get('p')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'personal/blog.html',
        {'blog_posts': posts}
    )

def delete(request, pk):
    if (not request.user.is_superuser):
        return HttpResponseForbidden()

    name = request.resolver_match.view_name

    if (name == 'deleteMedia'):
        media = File.objects.all().get(id=pk)

        if (media is not None):
            media.delete()

        return HttpResponseRedirect('/media')
    else:
        return HttpResponseRedirect('/')


def logoutView(request):
    logout(request)
    return redirect('/')


def post(request, pk, slug):
    try:
        post = Post.objects.all().get(id=int(pk))
    except:
        return HttpResponseNotFound()

    if (post == None):
        return HttpResponseNotFound()
    else:
        if (post.visible == True or request.user.is_superuser):
            if slug != post.slug:
                return redirect('post', pk=post.pk, slug=post.slug, permanent=True)
            else:
                return render(request, 'personal/post.html', {'post': post})
        else:
            return HttpResponseForbidden()


class MediaView(UpdateView):
    form_class = FileForm
    model = File
    template_name = 'personal/media.html'

    def get(self, request):
        if (request.user.is_superuser):
            files = File.objects.all().order_by("-date_uploaded")

            paginator = Paginator(files, per_page=20)

            page = request.GET.get('p')
            try:
                files = paginator.page(page)
            except PageNotAnInteger:
                files = paginator.page(1)
            except EmptyPage:
                files = paginator.page(paginator.num_pages)

            form = self.form_class(None)

            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'posts': files,
                    'paginator': paginator,
                }
            )
        else:
            return HttpResponseForbidden()

    def post(self, request):

        if (not request.user.is_superuser):
            return HttpResponseForbidden()

        form = self.form_class(request.POST, request.FILES)

        if (form.is_valid()):
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']

            media = form.save(commit=False)

            if (not name):
                media.name = name
            media.file = file

            media = form.save()

            return redirect('/media')
        else:
            return HttpResponseNotFound()
