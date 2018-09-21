# Caesar

{% video https://www.youtube.com/watch?v=Rg8P1wHDc0s %}

{% next %}

## Et tu?

Supposedly, Caesar (yes, that Caesar) used to "encrypt" (i.e., conceal in a reversible way) confidential messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D, ..., and, wrapping around alphabetically, Z as A. And so, to say HELLO to someone, Caesar might write IFMMP. Upon receiving such messages from Caesar, recipients would have to "decrypt" them by shifting letters in the opposite direction by the same number of places.

The secrecy of this "cryptosystem" relied on only Caesar and the recipients knowing a secret, the number of places by which Caesar had shifted his letters (e.g., 1). Not particularly secure by modern standards, but, hey, if you're perhaps the first in the world to do it, pretty secure!

Unencrypted text is generally called _plaintext_. Encrypted text is generally called _ciphertext_. And the secret used is called a _key_.

To be clear, then, here's how encrypting `HELLO` with a key of 1 yields `IFMMP`:

| plaintext    | H | E | L | L | O |
|--------------|---|---|---|---|---|
| + key        | 1 | 1 | 1 | 1 | 1 |
| = ciphertext | I | F | M | M | P |

More formally, Caesar's algorithm (i.e., cipher) encrypts messages by "rotating" each letter by _k_ positions. More formally, if _p_ is some plaintext (i.e., an unencrypted message), _p<sub>i</sub>_ is the _i<sup>th</sup>_ character in _p_, and _k_ is a secret key (i.e., a non-negative integer), then each letter, _c<sub>i</sub>_, in the ciphertext, _c_, is computed as

c<sub>i</sub> = (p<sub>i</sub> + k) % 26

wherein `% 26` here means "remainder when dividing by 26." This formula perhaps makes the cipher seem more complicated than it is, but it's really just a concise way of expressing the algorithm precisely. Indeed, for the sake of discussion, think of A (or a) as 0, B (or b) as 1, ..., H (or h) as 7, I (or i) as 8, ..., and Z (or z) as 25. Suppose that Caesar just wants to say Hi to someone confidentially using, this time, a key, _k_, of 3. And so his plaintext, _p_, is Hi, in which case his plaintext's first character, _p<sub>0</sub>_, is H (aka 7), and his plaintext's second character, _p<sub>1</sub>_, is i (aka 8). His ciphertext's first character, _c<sub>0</sub>_, is thus K, and his ciphertext's second character, _c<sub>1</sub>_, is thus L. Can you see why?

Let's write a program called `caesar` that enables you to encrypt messages using Caesar's cipher. At the time the user executes the program, they should decide, by providing a command-line argument, on what the key should be in the secret message they'll provide at runtime. We shouldn't necessarily assume that the user's key is going to be a number; though you may assume that, if it is a number, it will be a positive integer.

Here are a few examples of how the program might work. For example, if the user inputs a key of `1` and a plaintext of `HELLO`:

```
$ ./caesar 1
plaintext:  HELLO
ciphertext: IFMMP
```

Here's how the program might work if the user provides a key of `13` and a plaintext of `hello, world`:

```
$ ./caesar 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
```

Notice that neither the comma nor the space were "shifted" by the cipher. Only rotate alphabetical characters!

How about one more? Here's how the program might work if the user provides a key of `13` again, with a more complex plaintext:

```
$ ./caesar 13
plaintext:  be sure to drink your Ovaltine
ciphertext: or fher gb qevax lbhe Binygvar
```

{% spoiler "Why?" %}

{% video https://www.youtube.com/watch?v=9K4FsAHB-C8 %}

{% endspoiler %}

Notice that the case of the original message has been preserved. Lowercase letters remain lowercase, and uppercase letters remain uppercase.

And what if a user doesn't cooperate?

```
$ ./caesar HELLO
Error: Key is not numeric
```

Or really doesn't cooperate?

```
$ ./caesar
Error: Missing key
```

Or even...

```
$ ./caesar 1 2 3
Error: Too many keys
```

{% spoiler "Try It" %}

To try out the staff's implementation of this problem, execute

<pre>
./caesar KEY
</pre>

substituting a valid integer in place of <code>KEY</code>, within <a href="https://sandbox.cs50.io/fd78b740-81f3-4ab4-adfa-c3e3636ccb2e">this sandbox</a>.

{% endspoiler %}

How to begin? Let's approach this problem one step at a time.

{% next %}

## Pseudocode

First, write in `pseudocode.txt` at right some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There's no one right way to write pseudocode, but short English sentences suffice. Recall how we wrote pseudocode for [finding Mike Smith](https://cdn.cs50.net/2018/fall/lectures/0/lecture0.pdf). Odds are your pseudocode will use (or imply using!) one or more functions, conditions, Boolean expressions, loops, and/or variables.

{% spoiler %}

<p>
  There's more than one way to do this, so here's just one!
</p>

<ol>
  <li>Check that program was run with one command-line argument</li>
  <li>Iterate over the provided argument to make sure all characters are digits</li>
  <li>Convert that command-line argument from a `string` to an `int`</li>
  <li>Prompt user for plaintext</li>
  <li>Iterate over each character of the plaintext:
    <ol>
      <li>If it is an uppercase letter, rotate it, preserving case, then print out the rotated character</li>
      <li>If it is a lowercase letter, shift it, preserving case, then print out the rotated character</li>
      <li>If it is neither, print out the character as is</li>
    </ol></li>
  <li>Print a newline</li>
</ol>

<p>
  It's okay to edit your own after seeing this pseudocode here, but don't simply copy/paste ours into your own!
</p>

{% endspoiler %}

{% next %}

## Counting Command-Line Arguments

Whatever your pseudocode, let's first write only the C code that checks whether the program was run with a single command-line argument.

Specifically, modify `caesar.c` at right in such a way that: if the user provides exactly one command-line argument, it prints out the message `"Success"`; if the user provides no command-line arguments, it prints out `Error: missing key`; and if the user provides more than one command-line argument, it prints out `"Error: Too many keys"`. Remember, since this key is coming from the command line at runtime, and not via `get_string`,  we don't have an opportunity to re-prompt the user. The behavior of the resulting program should be like the below.

```
$ ./caesar 20
Success!
```

or

```
$ ./caesar
Error: Program requires exactly one key
```

or

```
$ ./caesar 1 2 3
Error: Program requires exactly one key
```

{% spoiler "Hints" %}

<ul>
  <li>Recall that you can compile your program with <code>make</code>.</li>
  <li>Recall that you can print with <code>printf</code>.</li>
  <li>Recall that <code>argc</code> and <code>argv</code> give you information about what was provided at the command line.</li>
  <li>Recall that the name of the program itself (here, <code>./caesar</code>) is in `argv[0]`.</li>
</ul>

{% endspoiler %}

{% next %}

## Accessing the Key

Now that your program is (hopefully!) accepting input as prescribed, it's time for another step.

Recall that in our program, we must defend against users who technically provide a single command-line argument (the key), but provide something that isn't actually an integer, for example:

```
$ ./caesar xyz
```

Before we start to analyze the key for validity, though, let's make sure we can actually read it. Further modify `caesar.c` at right such that it not only checks that the user has provided just one command-line argument, but after verifying that, prints out that single command-line argument. So, for example, the behavior might look like this:

```
$ ./caesar 20
Success
20
```

{% spoiler "Hints" %}

<ul>
  <li>Recall that <code>argc</code> and <code>argv</code> give you information about what was provided at the command line.</li>
  <li>Recall that <code>argv</code> is an array of strings.</li>
  <li>Recall that with <code>printf</code> we can print a string using <code>%s</code> as the placeholder.</li>
  <li>Recall that computer scientists like counting starting from 0.</li>
  <li>Recall that we can access individual elements of an array, such as <code>argv</code> using square brackets, for example: <code>argv[0]</code></li>
</ul>

{% endspoiler %}

{% next %}

## Validating the Key

Now that you know how to read the key, let's analyze it. Modify `caesar.c` at right such that instead of printing out the command-line argument provided, your program instead checks to make sure that each character of that command line argument is a decimal digit (i.e., `0`, `1`, `2`, etc.) and, if any of them are not, terminates after printing the message `"Error: Key is not numeric"`. But if the argument consists solely of digit characters, you should convert that string (recall that `argv` is an array of strings, even if those strings happen to look like numbers) to an actual integer, and print out the *integer*. So, for example, the behavior might look like this:

```
$ ./caesar 20
Success!
20
```

or

```
$ ./caesar 20x
Error: Key is not numeric
```

{% spoiler "Hints" %}

<ul>
  <li>Recall that <code>argv</code> is an array of strings.</li>
  <li>Recall that a string, meanwhile, is just an array of <code>char</code>s.</li>
  <li>Recall that the <code>string.h</code> header file contains a number of useful functions that work with strings.</li>
  <li>Recall that we can use a loop to iterate over each character of a string if we know its length.</li>
  <li>Recall that the <code>ctype.h</code> header file contains a number of useful functions that tell us things about characters.</li>
  <li>Recall that we can <code>return</code> nonzero values from <code>main</code> to indicate that our program did not finish successfully.</li>
  <li>Recall that with <code>printf</code> we can print an integer using <code>%i</code> as the placeholder.</li>
  <li>Recall that the <code>atoi</code> function converts a string that looks like a number into that number.</li>
</ul>

{% endspoiler %}

{% next %}

## Peeking Underneath the Hood

As human beings it's easy for us to intuitively understand the formula described above, inasmuch as we can say "H + 1 = I". But can a computer understand that same logic? Let's find out. For now, we're going to temporarily ignore the key the user provided and instead prompt the user for a secret message and attempt to shift all of its characters by just 1.

Extend the functionality of `caesar.c` at right such that, after validating the key, we prompt the user for a string and then shift all of its characters by 1, printing out the result. We can also at this point probably remove the line of code we wrote earlier that prints `"Success!"`. All told, this might result in this behavior:

```
$ ./caesar 20
plaintext:  hello
ciphertext: ifmmp
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
submit50 cs50/2018/fall/caesar
```
