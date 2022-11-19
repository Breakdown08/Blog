from ..utils import *


def about(request):
    data = {"somekey": None}
    return render(request, 'Pages/AboutPage.html', context=data)