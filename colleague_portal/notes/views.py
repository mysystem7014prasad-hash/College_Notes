from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.db.models import Q
from .models import Subject, Note, PreviousPaper
from django.urls import reverse


# ===== HOMEPAGE =====
def home(request):
    return render(request, 'home.html')

# ===== SEMESTER PAGE =====
def semester_view(request, sem):
    subjects = Subject.objects.filter(semester=sem)
    return render(request, 'semester.html', {
        'subjects': subjects,
        'semester': sem
    })

# ===== SUBJECT DETAIL PAGE =====
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    category = request.GET.get('category')
    
    # Base querysets (all for this subject)
    notes_qs = Note.objects.filter(subject=subject)
    papers_qs = PreviousPaper.objects.filter(subject=subject)
    
    # Apply filters based on category
    if category == 'previous_paper':
        # Show ONLY previous papers
        notes_qs = Note.objects.none()
        # papers_qs stays as all previous papers
    
    elif category == 'notes':
        # Show ONLY notes (category='notes')
        notes_qs = notes_qs.filter(category='notes')
        papers_qs = PreviousPaper.objects.none()
    
    elif category == 'syllabus':
        # Show ONLY syllabus notes (category='syllabus')
        notes_qs = notes_qs.filter(category='syllabus')
        papers_qs = PreviousPaper.objects.none()
    
    # else: category is None (All) -> show both notes and papers (no filtering)
    
    # Combine into list with type info
    combined = []
    
    for note in notes_qs:
        combined.append({
            'type': 'note',
            'id': note.id,
            'title': note.title,
            'category_display': note.get_category_display(),
            'uploaded_at': note.uploaded_at,
            'downloads': note.downloads,
            'download_url': reverse('download_note', args=[note.id]),
            'file_url': reverse('view_note', args=[note.id]),
        })
    
    for paper in papers_qs:
        combined.append({
            'type': 'paper',
            'id': paper.id,
            'title': paper.title,
            'file_url': reverse('view_previous_paper', args=[paper.id]),
            'download_url': reverse('download_previous_paper',args=[paper.id]),
            'category_display': 'Previous Paper',
            'uploaded_at': paper.uploaded_at,
            'downloads': paper.downloads,
        })
    
    # Sort by date (newest first)
    combined.sort(key=lambda x: x['uploaded_at'] or '', reverse=True)
    
    return render(request, 'subject_detail.html', {
        'subject': subject,
        'notes': combined,
        'category': category,
    })

# ===== DOWNLOAD FUNCTION =====
def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.downloads += 1
    note.save()
    return FileResponse(note.file.open('rb'), as_attachment=True)

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    response = FileResponse(note.file.open('rb'))
    response['Content-Disposition'] = f'inline; filename="{note.file.name.rsplit("/", 1)[-1]}"'
    return response

def view_previous_paper(request, paper_id):
    paper = get_object_or_404(PreviousPaper, id=paper_id)
    response = FileResponse(paper.file.open('rb'))
    response['Content-Disposition'] = f'inline; filename="{paper.file.name.rsplit("/", 1)[-1]}"'
    return response

from django.shortcuts import get_object_or_404, redirect
from .models import PreviousPaper

def download_previous_paper(request, paper_id):
    paper = get_object_or_404(PreviousPaper, id=paper_id)
    paper.downloads += 1
    paper.save()
    return redirect(paper.file.url)
