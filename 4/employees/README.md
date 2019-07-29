# Employees

Consider (again) this [table of employees](https://docs.google.com/spreadsheets/d/1kEOrpIhASIVKtl1ClDRqOotj7u4aWc07VOYZvAsShp0/edit#gid=1496860225), a copy of which, `employees.csv`, can be found in the text editor at top-right.

In `employees.py` in the text editor at top-right, implement a program that whittles `employees.csv` down to just three fields by:

1. opening `employees.csv` for reading,
1. printing, verbatim, `Manager,LastName,FirstName`, on a line of its own, and
1. printing, for each employee in `employees.csv`, on a line of its own, the employee's manager, followed by a comma, the employee's last name, followed by a comma, and the employee's first name.

Your program should thus output:

```
Manager,LastName,FirstName
,Adams,Andrew
Michael Mitchell,Callahan,Laura
Andrew Adams,Edwards,Nancy
Nancy Edwards,Johnson,Steve
Michael Mitchell,King,Robert
Andrew Adams,Mitchell,Michael
Nancy Edwards,Park,Margaret
Nancy Edwards,Peacock,Jane
```

Notice the leading comma for Andrew Adams, who doesn't have a manager.

Each name that you print should be extracted from `employees.csv`; no names should be hard-coded into your program.

{% next %}

Let's now assign each employee a unique identifier, an integer starting at `1` that's incremented for each employee in `employees.csv`, from top to bottom.

Modify `employees.py` in the text editor at top-right in such a way that the program

1. outputs, verbatim, `Id,Manager,LastName,FirstName`, on a line of its own, and
1. outputs, for each employee, on a line of its own, a unique identifier for the employee, followed by a comma, followed by the employee's manager, followed by a comma, followed by the employee's last name, followed by a comma, followed by the employee's first name.

Your program should thus output:

```
Id,Manager,LastName,FirstName
1,,Adams,Andrew
2,Michael Mitchell,Callahan,Laura
3,Andrew Adams,Edwards,Nancy
4,Nancy Edwards,Johnson,Steve
5,Michael Mitchell,King,Robert
6,Andrew Adams,Mitchell,Michael
7,Nancy Edwards,Park,Margaret
8,Nancy Edwards,Peacock,Jane
```

Notice the pair of adjacent commas for Andrew Adams, who doesn't have a manager.

Each name that you print should again be extracted from `employees.csv`; no names should be hard-coded into your program.

{% next %}

Let's now eliminate the redundancy of storing managers' names and instead associate with each employee the unique identifier of his or her manager.

Modify `employees.py` in the text editor at top-right in such a way that the program

1. outputs, verbatim, `Id,ManagerId,LastName,FirstName`, instead of `Id,Manager,LastName,FirstName`, on a line of its own, and
1. outputs, for each employee in `employees.csv`, the unique identifier of the employee, followed by a comma, the unique identifier of the employee's manager, followed by a comma, the employee's last name, followed by a comma, and the employee's first name.

Your program should thus output:

```
Id,ManagerId,LastName,FirstName
1,,Adams,Andrew
2,6,Callahan,Laura
3,1,Edwards,Nancy
4,3,Johnson,Steve
5,6,King,Robert
6,1,Mitchell,Michael
7,3,Park,Margaret
8,3,Peacock,Jane
```

Notice the pair of adjacent commas for Andrew Adams, who doesn't have a manager.

Each name that you print should again be extracted from `employees.csv`; no names should be hard-coded into your program.

{% spoiler "Hints" %}

If an employee's first name is in a variable, `FirstName`, and an employee's last name is in a variable, `LastName`, recall that you can concatenate them in a variable, `Name`, with code like:

```py
Name = f"{FirstName} {LastName}"
```

Or:

```py
Name = FirstName + " " + LastName.
```

And recall that you can compare two variables, `a` and `b`, for equality with code like:

```py
if a == b:
```

{% endspoiler %}

{% spoiler "More Hints" %}

Recall that a `dict` (i.e., dictionary) in Python allows you to associate "keys" with "values." Accordingly, you can use it to "look up" values by keys, much like you can look up definitions (in a real-world dictionary) by words.

For instance, suppose that you'd like to associate humans with their favorite numbers. You could instantiate (i.e., create) an initially empty `dict` for such as follows:

```py
favorites = {}
```

And you could then add some keys and values as follows:

```py
favorites["Freddy"] = 13
favorites["Douglas"] = 42
```

Thereafter, to check if someone's favorite number is, say, 50, you could use code like the below, where `someone` is their actual name:

```py
if favorites["someone"] == 50:
```

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
pip3 install --upgrade git+git://github.com/cs50/submit50@hbap &>/dev/null && submit50 cs50/labs/pdss/4/employees
```
