from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

from . import util
from . import forms

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def showentry(request, entry):
    entry_text = util.get_entry(entry)

    if entry_text is None:
        wiki_page = "<h2>" + entry + " : Entry not found</h2>"
        page_edit_menu = ""
    else:
        wiki_page = markdown2.markdown(util.get_entry(entry))
#        page_edit_menu = '<br><a href="' + reverse(updateform) + entry + '">Edit this page</a>'

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "wiki_page": wiki_page,
#        "page_edit_menu": page_edit_menu
    })


def entryform(request):
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
        form = forms.EntryForm()
        return render(request, "encyclopedia/entryform.html", {
            'form': form
        })