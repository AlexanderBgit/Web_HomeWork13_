from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage

from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from .models import Author, Tag
from .models import Quote

from .utils import get_mongodb
from .templatetags.extract import get_author_and_quotes

import logging
logger = logging.getLogger(__name__)


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user  # Встановлення користувача
            author.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


def about(request, author_id):
    author, quotes = get_author_and_quotes(author_id)

    if author is None:
        return render(request, 'quotes/author_not_found.html', {'author_id': author_id})

    context = {
        'author_id': author_id,
        'quotes': quotes,
        'author': author,
    }
    logger.info("Rendering page for author: %s", author['fullname'])
    return render(request, 'quotes/author.html', context)



def author_detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        quotes = Quote.objects.filter(author=author)
        return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})
    except Author.DoesNotExist:
        return render(request, 'quotes/author_not_found.html', {'author_id': author_id})


@login_required
def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes:root')

        else:
            return render(request, 'quotes/add_quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotes/add_quote.html', {"tags": tags, 'form': QuoteForm()})
