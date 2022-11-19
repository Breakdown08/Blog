from ..utils import *


class NewDetail(ObjectDetailMixin, View):
    model = New
    template = 'Pages/NewDetail.html'