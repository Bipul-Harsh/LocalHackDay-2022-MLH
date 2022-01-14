'''
Generate Random Number between given range.
Using current time to create random number.
'''

import argparse
import datetime

def get_random_number(MIN, MAX):
    '''
    Generate random number between MIN and MAX.
    '''
    return MIN + (datetime.datetime.now().microsecond % (MAX - MIN))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog="Random Number Generator",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--min', type=int, default=0, help="Provide staring range integer value.",nargs='?')
    parser.add_argument('--max', type=int, default=100, help="Provide ending range ineger value.", nargs='?')

    args = parser.parse_args()
    MIN = args.min
    MAX = args.max

    if MIN > MAX:
        print("Starting range value is greater than ending range value.")
        exit(1)
    else:
        print(f'{get_random_number(MIN, MAX)}')