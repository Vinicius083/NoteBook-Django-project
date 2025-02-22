from django.urls import path
from .views import get_notes_from_user, add_note, update_note, delete_note

app_name = 'notes'

urlpatterns = [
    path('<int:user_id>/', get_notes_from_user, name='get_notes_from_user'),
    path('<int:user_id>/add_note/', add_note, name='add_note'),
    path('<int:note_id>/user/<int:user_id>/update/', update_note, name='update_note'),
    path('<int:note_id>/delete/', delete_note, name='delete_note'),
]