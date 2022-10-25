from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from datetime import datetime
from main.date_converter import DateConverter

def sort_and_unique_lib():
    to_dict = dict.fromkeys(LIB_DATE)
    to_list = list(to_dict.keys())
    to_list.sort()
    return to_list

LIB = Book.objects.all()
LIB_DATE = [book.pub_date.strftime('%Y-%m-%d') for book in LIB]
LIB_DATE_U_SORTED = sort_and_unique_lib()

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)
#
def show_book_view(request, pub_date):
    template = 'books/show_book.html'

    books = Book.objects.filter(pub_date=pub_date)

    date_str = pub_date.strftime('%Y-%m-%d')
    date_index = LIB_DATE_U_SORTED.index(date_str)
    previous_date = None
    next_date = None
    datetime.strptime(date_str, '%Y-%m-%d').date()
    if date_index > 0:
        previous_date_str = LIB_DATE_U_SORTED[date_index - 1]
        previous_date = datetime.strptime(previous_date_str, '%Y-%m-%d').date()
    if date_index < len(LIB_DATE_U_SORTED) - 2:
        next_date_str = LIB_DATE_U_SORTED[date_index + 1]
        next_date = datetime.strptime(next_date_str, '%Y-%m-%d').date()

    page_number = request.GET.get('page', date_str)
    paginator = Paginator(LIB_DATE_U_SORTED, 1)
    page = paginator.get_page(page_number)

    context = {
        'books': books,
        'page': page,
        'next': next_date,
        'previous': previous_date,
    }
    return render(request, template, context)

