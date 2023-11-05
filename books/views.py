from django.shortcuts import render,HttpResponse
from .forms import UploadCSVForm,BookSearchForm
from .models import Book
# Create your views here.

def Home(request):
    return render(request,'books/Home.html')
def category(request):
    return render(request,'books/Category.html')
def horror(request):
    return render(request,'books/Horror.html')
def Sci_fi(request):
    return render(request,'books/Sci-fi.html')
def fantasy(request):
    return render(request,'books/Fantasy.html')
def mystery(request):
    return render(request,'books/Mystery.html')
def dsytopia(request):
    return render(request,'books/Dsytopian.html')
def philosphy(request):
    return render(request,'books/philosophy.html')
def education(request):
    return render(request,'books/educational.html')
def young_adult(request):
    return render(request,'books/young_adult.html')
def about(request):
    return render(request,'books/about.html')
def BHome(request):
    return render(request,'books/BHome.html')
def manga(request):
    return render(request,'books/Manga.html')
def classics(request):
    return render(request,'books/classics.html')
def cookbook(request):
    return render(request,'books/cookbook.html')

from .models import Book

# views.py
from django.shortcuts import render
from .models import Book

# views.py
from django.shortcuts import render
from .models import Book

# views.py
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_search(request):
    form = BookSearchForm()
    results = []

    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                query = query.lower()  # Convert the query to lowercase for case-insensitive search
                all_books = Book.objects.all()
                results = [book for book in all_books if query in book.btitle.lower()]

    return render(request, 'books/search_results.html', {'form': form, 'results': results})


#for searching

# views.py
import csv
 # Replace with the actual model you want to populate

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_data = csv.reader(decoded_file)
            next(csv_data, None)  # Skip the header row if present

            for row in csv_data:
                _, created = Book.objects.get_or_create(
                    bid=row[0],
                    btitle=row[1],
                    author=row[2],
                    bcopies=row[4],
                    # Add fields for each column in your CSV
                )

            return HttpResponse('<h1>Book uploaded</h1>')  # Redirect to a success page or another URL

    else:
        form = UploadCSVForm()

    return render(request, 'books/upload_csv.html', {'form': form})

