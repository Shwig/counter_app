import csv
from matplotlib import pylab

numbers = []

def get_user_input():
    validate = tuple(range(1,11))
    while True:
        try:
            user_input = input("Enter a number from 1-10 >> ")
            user_input = int(user_input)
        except ValueError:
            print("\n*Your seleciton is not a valid number*")
        if user_input not in validate:
            print("!Please enter a valid number between 1 and 10\n")
        else:
            break
    return user_input

def append_data_file(number):
    with open('data.csv', 'a+',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([number])

def load_array():
    with open('data.csv', newline='') as f:
        file_data = csv.reader(f)
        for row in file_data:
            numbers.extend(map(int,row))

def display_data(data_array):
    data_array.sort()
    pylab.hist(data_array, bins = 10)
    pylab.xlabel("User Input")
    pylab.ylabel("test")
    pylab.xticks(range(1,11))
    pylab.show()

def main():
    try:
        load_array()
    except OSError as e:
        # file will not exist on first execution
        pass

    value = get_user_input()
    append_data_file(value)
    numbers.append(value)
    # display the histogram
    # display_data(numbers)

if __name__ == "__main__":
    main()
