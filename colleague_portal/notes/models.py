from django.db import models
from django.contrib.auth.models import User


class PreviousPaper(models.Model):
    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
    ]

    CATEGORY_CHOICES = [
        ('previous_paper', 'Previous Paper'),
    ]

    title = models.CharField(max_length=200)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)  # <-- Changed from CharField to ForeignKey
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default='1')
    year = models.IntegerField()
    file = models.FileField(upload_to='previous_papers/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    downloads = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='previous_paper')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title



    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"

CATEGORY_CHOICES = [
    ('notes', 'Notes'),
    ('syllabus', 'Syllabus'),
    ('previous_paper', 'Previous Paper'),
]

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    downloads = models.IntegerField(default=0)
    category = models.CharField(max_length=50)  # <-- missing choices!
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    # ➕ ADD THIS LINE:
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='notes')

    def __str__(self):
        return self.title
    
    
