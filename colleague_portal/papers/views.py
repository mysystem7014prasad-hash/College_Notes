from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Note, PreviousPaper

def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.downloads += 1
    note.save()
    return redirect(note.file.url)

def download_previous_paper(request, paper_id):
    paper = get_object_or_404(PreviousPaper, id=paper_id)
    paper.downloads += 1
    paper.save()
    return redirect(paper.file.url)

for paper in papers_qs:
    combined.append({
        'type': 'paper',
        'id': paper.id,
        'title': paper.title,
        'file_url': paper.filurl,   # <-- this must exist!
        'download_url': reverse('download_previous_paper', args=[paper.id]),  # <-- this too!
        'category_display': 'Previous Paper',
        'uploaded_at': paper.uploaded_at,
        'downloads': paper.downloads,
    })