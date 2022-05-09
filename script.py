import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)