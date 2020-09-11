# Project 1 - Wiki

Web Programming with Python and JavaScript

00:00:00 --> 00:00:06
Greetings! Welcome to a demonstration of Project 1.
Project 1 builds a Wikipedia-like online encyclopaedia.

00:00:06 --> 00:00:24
The Index Page displays an unordered list of entries in the encyclopaedia. Each of the list items is a link that the user can select to be taken directly to the entry page. The side bar contains a search field and a few links to navigate through the site contents.

00:00:24 --> 00:00:53
Selecting CSS, displays a page with the contents of the CSS entry.
The encyclopaedia entry can also be displayed by navigating directly to the entry page i.e. /wiki/HTML
If the entry does not exist i.e. /wiki/ABC, the visitor is presented with an error page indicating the requested entry was not found.

00:00:53 --> 00:00:59
Selecting “Home” in the sidebar brings the visitor to the index page.

00:00:59 --> 00:01:17
The site incorporates a search function to allow a visitor to search through the encyclopaedia entries.
If the query matches a single entry i.e. Git, the page for that entry is displayed. The query string is not case sensitive.

00:01:17 --> 00:01:42
If the query string matches the substring of more than one entry, all the matching entries are displayed as an unordered list. For example, the query string “o” will find the 3 entries listed. Selecting an item in the list takes the visitor to the page for that entry i.e. Django.

00:01:42 --> 00:02:01
When an entry page is displayed, the side bar has an additional link “Edit this page” the visitor can select to edit the page displayed. Only the Entry text can be edited. The Entry title is flagged as ‘read-only’.

00:02:01 --> 00:02:12
Entry text uses the markup language Markdown to make the entries more human-friendly to write and edit. Notice the Markdown syntax for the text “Python” and “HTML”.

00:02:12 --> 00:02:29
Clicking on the “Submit” button saves the Entry page to disk, and displays the updated page. Markdown text is converted into HTML before the page is displayed. (Notice that Python and HTML now appear as links on the page)

00:02:29 --> 00:03:07
“Create New Page” displays a form the visitor can fill in to create a new encyclopaedia entry. For example, we can create a sample entry “ABC” with dummy text. Submitting the form saves the entry to the disk and displays the entry page. Notice the word “sample” is formatted in bold text as a result of the Markdown to HTML conversion.

00:03:07 --> 00:03:37
When the New Page form is submitted, there is a check for duplicate entries. For example, if we try to create a new page with the same title as an existing page “HTML”, an error message is displayed and the update to disk is aborted.

00:03:37 --> 00:03:52
Clicking “Random Page” in the sidebar displays a random encyclopaedia entry.  


Link to Video posted on Youtube

https://www.youtube.com/watch?v=EIAl7sRxBTA
