from django.urls import reverse

from ..models import New
from ..forms import CreateNewForm
from django.views.generic import CreateView


class CreateNewView(CreateView):
    model = New
    form_class = CreateNewForm
    template_name = 'Pages/NewAdd.html'

    # fields = [
    #     'title',
    #     'short-description',
    #     'content',
    #     'image_original',
    #     'is_private'
    # ]

    def form_valid(self, form):
        print("!!!")
        form.instance.author = self.request.user
        # form.instance.post_date = datetime.now()
        form.save()
        return super(CreateNewView, self).form_valid(form)

    def get_success_url(self):
        return reverse ('new_detail_url', kwargs={'slug': self.object.slug})