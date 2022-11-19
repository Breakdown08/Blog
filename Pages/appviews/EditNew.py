from django.views.generic import UpdateView
from ..models import New


class UpdateNewView(UpdateView):
    model = New
    template_name = 'Pages/NewEdit.html'
    fields = [
        'title',
        'short_description',
        'content',
        'image_original',
        'is_private'
    ]