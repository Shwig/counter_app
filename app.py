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

def appened_data_file(number):
    number_string = str(number)
    f = open("data.txt","a+")
    f.write(number_string)
    f.close()

def load_data_array():
    with open("data.txt") as f:
        numbers.append([int(x) for x in next(f).split()])
    f.close()

def display_data(data_array):
    pylab.hist(data_array)
    pylab.show()

def main():
    load_data_array()
    print(numbers)

if __name__ == "__main__":
    main()
