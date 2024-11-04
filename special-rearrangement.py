#defined the function that will put the even numbers before the odd ones and keeping their order
def special_rearrangement(numbers):
    
    #created two empty lists and will be used later to separate the numbers from the original list depending whether they are even or odd
    odd_numbers = []
    even_numbers = []

    #checking if the numbers are either odd or even and appending them to their respective list
    for i in range(len(numbers)):
        if(numbers[i] % 2 == 0):
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])

    #clearing the old order of the numbers to replace it with the new one 
    #where the even numbers will come before the old ones by using the extend built in function
    numbers.clear()
    numbers.extend(even_numbers)
    numbers.extend(odd_numbers)

    print(numbers)

#initiated a list that consists of random numbers to send it to the special_arrangement function
special_rearrangement([1, 4, 33, 6, 2, 7, 5, 23, 9, -1, -2])