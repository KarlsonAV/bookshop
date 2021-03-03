from django.forms import ModelForm, TextInput
from .models import Book, Review


class CreateProductForm(ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'price', 'cover', )


class CreateReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('review', )
        widgets = {
            "review": TextInput(attrs={
                'class': 'form-control'
            })
        }