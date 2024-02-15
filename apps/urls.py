from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from apps.forms import UserForm
from apps.models import User


class UserListView(ListView):
    template_name = 'apps/user_list.html'
    paginate_by = 3
    queryset = User.objects.order_by('-id')
    context_object_name = 'users'


class UserDeleteView(DeleteView):
    model = User
    pk_url_kwarg = 'pk'
    form = UserForm
    template_name = 'apps/user_list.html'
    success_url = reverse_lazy('user_list_page')

    def get(self, request, pk):
        User.objects.filter(id=pk).delete()
        return redirect('user_list_page')
