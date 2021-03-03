from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Book
from django.db.models import Q

from .forms import CreateProductForm, CreateReviewForm


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateReviewForm
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        if book.title in self.request.user.paid_books:
            context['Paid'] = True
        else:
            context['Paid'] = False
        return context

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            new_form = CreateReviewForm(data=self.request.POST)
            review = new_form.save(commit=False)
            review.book = get_object_or_404(Book, id=kwargs['pk'])
            review.author = self.request.user
            review.save()
            return HttpResponseRedirect(self.request.path_info)
        return HttpResponseRedirect(reverse('account_login'))


class CreateProductView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'books/create_product.html'
    form_class = CreateProductForm
    login_url = 'account_login'
    permission_required = 'books.special_status'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('books.special_status'):
            return HttpResponseRedirect(reverse('book_list'))
        return super().dispatch(request, *args, **kwargs)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))