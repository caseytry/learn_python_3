# Exercise 29: What If

Here is the next script of Python you will enter, which introduces you to the if-statement. Type this in, make it run exactly right, and then we'll see if your practice has paid off.

```python
people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
```



## What You Should See

```sh
$ python3.6 ex29.py
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
```



## Study Drills

In this Study Drill, try to guess what you think the if-statement is and what it does. Try to answer these questions in your own words before moving on to the next exercise:

> What do you think the if does to the code under it?
> Why does the code under the if need to be indented four spaces?
> What happens if it isn't indented?
> Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
> What happens if you change the initial values for people, cats, and dogs?



### My response:
> What do you think the if does to the code under it?
After the 'if' statement is evaluated for if it is true or not, the code beneath it is only executed if the statement was True. 

> Why does the code under the if need to be indented four spaces?
To indicate/ensure that the code is a part of an expression and is only ran if the "If" statement was true.

> What happens if it isn't indented?
You get an IndentationError, where python expects the code to be indented.

> Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
I did these updates in the final part of the code, underneath comment

> What happens if you change the initial values for people, cats, and dogs?
The expressions change to the other results (IE: if cats are lower than people, returns the "The world is saved",  if people are less than dogs, returns "The world is drooled on")