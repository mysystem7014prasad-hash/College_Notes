import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colleague_portal.settings')
django.setup()

from notes.models import Note

def fix():
    notes = Note.objects.all()
    count = 0
    
    for note in notes:
        old_path = note.file.path
        old_name = note.file.name
        
        # Check if the file actually exists
        if not os.path.exists(old_path):
            print(f"❌ File missing: {old_path}")
            continue
        
        # Just update the database path to match the actual file name
        # (Keep spaces as they are)
        new_name = old_name.replace(' ', ' ')  # Does nothing - keeps spaces
        
        if old_name == new_name:
            continue
        
        note.file.name = new_name
        note.save()
        count += 1
        print(f"✅ Updated DB: {old_name} → {new_name}")
    
    print(f"\n🎉 Done! Updated {count} files in database.")

if __name__ == "__main__":
    fix()