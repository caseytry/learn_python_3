Exercise 30: Else and If

In the last exercise you worked out some if-statements and then tried to guess what they are and how they work. Before you learn more I'll explain what everything is by answering the questions you had from Study Drills. You did the Study Drills right?

    What do you think the if does to the code under it? An if-statement creates what is called a "branch" in the code. It's kind of like those choose your own adventure books where you are asked to turn to one page if you make one choice and another if you go a different direction. The if-statement tells your script, "If this Boolean expression is True, then run the code under it, otherwise skip it."
    Why does the code under the if need to be indented four spaces? A colon at the end of a line is how you tell Python you are going to create a new "block" of code, and then indenting four spaces tells Python what lines of code are in that block. This is exactly the same thing you did when you made functions in the first half of the book.
    What happens if it isn't indented? If it isn't indented, you will most likely create a Python error. Python expects you to indent something after you end a line with a : (colon).
    Can you put other boolean expressions from Exercise 27 in the if-statement? Try it. Yes you can, and they can be as complex as you like, although really complex things generally are bad style.
    What happens if you change the initial values for people, cats, and dogs? Because you are comparing numbers, if you change the numbers, different if-statements will evaluate to True and the blocks of code under them will run. Go back and put different numbers in and see if you can figure out in your head which blocks of code will run.

Compare my answers to your answers, and make sure you really understand the concept of a "block" of code. This is important for when you do the next exercise where you write all the parts of if-statements that you can use.

Type this one in and make it work too.

people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

What You Should See

$ python3.6 ex30.py
We should take the cars.
Maybe we could take the trucks.
Alright, let's just take the trucks.

Study Drills

    Try to guess what elif and else are doing.
    Change the numbers of cars, people, and trucks, and then trace through each if-statement to see what will be printed.
    Try some more complex boolean expressions like cars > people or trucks < cars.
    Above each line write an English description of what the line does.


My Responses:
Try to guess what elif and else are doing.
    While 'if' statements on their own provide only one potential branch for the code to go down, elif and else provide more.  'elif' is shortend from 'else-if', which allows for a second condition to be evaulated to see if it should be executed if the first 'if' was not true.

    'Else' is similar to 'elif'; except it must be last in the potential branches as the final 'stopping' point for the code to be evaluated. If you try to put an 'else' before an 'elif', you get a syntax error.

Change the numbers of cars, people, and trucks, and then trace through each if-statement to see what will be printed.

    I changed the values 3 times to change the responses.

    first changed the number of trucks from 15 to 42, which lead to having too many trucks:
        We should take the cars.
        That's too many trucks.
        Fine, let's stay home then.
    
    Then, I changed the number of people from 30 to 50, so that People would be the highest value. This lead to finally taking the trucks.
        We should not take the cars.
        That's too many trucks.
        Alright, let's just take the trucks.

    Last, I changed the value of cars from 40 to 100.
        We should take the cars.
        Maybe we could take the trucks.
        Alright, let's just take the trucks

The last two drills I did in the code.