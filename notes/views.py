from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, ListView
from mixins import CustomLoginRequiredMixin

from . import forms, models
from .forms import CommentForm
from .models import Note


class NoteCreateView(CustomLoginRequiredMixin, CreateView):
    """ This view will handle the creation of notes, and saving them to the database """

    template_name = "notes/create.html"
    form_class = forms.CreateNoteForm

    def form_valid(self, form, *args, **kwargs):
        user = self.request.user
        note = form.save(commit=False)
        note.writer = user
        note.save()
        return super().form_valid(form, *args, **kwargs)


class NotesListView(ListView):
    """ This view will handle displaying all the notes in the database """

    # model = models.Note
    paginate_by = 10
    template_name = "notes/list.html"

    def get_queryset(self, *args, **kwargs):
        return (
            models.Note.objects.annotate(count=Count("bookmark__id"))
            .order_by("-count")
            .filter(hidden=False, draft=False)
        )
        # return sorted(qs, key=lambda x: random.random())


def note_detail(request, slug):
    """This view will display a note and then all the comments associated
    with it. A form to post a comment on the note will be available only to
    logged in users. On submission, the page will be reloaded with either a
    success or an error message depending on whether the comment was
    posted successfully."""

    note = get_object_or_404(Note, slug=slug)
    comments = models.Comment.objects.filter(note=note, active=True)
    bookmarks = models.Bookmark.objects.filter(note=note).count()
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.note = note
            comment.user = request.user
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Your comment was posted successfully!"
            )
            # reset the form to make sure that the previously filled in data is
            # not re-rendered
            comment_form = CommentForm()
        else:
            messages.add_message(
                request, messages.ERROR, "There was an error, please try again..."
            )
    else:
        comment_form = CommentForm()
    context = {
        "note": note,
        "comments": comments,
        "bookmarks": bookmarks,
        "comment_form": comment_form,
    }
    return render(request, "notes/detail.html", context)


class PrivateListView(ListView):
    """ This view will handle displaying of private notes of the user. """

    paginate_by = 10
    queryset = models.Note.objects.filter(hidden=True).order_by("-updated_at")
    template_name = "notes/private.html"


class PublicListView(ListView):
    """ This view will handle displaying of publicly available notes """

    paginate_by = 10
    queryset = models.Note.objects.filter(hidden=False).order_by("-updated_at")
    template_name = "notes/public.html"


class DraftListView(ListView):
    """ This view will handle displaying draft notes """

    paginate_by = 10
    queryset = models.Note.objects.filter(draft=True).order_by("-updated_at")
    template_name = "notes/drafts.html"


class BookmarkListView(CustomLoginRequiredMixin, ListView):
    """ This view will handle display of bookmarks """

    paginate_by = 10
    template_name = "notes/bookmarks.html"

    def get_queryset(self, *args, **kwargs):
        bookmarks = models.Bookmark.objects.filter(user=self.request.user)
        return [bookmark.note for bookmark in bookmarks]
