# Project 1 - Wiki

Web Programming with Python and JavaScript

Greetings! Welcome to a demonstration of my Project 1.

This project builds a Wikipedia-like online encyclopaedia.

The Index Page displays an unordered list of entries in the encyclopaedia. Each of the list items is a link that
the user can select to be taken directly to the entry page. The side bar contains a search field and a few
links to navigate through the site contents. We will walkthrough each of the links in the side bar in a later
section of the video.

By selecting an item on the list displayed, the visitor will be presented with a page that displays the contents
of the encyclopaedia entry.

The encyclopaedia entry can also be displayed by visiting /wiki/TITLE where TITLE is an encyclopaedia
entry, i.e. /wiki/HTML

If the entry does not exist i.e. /wiki/ABC, the visitor is presented with an error page indicating the requested
entry was not found.

The wiki site incorporates a search function to allow a visitor to search for an encyclopaedia entry.

If the query matches a single encyclopaedia entry i.e. HTML, the entry page is displayed. The query string is
not case sensitive.

If the query string matches the substring of more than one encyclopaedia entries, all the matching entries
are displayed. For example, the query string “o” will find the 3 entries listed. Selecting an item in the list
takes the visitor to the encyclopaedia page for that entry.

When an encyclopaedia entry is displayed, the side bar has an additional link “Edit this page” the visitor can
select to edit the page displayed. Only the Entry text can be edited. The Entry title is flagged as ‘read-only’.

Entry text uses the markup language Markdown to make the entries more human-friendly to write an edit.
Notice the Markdown syntax for the links (Python and HTML) on this page. 

Clicking on the “Submit” button saves the Entry page to disk, and displays the updated page. Markdown text
is converted into HTML before the page is displayed. (Notice that Python and HTML now appear as links on
the page).

Clicking “Random Page” in the sidebar displays a random encyclopaedia entry.

Thank you for your time.


