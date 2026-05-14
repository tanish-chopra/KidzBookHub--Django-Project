from django.db import models
import os

class Book(models.Model):
    GRADE_CHOICES = [(i, f'Grade {i}') for i in range(1, 6)]
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('marathi', 'Marathi'),
        ('english', 'English'),
        ('history', 'History'),
        ('general', 'General Knowledge')
    ]

    grade = models.IntegerField(choices=GRADE_CHOICES)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/pdfs/')
    cover_image = models.ImageField(upload_to='books/covers/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(default=0)
    allow_online_reading = models.BooleanField(default=True)

    def __str__(self):
        return f'Grade {self.grade} {self.get_subject_display()} - {self.title}'
    
    def filename(self):
        return os.path.basename(self.pdf_file.name)
