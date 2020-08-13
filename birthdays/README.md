# Birthdays

Create a webpage that keeps track of friends' birthdays.

## Implementation Details

Build a webpage that keeps track of friends' birthdays in a database and displays the birthdays by implementing `application.py`, `index.html`, and `styles.css` at right.

* Note that the database `birthdays.db` has been linked to `application.py`. Check out the structure of this database – there's a `name` column of data type `varchar(255)`, a `month` and a `day` column of data type `smallint`. 

* Complete `application.py` such that via `POST`, users can add birthdays to a database, and via `GET`, users can view a table of birthdays stored in the database. 

* Complete `index.html` such that the user can input a name, a month, and a day to add a birthday to the database. Additionally, display a table of names and dates that are currently in the database. Sort the dates by the `month` column. If there are ties, sort by the `day` column. 
  
* Notice that some CSS has already been included for you in `styles.css`, and this file has already been linked to `index.html`. Feel free to change `styles.css` how you'd like!
  
### Hints

* Recall that when a user inputs information into a form, this information should be `posted` upon submission. 
  
* In `application.py`, we can obtain the information posted by the user via `request.form.get("args")` where `args` is the `name` attribute of the `input` in `index.html`.
  * For example, if in `index.html`, we have `<input name="value" type="text"></input>`, we can write `request.form.get("value")` in `application.py` to extract the user's input.

* Recall that we can use `db.execute()` to execute SQL queries within `application.py`. 

* You may find it helpful to pass in additional argument(s) to `render_template()` to display the birthdays in the database.

### How to Test Your Code

You should see your webpage upon running the following in the terminal window: 

```
$ flask-run
```


{% next %}

## How to Submit

TODO
