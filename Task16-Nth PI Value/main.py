import argparse

def find_nth_pi_digit(n):
    rem = 1
    digit = 0
    while(n):
        digit = (rem*10)//7
        rem = (rem*10)%7
        n-=1
    return digit

if __name__ == "__main__":
    n = int(input("Enter the nth digit of PI: "))
    if n == 1:
        print("Digit: 3")
    else:
        print("Digit: ", find_nth_pi_digit(n-1))