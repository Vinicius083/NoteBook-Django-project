from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Note, User

def get_notes_from_user(request, user_id):
    notes = Note.objects.filter(user_id=user_id)
    return render(request, 'notes/notes.html', {'notes': notes, 'user_id': user_id})

def add_note(request, user_id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = User.objects.get(id=user_id)

        note = Note( title=title, content=content, user=user)
        note.save()
        return HttpResponseRedirect(reverse('notes:get_notes_from_user', args=[user_id]))
    return render(request, 'notes/add_note.html', {'user_id': user_id})
 

def update_note(request, note_id, user_id):
    note = Note.objects.get(id=note_id, user_id=user_id)

    if request.method == "POST":
        note.title = request.POST.get('title', note.title)
        note.content = request.POST.get('content', note.content)
        note.save()
        return HttpResponseRedirect(reverse('notes:get_notes_from_user', args=[user_id]))
    return render(request, 'notes/update_note.html', {'note': note, 'user_id': user_id})


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('notes:get_notes_from_user', args=[note.user_id]))