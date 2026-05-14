from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, HttpResponseForbidden
from django.db.models import F
from django.urls import reverse
from .models import Book

def course_list(request):
    books = Book.objects.all()
    
    # Filter by grade
    grade = request.GET.get('grade')
    if grade and grade.isdigit():
        books = books.filter(grade=int(grade))
    
    # Filter by subject
    subject = request.GET.get('subject')
    if subject:
        books = books.filter(subject=subject)
    
    return render(request, 'courses/course_list.html', {
        'books': books,
        'current_grade': grade,
        'current_subject': subject
    })

def course_detail(request, course_id):
    book = get_object_or_404(Book, id=course_id)
    return render(request, 'courses/course_detail.html', {'book': book})

def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Increment download count
    Book.objects.filter(id=book_id).update(downloads=F('downloads') + 1)
    # Return the PDF file
    return FileResponse(book.pdf_file, as_attachment=True, filename=book.filename())

def read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.allow_online_reading:
        return HttpResponseForbidden("This book is not available for online reading.")
    
    # Serve the PDF file directly
    try:
        response = FileResponse(book.pdf_file.open('rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{book.filename()}"'
        return response
    except Exception as e:
        return HttpResponseForbidden("Error accessing the PDF file.")
