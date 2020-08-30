from django import forms

from . import util


class EntryForm(forms.Form):
    entry = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': '25',
                                                          'placeholder': 'Wiki Entry'}))

    entry_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15',
                                                              'placeholder': 'Enter the Wiki Page content here'}))

    # A hidden field to identify if the page being posted is a New Entry or an Update to an existing Entry
    newentryflag = forms.BooleanField(required=False,
                                      widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        entry = self.cleaned_data.get('entry')
        newentryflag = self.cleaned_data.get('newentryflag')

        # Validate for duplicate Entries only if the 'newentryflag' is True
        if newentryflag == True:
            entries = util.list_entries()
            if entry.casefold() in [x.casefold() for x in entries]:
                raise forms.ValidationError("Entry for %s already exists" % entry)
        # return (entry)