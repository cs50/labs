# Scrabble

Determine which of two Scrabble words is worth more.

## Background

In the game of [Scrabble](https://scrabble.hasbro.com/en-us/rules), players create words to score points, and the number of points is the sum of the point values of each letter in the word. 

For example, if we wanted to score the word `Code`, we would note that in general Scrabble rules, the `C` is worth `3` points, the `o` is worth `1` point, the `d` is worth `2` points, and the `e` is worth `1` point. Summing these, we get that `Code` is worth `3+1+2+1 = 7` points. 

## Implementation Details

Complete the implementation of `scrabble.c` at right, such that it determines the winner of a short scrabble-like game, where two players each enter their word, and the higher scoring player wins.

* We've stored the point values of each letter of the alphabet in an integer array named `POINTS`. 
  * For example, `A` or `a` is worth `1` point, `B` or `b` is worth `3` points, etc.
* We've created a header for a helper function called `score()` that takes a string as input and returns an `int`. Whenever we would like to assign point values to a particular word, we can call this function. Note that this header is required for C to know that `score()` exists later in the program. 
* In `main()`, the program prompts the two players for their words using the `get_string()` function. These values are stored inside variables named `p1` and `p2`.
* In `score()`, your program should compute, using the `POINTS` array, and return the score for the string argument. Characters that are not letters should be given zero points, and uppercase and lowercase letters should be given the same point values. 
  * `!` is worth `0` points while `A` and `a` are both worth `1` point.
* In `main()`, your program should print the winner, whether `Player 1` or `Player 2`, via their scores. If the scores are the same, there is a tie.  
  
### Hints

* You may find the functions `isupper()` and `islower()` to be helpful to you. These functions take in a character as the argument and return a boolean. 
  
* To find the value at the `n`th index of an array called `arr`, we can write `arr[n]`. We can apply this to strings as well, as strings are arrays of characters. 

* The ASCII standardized system may prove to be helpful to you, as it maps characters to numbers. 

### How to Test Your Code

Your program should behave per the examples below.

```
./scrabble 
Player 1: Question?
Player 2: Question!
Tie!
```

```
$ ./scrabble
Player 1: Oh,
Player 2: hai!
Player 2 wins!
```

```
$ ./scrabble 
Player 1: COMPUTER
Player 2: Science
Player 1 wins!
```

```
$ ./scrabble 
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

{% next %}

## How to Submit

TODO
