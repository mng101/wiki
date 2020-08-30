from django.shortcuts import render, redirect
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

        if len(match) == 0:
            # No matching entry found. Display the index page
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
        elif len(match) == 1:
        # Only one Wiki entry returned by the search, display the Wiki entry
            return HttpResponseRedirect(reverse("showentry", args=[match[0]]))
        else:
            # Search returned multiple Wiki entries
            return render(request, "encyclopedia/index.html",
                dict(entries = match)
        )


def showentry(request, entry):
    entry_text = util.get_entry(entry)

    if entry_text is None:
        wiki_page = "<h2>" + entry + "</h2><br> Requested Page not found"
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
        # if len(entry) == 0:
        #     newPage = True          # We will use this flag to decide if we check for duplicates
        form = forms.EntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"]
            entry_text = form.cleaned_data["entry_text"]
            # if newPage == True:
            #     # If this is a "Create New Page" function, check if the 'entry' exists
            #     entries = util.list_entries()
            #     if entry.casefold() in [x.casefold() for x in entries]:
            #         raise forms.ValidationError("Entry for %s already exists" % entry)
            entry_text = "# " + entry + "\n" + entry_text
            util.save_entry(entry, entry_text)
            return HttpResponseRedirect(reverse("showentry", args=[entry]))
        else:
            return render(request, "encyclopedia/entryform.html", {
                'form': form
            })
    else:
        if len(entry) == 0:             # Creating a new Page
            form = forms.EntryForm(initial={"newentryflag":True})
            # newPageFlag = True
        else:                           # Updating an existing Page
            entry_text = util.get_entry(entry).split("\n", 1)[1]
            form = forms.EntryForm(initial={"entry":entry, "entry_text":entry_text, "newentryflag":False})
            form.fields["entry"].widget.attrs['readonly'] = True

        return render(request, "encyclopedia/entryform.html", {
            'form': form
        })

def randompage(request):
    entry = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("showentry", args=[entry]))


