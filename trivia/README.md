# Trivia

Create a webpage with trivia questions.

## Implementation Details

Complete the implementation of `trivia.html` at right, such that the webpage contains at least 1 multiple choice question and 1 text input question. 

* Under `Part 1: Multiple Choice`, write a multiple choice question. Then, write the script necessary such that when a person selects an answer choice, the choice becomes red or green depending on whether the choice is correct or not. 
  
* Under `Part 2: Text Answers`, write a text input question and the script necessary such that when a person submits an answer, the text box turns red or green depending on whether the answer is correct or not.

* Notice that some CSS has already been included for you in `styles.css`, and this file has already been linked to `trivia.html`. Feel free to change `styles.css` how you'd like!
  
### Hints

* Recall that when changing a property of an HTML element with `id=id_name`, `document.querySelector(#id_name)` allows us to retrieve that particular element. We can then change the style of that element. 

* For the multiple choice, it may help to use `<button>` tags, and for the text answer, it may help to use `<form>` and `<input>` tags. You may additionally find it helpful that the `<form>` tag has an attribute called `onsubmit`, where upon user submission, the action specified by `onsubmit` will be executed.

### How to Test Your Code

You should see your webpage upon running the following in the terminal window: 

```
$ http-server
```


{% next %}

## How to Submit

TODO
