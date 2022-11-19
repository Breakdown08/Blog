from ..utils import *

def homepage(request):
    news = New.objects.all().filter(is_private=False)
    data = {"news": news}
    return render(request, 'Pages/HomePage.html', context=data)

def private(request):
    news = None
    if request.user.username != 'AnonymousUser':
        news = New.objects.all().filter(author=request.user.id, is_private=True)
    data = {"news": news}
    return render(request, 'Pages/HomePage.html', context=data)

