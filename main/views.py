from django.shortcuts import render
# from django.http import HttpResponse


posts = [
    {
        'author': 'MikeMDC',
        'title': 'new post!',
        'content': 'ha sike',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'MikeMDC1',
        'title': 'secnd post!',
        'content': 'ha ddddd',
        'date_posted': 'August 27, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/home.html', context)

def news(request):
    return render(request, 'main/news.html', {'title': 'News'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def my_stats(request):
    return render(request, 'main/my_stats.html', {'title': 'Stats'})


def clients(request):
    return render(request, 'main/clients.html', {'title': 'Clients'})

