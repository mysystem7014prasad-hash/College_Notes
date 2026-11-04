from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('semester/<int:sem>/', views.semester_view, name='semester'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('download/<int:note_id>/', views.download_note, name='download_note'),
    path('download-paper/<int:paper_id>/',views.download_previous_paper,name='download_previous_paper'),
    path('view/<int:note_id>/', views.view_note, name='view_note'),
    path('view-paper/<int:paper_id>/', views.view_previous_paper, name='view_previous_paper'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)