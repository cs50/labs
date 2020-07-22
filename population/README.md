# Population Growth

Determine how long it takes for a population to reach a particular size.

```
$ ./population
Start size: 100
End size: 200
9 years
```

## Populations

Say we have a popluation of `n` llamas. Each year, `n/3` new llamas are born, and `n/4` llamas pass away.

For example, if we were to start with `n = 1200` llamas, then in that year, `1200/3` new llamas would be born and `1200/4` llamas would pass away. At the end of that year, we would have `1200 + 1200/3 - 1200/4 = 1200 + 400 - 300 = 1300` llamas. 

As another example, if we were to start with `n = 1000` llamas, at the end of the year , we would have `1000 + 1000/3 - 1000/4 = 1083.33` llamas. We can't have a decimal portion of a llama though, so we'll truncate the decimal to get `1083`. The next year will then begin with `1083` llamas.

## Implementation Details

Complete the implementation of `population.c` at right, such that it calculates the number of years required for the population to grow from the start size to the end size.

* The program prompts the user for two numbers. To prompt the user, we use the `get_int()` function, which takes in a message as its argument. This function, when called, will print the specified message and return the value that the user inputs into the system. 
* We've stored the values returned by the `get_int()` function inside variables named `start` and `end`, both having the `int` data type. `start` and `end` represent the numbers of llamas we're starting with and ending with. 
* Your program should first ensure that the end size is greater than the start size. It should prompt the user to enter another value for as long as this condition is not met.
* Your program should then calculate an integer number of years until the end value is reached. Remember that there cannot be a decimal number of llamas at the end of each year.
* Finally, your program should print the number of years required for the llama population to reach that end size.

### Hints

* To create a new variable, make sure to specify a data type, a name for the variable, and what value it should be assigned to. It might help to take a look at how the variables `start` and `end` are created.
  
* You might find a while loop helpful to you. Remember that a while loop works as follows: while a certain condition evaluates to true, execute these particular commands. Stop when the condition no longer evaluates to true.
    ```C
    while(condition evaluates to true)
    {
        commands to execute;
    }
    ```
  

### How to Test Your Code

Your program should behave per the examples below.


```
$ ./population
Start size: 1200
End size: 1300
1 years
```

```
$ ./population
Start size: 1000
End size: 10000
29 years
```

```
$ ./population
Start size: 20
End size: 1
End size must be greater than start size.
End size: 10
End size must be greater than start size.
End size: 100
20 years
```

```
$ ./population
Start size: 100
End size: 1000000
115 years
```

{% next %}

## How to Submit

TODO
