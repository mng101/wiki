from django import forms

from . import util


class EntryForm(forms.Form):
    entry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': '25',
                                                          'placeholder': 'Wiki Entry'}))

    entry_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15',
                                                              'placeholder': 'Enter the Wiki Page content here'}))



    # def clean_entry(self):
    #     entry = self.cleaned_data.get('entry').capitalize()
    #     entries = util.list_entries()
    #     if entry.casefold() in [x.casefold() for x in entries]:
    #         raise forms.ValidationError("Entry for %s already exists" % entry)
    #     return (entry)

