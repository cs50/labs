# Frosh IMs

At right is a web app via which first-year students at Harvard could potentially register for Freshman Intramural Sports, otherwise known as Frosh IMs. Go ahead and run

```
flask run
```

and experiment with the app to see what it does. Try to register a few students. Then read through

1. `application.py`,
1. `registrants.csv`,
1. `templates/layout.html`,
1. `templates/index.html`,
1. `templates/failure.html`,
1. `templates/success.html`,

in that order, to understand how the app works.

{% next %}

Enhance and personalize this app in, at least, the following ways:

* Alter the colors and/or layout of the app's navigation bar and/or form using Bootstrap.
* Require that students provide, when registering, at least two values besides their email address and name; store those values in `registrants.csv` as well.
* Display registrants using a [table](https://getbootstrap.com/docs/4.3/content/tables/) instead of an unordered list, the design of which is up to you.
* Require that a student input an actual email address, not just text. You're welcome to use a Python library for such, or you might want to read up on Python's support for "regular expressions."

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/froshims
```
