# Survey

At right is the start of a web application that (for now) just displays a blank form. Your goal will be to complete the web app in such a way that it enables a user to

* fill out a form, a la Google Forms, the results of which are saved to a comma-separated-value (CSV) file on the server, and
* view a table of all of the submissions received, a la Google Sheets.

{% video https://www.youtube.com/watch?v=0zIpv_dbaSQ %}

{% next %}

## Understanding

### `application.py`

This file represents your web app's "controller," all of the logic that implements its functionality. Atop the file are a few imports of libraries followed by some configuration of Flask, per the comments therein. Below that are declarations of four routes, two of which are for you to do!

### `templates/layout.html`

This file represents your web app's layout, an HTML structure that all of your views will share.


### `templates/form.html`

In this file will live your very own form, only the skeleton of which we've written for you.

### `templates/error.html`

In this file is a template for any messages you might like to display to the user in the event of some error.

### `static/styles.css`

In this file will be any of your own CSS properties for any or all of your app's views.

{% next %}

## Specification

Complete the implementation of `templates/form.html` in such a way that the form therein contains not only a button but also

* one or more text fields of any type,
* one or more checkboxes or two or more radio buttons,
* one or more select menus, each with two or more options, and
* zero or more other inputs of any type.

Style that form using [Bootstrap](http://getbootstrap.com/docs/4.1/components/forms/) so that it looks nicer than it would with raw HTML alone.

Add to that file some JavaScript code that prevents users from submitting the form if they have not provided values for one or more fields, alerting the user accordingly, as via [`alert`](https://www.w3schools.com/jsref/met_win_alert.asp) or [Bootstrap](http://getbootstrap.com/docs/4.1/components/forms/#validation).

Complete the implementation of `post_form` in such a way that it

* validates a form's submission, alerting users with a `message` via `error.html` if they have not provided values for one or more fields, just in case your JavaScript code let something through (or was disabled),
* writes the form's values to a new row in `survey.csv` using `csv.writer` or `csv.DictWriter`, and
* redirects the user to `/sheet`.

Complete the implementation of `get_sheet` in such a way that it

* reads past submissions from `survey.csv` using `csv.reader` or `csv.DictReader` and
* displays those submissions in an HTML `table` via a new template.

Style that table using [Bootstrap](http://getbootstrap.com/docs/4.1/content/tables/) so that it looks nicer than it would with raw HTML alone.

Optionally enhance the table with JavaScript, as via [DataTables](https://datatables.net/examples/styling/bootstrap4).

Provided you meet these specifications, you're welcome to alter the aesthetics of your app however you'd like, as via [Bootstrap](http://getbootstrap.com/docs/4.1/) or your own CSS and HTML.

## References

* [Bootstrap](http://getbootstrap.com/docs/4.1/)
** [Forms](https://getbootstrap.com/docs/4.1/components/forms/)
** [Tables](https://getbootstrap.com/docs/4.1/content/tables/)
* [`csv`](https://docs.python.org/3/library/csv.html)
** [`csv.writer`](https://docs.python.org/3/library/csv.html#csv.writer)
** [`csv.DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter)
* [DataTables](https://datatables.net/examples/styling/bootstrap4)
** [Options](https://datatables.net/reference/option/)
* [HTML Forms](https://www.w3schools.com/html/html_forms.asp)
** [HTML Form Elements](https://www.w3schools.com/html/html_form_elements.asp)
** [HTML Input Types](https://www.w3schools.com/html/html_form_input_types.asp)
** [HTML Input Attributes](https://www.w3schools.com/html/html_form_attributes.asp)

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/survey
```

## Understanding
