# Vigenère

{% video https://www.youtube.com/watch?v=L7d2-lcfOz0 %}

{% next %}

## Ooh, la la!

Vigenère’s cipher improves upon Caesar’s cipher by encrypting messages using a _sequence_ of keys (or, put another way, a _keyword_).

In other words, if _p_ is some plaintext and _k_ is a keyword (i.e., an alphabetical string, whereby A (or a) represents 0, B (or b) represents 1, C (or c) represents 2, …​, and Z (or z) represents 25), then each letter, _c<sub>i</sub>_, in the ciphertext, _c_, is computed as:

c<sub>i</sub> = (p<sub>i</sub> + k<sub>j</sub>) % 26

Note this cipher’s use of _k<sub>j</sub>_ as opposed to just _k_. And if _k_ is shorter than _p_, then the letters in _k_ must be reused cyclically as many times as it takes to encrypt _p_.

In other words, if Vigenère himself wanted to say HELLO to someone confidentially, using a keyword of, say, ABC, he would encrypt the H with a key of 0 (i.e., A), the E with a key of 1 (i.e., B), and the first L with a key of 2 (i.e., C), at which point he’d be out of letters in the keyword, and so he’d reuse (part of) it to encrypt the second L with a key of 0 (i.e., A) again, and the O with a key of 1 (i.e., B) again. And so he’d write HELLO as HFNLP, per the below:

| plaintext    | H | E | L | L | O |
|--------------|---|---|---|---|---|
| + key        | A | B | C | A | B |
| (shift value)| 0 | 1 | 2 | 0 | 1 |
| = ciphertext | H | F | N | L | P |

Let's now write a program called `vigenere` that enables you to encrypt messages using Vigenère's cipher. At the time the user executes the program, they should decide, by providing a command-line argument, on what the keyword should be for the secret message they'll provide at runtime.

Here are a few examples of how the program might work.

```
$ ./vigenere bacon
plaintext:  Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```

or for when the user provides a keyword that is not fully alphabetic:

```
$ ./vigenere 13
Usage: ./vigenere k
```

or for when they don't provide a keyword at all:

```
$ ./vigenere
Usage: ./vigenere k
```

or for when they provide too many keywords:

```
$ ./vigenere bacon and eggs
Usage: ./vigenere k
```

{% spoiler "Try It" %}

To try out the staff's implementation of this problem, execute

<pre>
./vigenere KEYWORD
</pre>

substituting a valid alphabetic string in place of <code>KEYWORD</code>, within <a href="https://sandbox.cs50.io/fd78b740-81f3-4ab4-adfa-c3e3636ccb2e">this sandbox</a>.

{% endspoiler %}

How to begin? Let's start with something familiar.

{% next %}

## Déjà vu

As you may have gleaned from the write-up above, the basic idea for this cipher is strikingly similar to the idea underlying the Caesar cipher. As such, our code from Caesar seems like a good place to begin, so feel free to start by replacing the entire contents of `vigenere.c`, at right, with your solution to `caesar.c`.

One difference between Caesar's and Vigenère's ciphers is that the Vigenère cipher key is a series of letters, rather than a number. So let's make sure that the user actually gave us a keyword! Modify the check you implemented in Caesar to instead ensure every character of the keyword is alphabetic, rather than a digit. If any of them isn't, print `"Usage: ./vigenere k"` and return a nonzero value as we did before. If they are all alphabetic, after checking you should print `"Success"` and then, `return 0;` immediately (for now), since our enciphering code is not quite ready to work just yet, so we won't have our program execute it.

Sample behavior:

```
$ ./vigenere alpha
Success
```

or

```
$ ./vigenere 123
Usage: ./vigenere k
```

{% spoiler "Hints" %}

<ul>
  <li>Recall that the <code>string.h</code> header file contains a number of useful functions that work with strings.</li>
  <li>Recall that we can use a loop to iterate over each character of a string if we know its length.</li>
  <li>Recall that the <code>ctype.h</code> header file contains a number of useful functions that tell us things about characters.</li>
</ul>

{% endspoiler %}

## Getting the shift value

Let's for now assume that the user is providing single-character keywords. Can we convert that character into the correct shift value? Let's do so by writing a _function_.

Near the top of your file, below the `#include` lines, let's _declare_ a new function whose purpose is to do just that. It will take a single character as input, and it will output the shift value for that character.

```
int shift(char c);
```

Now we've declared a function called `shift` that takes a single character (`c`) as input, and will output an integer.

Now, down below the closing curly brace of `main`, let's give ourselves a place to _define_ this new function.

```
int shift(char c)
{
   // TODO
}
```

In place of that `TODO` is where we'll do the work of converting that character to its positional integer value (so, again, `A` or `a` would be 0, `B` or `b` would be 1, `Z` or `z` would be 25, etc.)

To test this out, delete the line where you printed `"Success"` (but leave the `return 0;` for now), and in place of the just-deleted line, add the below lines to test whether your code works.

```
int key = shift('A');
printf("%i\n", key);
```

Your program should print a 0! Replace the `'A'` with other capital and lowercase letters. Is the behavior what you expect?

{% spoiler "Hints" %}

<ul>
  <li>Functions have inputs and outputs.</li>
  <li>When we <i>declare</i> a function, we need to provide its return type, name, and an argument list, each of which also has a type.</li>
  <li>When we <i>use</i> or <i>call</i> a function, we just plug in appropriate values in the argument list, and assign the output of the function to a variable that correspond's to the function's return type.</li>
  <li>Recall that the <code>ctype.h</code> header file contains a number of useful functions that tell us things about characters.</li>
  <li>The ASCII value of <code>A</code> is 65. The ASCII value of <code>a</code> is 97.</li>
  <li>The ASCII value of <code>B</code> is 66. The ASCII value of <code>b</code> is 98. See a potential pattern emerging?</li>
</ul>

{% endspoiler %}

## One-character keywords

Time to get start using that enciphering code you wrote before again! You may have noticed that if your keyword _k_ consists of exactly one letter (say, `H` or `h`), Vigenère's cipher effectively becomes a Caesar cipher (of, in this example, 7). Let's for now just assume the user's keyword will just be a single letter. Use your newly-written `shift` function to calculate the shift value for the letter they provided, assign the return value of that function to an integer variable `key`, and use `key` exactly as you did in the Caesar cipher!

```
$ ./vigenere A
plaintext:  hello
ciphertext: hello
```

or

```
$ ./vigenere b
plaintext:  HELLO
ciphertext: ifmmp
```

or

```
$ ./vigenere C
plaintext:  HeLlO
ciphertext: JgNnQ
```

{% spoiler "Hints" %}

<ul>
  <li>Try to iterate over every character in the plaintext and literally add 1 to it, then print it.</li>
  <li>If <code>ch</code> is a <code>char</code> variable in C, what happens when you <code>printf("%c", ch + 1);</code>?</li>
</ul>

{% endspoiler %}

{% next %}

## Your Turn

Now it's time to tie everything together! Instead of shifting the characters by 1, modify `caesar.c` to instead shift them by the actual key value. And be sure to preserve case! Capital letters should stay capital, lowercase letters should stay lowercase, and things that aren't letters...

{% spoiler "Hints" %}

<ul>
  <li>Best to use the modulo operator, <code>%</code>, to handle wraparound from Z to A!</li>
  <li>Things get weird if we try to wrap <code>Z</code> or <code>z</code> by 1 using the technique in the previous section.</li>
  <li>Things get weird also if we try to wrap punctuation marks using that technique.</li>
  <li>Recall that the ASCII table maps all printable characters to numbers.</li>
  <li>Recall that the ASCII value of <code>A</code> is 65. The ASCII value of <code>a</code>, meanwhile, is 97.</li>
</ul>

{% endspoiler %}

{% next %}

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/2018/fall/vigenere
```
