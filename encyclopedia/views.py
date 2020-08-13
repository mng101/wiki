from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

from . import util
from . import forms

import markdown2
import random


def index(request):
    querystring = request.GET.get('q')

    if querystring is None:
        # This is a request for the Index Page
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        # This is a search for entries containing the query string
        entries = util.list_entries()
        match = []
        for entry in entries:
            if querystring.casefold() in entry.casefold():
                match.append(entry)

        return render(request, "encyclopedia/index.html",
            dict(entries = match)
        )



def showentry(request, entry):
    entry_text = util.get_entry(entry)

    if entry_text is None:
        wiki_page = "<h2>" + entry + " : Entry not found</h2>"
        page_edit_menu = ""
    else:
        wiki_page = markdown2.markdown(util.get_entry(entry))
        page_edit_menu = '<br><a href="' + reverse(entryform) + entry + '">Edit this page</a>'

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "wiki_page": wiki_page,
        "page_edit_menu": page_edit_menu
    })


def entryform(request, entry=""):
    if request.method == "POST":
        form = forms.EntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"]
            entry_text = form.cleaned_data["entry_text"]
            entry_text = "# " + entry + "\n" + entry_text
            util.save_entry(entry, entry_text)
            return HttpResponseRedirect(reverse("showentry", args=[entry]))
        else:
            return render(request, "encyclopedia/entryform.html", {
                'form': form
            })
    else:
        if len(entry) == 0:             # Creating a new Page
            form = forms.EntryForm()
        else:                           # Updating an existing Page
            entry_text = util.get_entry(entry).split("\n", 1)[1]
            form = forms.EntryForm(initial={"entry":entry, "entry_text":entry_text})
            form.fields["entry"].widget.attrs['readonly'] = True

        return render(request, "encyclopedia/entryform.html", {
            'form': form
        })

def randompage(request):
    entry = random.choice(util.list_entries())
    return showentry(request, entry)
