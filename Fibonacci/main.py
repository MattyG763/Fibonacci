def main():
    #Sequence 0, 1, 1, 2, 3
    n = get_input()
    fibonacci(n)


def fibonacci(n): 
    current_place = 1
    sequence = [0, 1]

    while n != 0:
        #Add the current number with the previous one
        add = sequence[current_place - 1] + sequence[current_place]
        #take the new number and append to the end of the list
        sequence.append(add)
        #increase by one the current_place by 1 and decrease n by 1
        current_place += 1
        n -= 1
    
    print(sequence)



def get_input():
    return int(input("How many times would you like to iterate? "))


main()