# Similarities

Determining whether two files are identical is (relatively!) trivial: iterate over the characters in each, checking whether each and every one is identical. But determining whether two files are similar is non-trivial. After all, what does it mean to be similar? Perhaps the files have lines in common. Perhaps the files have sentences in common. Perhaps the files have only substrings in common.

Suffice it to say, the challenge ahead is to determine if two files are similar! You'll complete the implementation of a web app that does just that, a la [similarities.cs50.net](https://similarities.cs50.net/)!

{% next %}

## `helpers.py`

Let's first have you complete the implementation of a few functions in `helpers.py`.

### `lines`

Implement `lines` in such a way that, given two strings, `a` and `b`, it returns a `list` of the lines that are, identically, in both `a` and `b`.   The `list` should not contain any duplicates. Assume that lines in `a` and `b` will be be separated by `\n`, but the strings in the returned `list`  should not end in `\n`. If both `a` and `b` contain one or more blank lines (i.e., a `\n` immediately preceded by no other characters), the returned `list` should include an empty string (i.e., `""`).

To test your implementation of `lines` (via a command-line program we've written for you), execute the below, where `FILE1` and `FILE2` are any two text files (e.g., those in `inputs/`):

```
python compare.py --lines FILE1 FILE2
```

### `sentences`

Implement `sentences` in such a way that, given two strings, `a` and `b`, it returns a `list` of the _unique_ English sentences that are,            identically, present in both `a` and `b`. The `list` should not contain any duplicates. Use `sent_tokenize` from the Natural Language Toolkit to     "tokenize" (i.e., separate) each string into a `list` of sentences. It can be imported with:

```python
from nltk.tokenize import sent_tokenize
```

Per its http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize[documentation], `sent_tokenize`, given a `str` as input, returns a    `list` of English sentences therein. It assumes that its input is indeed English text (and not, e.g., code, which might coincidentally have periods  too).

To test your implementation of `sentences` (via a command-line program we've written for you), execute the below, where `FILE1` and `FILE2` are any two text files (e.g., those in `inputs/`):

```
python compare.py --sentences FILE1 FILE2
```

### `substrings`

Implement `substrings` in such a way that, given two strings, `a` and `b`, and an integer, `n`, it returns a `list` of all substrings of length `n`  that are, identically, present in both `a` and `b`. The `list` should not contain any duplicates.

Recall that a substring of length `n` of some string is just a sequence of `n` characters from that string. For instance, if `n` is `2` and the      string is `Yale`, there are three possible substrings of length `2`: `Ya`, `al`, and `le`. Meanwhile, if `n` is `1` and the string is `Harvard`,     there are seven possible substrings of length `1`: `H`, `a`, `r`, `v`, `a`, `r`, and `d`. But once we eliminate duplicates, there are only five      unique substrings: `H`, `a`, `r`, `v`, and `d`.

To test your implementation of `substrings` (via a command-line program we've written for you), execute the below, where `FILE1` and `FILE2` are any two text files (e.g., those in `inputs/`) and `LENGTH` is an integer:

```
python compare.py --substrings LENGTH FILE1 FILE2
```

## `templates/index.html`

Finally, complete the implementation of `templates/index.html` in such a way that it contains an HTML form via which a user can submit:

* a file called `file1`
* a file called `file2`
* a value of `lines`, `sentences`, or `substrings` for an `input` called `algorithm`
* a number called `length`

To test your implementation, execute

```
flask run
```

and then visit the outputted URL. Be sure to test your implementation with the files in `inputs/` (which you can download from your lab) as well as with some files of your own!

{% next %}

To submit your work, execute the below.

```
submit50 cs50/labs/cscip14300/similarities
```
