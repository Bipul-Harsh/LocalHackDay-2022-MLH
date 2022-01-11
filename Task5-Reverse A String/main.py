def reverse_string(string):
    return string[::-1]

if __name__ == "__main__":
    cnt = True
    while cnt:
        string = input("Please enter a string to reverse: ")
        print('Reversed String: \n'+reverse_string(string))
        cnt = input("Do you want to continue? (y/n): ")
        if cnt == 'n':
            exit(0)