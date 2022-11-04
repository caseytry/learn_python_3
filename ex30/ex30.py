#defining the variable people with the integer value of 30
people = 30
#defining the variable cars with the integer value of 40
cars = 30
#defining the variable trucks with the integer value of 15
trucks = 30

#evaluate if the number of cars is greater than the number of people.
if cars > people:
    #if cars are greater than people, print the sentence.
    print("We should take the cars.")
#if first condition was not true, evaluate this expression for if the number of cars is less than the number of people.
elif cars < people:
    #if cars are less than people, then print the sentence.
    print("We should not take the cars.")
#if neither of the above conditions are true, then continue to this branch.
else:
    #if the above logic is True, then print the sentence.
    print("We can't decide.")

#evaluate if the number of trucks is greater than the number of cars.
if trucks > cars:
    #if the number of trucks is greater than the number of cars, then print this sentence.
    print("That's too many trucks.")
#if first statement was not true, evaluate if trucks is less than cars.
elif trucks < cars:
    #if trucks are less than cars, print the statement.
    print("Maybe we could take the trucks.")
#if neither condition above is true, continue to this evaluation. 
else:
    #if this condition is true, print this sentence
    print("We still can't decide.")

#evaluate if the vaule of people is greater than the value of trucks.
if people > trucks:
    #if the value of people is greater than the value of trucks, print the statement.
    print("Alright, let's just take the trucks.")
#if the first statement was not true, continue to this statement.
else:
    #if this statment is found to be true, print the sentence.
    print("Fine, let's stay home then.")

#Study Drill additions:
if people < cars and cars > trucks:
    print("We have more than enough cars.")
elif people < trucks and trucks > cars:
    print("We have more trucks than cars or people.")
elif people > cars and people > trucks:
    print("We need both cars and trucks, people outnumber both.")
else:
    print("People may equal cars or trucks. review!")