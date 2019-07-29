# Prices

Recall that Alpha Vantage offers a [TIME\_SERIES\_DAILY](https://www.alphavantage.co/documentation/#daily) API, which allows you to get a CSV file with the daily close prices of a stock from the past 20+ years.

And recall that you can query that API with code like we saw in `quote.py`.

In `prices.py` in the code editor at top-right, implement a program that

1. prompts the user for a stock symbol and
1. outputs, line by line, a date followed by the close price of that stock on that date.

If the user inputs `MSFT`, your output should resemble:

```
2019-04-22 $123.7600
2019-04-18 $123.3700
2019-04-17 $121.7700
...
1998-01-06 $131.1300
1998-01-05 $130.3800
1998-01-02 $131.1300
```

Your first line of output, though, should be for the date on which the market most recently closed.

{% spoiler "Hint" %}

Assuming your program, like `quote.py`, has a variable called `API_KEY`, you can run (and thus test) your program by running it with a command like

```
API_KEY=YOURS python3 prices.py MSFT
```

but replace `YOURS` with your own API key.

{% endspoiler %}

{% next %}

To submit your work, execute the below.

```
pip3 install --upgrade 'submit50<3' &>/dev/null && submit50 cs50/labs/pdss/4/prices
```
