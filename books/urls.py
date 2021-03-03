from django.urls import path

from .views import BookListView, BookDetailView, CreateProductView, SearchResultsListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add_product/', CreateProductView.as_view(), name='create_product'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]