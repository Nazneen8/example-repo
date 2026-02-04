# asks user to input swimming time in minutes and prints the answer
swimming = int(input("Enter your completeion time for swimming (in minutes): "))
print(swimming)
print()

# asks user to input cycling time in minutes and prints the answer
cycling = int(input("Enter your completeion time for cycling (in minutes): "))
print(cycling)
print()

# asks user to input running time in minutes and prints the answer
running = int(input("Enter your completeion time for running (in minutes): "))
print(running)
print()

# calculates and displays sum of all three times
total_completion_time = swimming + cycling + running
print("Total completion time is: ",total_completion_time, "minutes.")

# checks if statements are true and outputs matching awards

if total_completion_time <= 100:
    print("Award: Provincial colours")

elif total_completion_time >= 101 and total_completion_time <= 105:
    print("Award: Provincial half colours")

elif total_completion_time >= 106 and total_completion_time <= 110: 
    print("Award: Provincial scroll")

else: 
    print("No award")