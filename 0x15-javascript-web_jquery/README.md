# JavaScript Web JQuery

This repository contains JavaScript scripts for various tasks related to JQuery and DOM manipulation. Below is an explanation of each task:

## Task 0: No JQuery

In this task, a JavaScript script named `0-script.js` is written to update the text color of the `<header>` element to red (#FF0000) without using JQuery. The script uses `document.querySelector` to select the HTML tag and modifies its style to change the text color.

## Task 1: With JQuery

In this task, a JavaScript script named `1-script.js` is written to update the text color of the `<header>` element to red (#FF0000) using the JQuery API. The script uses the JQuery selector to select the HTML tag and modifies its style to change the text color.

## Task 2: Click and turn red

This task involves writing a JavaScript script named `2-script.js` that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag `DIV#red_header`. The script uses the JQuery API to add a click event handler to the `DIV#red_header` element, and upon clicking, it modifies the style of the `<header>` to change the text color.

## Task 3: Add `.red` class

In this task, a JavaScript script named `3-script.js` is written to add the class "red" to the `<header>` element when the user clicks on the tag `DIV#red_header`. The script uses the JQuery API to add a click event handler to the `DIV#red_header` element, and upon clicking, it adds the class "red" to the `<header>` element, thereby updating its style to change the text color.

## Task 4: Toggle classes

This task involves writing a JavaScript script named `4-script.js` that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`. The `<header>` element must always have one class: "red" or "green," never both at the same time and never empty. The script uses the JQuery API to add a click event handler to the `DIV#toggle_header` element, and upon clicking, it toggles the class of the `<header>` between "red" and "green" accordingly.

## Task 5: List of elements

In this task, a JavaScript script named `5-script.js` is written to add an `<li>` element to a list when the user clicks on the tag `DIV#add_item`. The new element must be: `<li>Item</li>`, and it must be added to the `<ul class="my_list">` element. The script uses the JQuery API to add a click event handler to the `DIV#add_item` element, and upon clicking, it appends the new `<li>` element to the `<ul class="my_list">`.

## Task 6: Change the text

This task involves writing a JavaScript script named `6-script.js` that updates the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`. The script uses the JQuery API to add a click event handler to the `DIV#update_header` element, and upon clicking, it updates the text content of the `<header>` element to "New Header!!!".

## Task 7: Star wars character

In this task, a JavaScript script named `7-script.js` is written to fetch the character name from the URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`. The fetched name is displayed in the HTML tag `DIV#character`. The script uses the JQuery API to perform the API request and display the character name in the specified tag.

## Task 8: Star wars movies

This task involves writing a JavaScript script named `8-script.js` that fetches and lists the title for all movies from the URL: `https://swapi-api.alx-tools.com/api/films/?format=json`. All movie titles are listed in the HTML tag `UL#list_movies`. The script uses the JQuery API to perform the API request and display the movie titles in the specified list.

## Task 9: Say Hello!

In this task, a JavaScript script named `9-script.js` is written to fetch the value of "hello" from the URL `https://fourtonfish.com/hellosalut/?lang=fr` and display the translation of "hello" in the HTML tag `DIV#hello`. The script uses the JQuery API to perform the API request and display the translated "hello" in the specified tag.

Please note that all scripts should be tested with the corresponding HTML files mentioned in the task descriptions to ensure their functionality in the browser.

## Task 10: No jQuery - document loaded

In this advanced task, a JavaScript script named `100-script.js` is written to update the text color of the `<header>` element to red (#FF0000) using `document.querySelector` without using the JQuery API. The script is imported from the `<head>` tag and modifies the style of the `<header>` element upon document load.

## Task 11: List, add, remove

In this advanced task, a JavaScript script named `101-script.js` is written to add, remove, and clear `<li>` elements from a list when the user clicks on specific elements. The script uses the JQuery API to add click event handlers to `DIV#add_item`, `DIV#remove_item`, and `DIV#clear_list`, and upon clicking, it adds, removes, or clears `<li>` elements from the list accordingly.

## Task 12: Say hello to everybody!

This advanced task involves writing a JavaScript script named `102-script.js` that fetches and prints how to say "Hello" depending on the language. The script uses the JQuery API to fetch the translation from `https://www.fourtonfish.com/hellosalut/hello/` based on the language code entered in `INPUT#language_code`, and the translation of "Hello" is displayed in the HTML tag `DIV#hello` upon clicking `INPUT#btn_translate`.

## Task 13: And press ENTER

In this advanced task, a JavaScript script named `103-script.js` is written to fetch and print how to say "Hello" depending on the language. The script uses the JQuery API to fetch the translation from `https://www.fourtonfish.com/hellosalut/hello/` based on the language code entered in `INPUT#language_code`, and the translation of "Hello" is displayed in the HTML tag `DIV#hello` upon clicking `INPUT#btn_translate` or pressing ENTER when the focus is on `INPUT#language_code`.