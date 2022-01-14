import argparse

def find_dtype(lst):
    '''
    This function is used to find the data type from element of given list.
    
    Parameters:
        lst: List to be checked.
        
    Returns:
        Data type of the list.
    '''
    concatenated_string = ''.join(lst)
    if concatenated_string.isdigit():
        return int
    elif concatenated_string.replace('.', '').isdigit():
        return float
    else:
        return str

def sort_list(lst, dtype, order):
    '''
    This function is used to sort a list.
    
    Parameters:
        lst: List to be sorted.
        dtype: Data type of the list.
        order: Order of the list.
        
    Returns:
        Sorted list.
    '''
    try:
        if order == 'asc':
            return sorted(lst, key=lambda x: dtype(x))
        else:
            return sorted(lst, key=lambda x: dtype(x), reverse=True)
    except ValueError:
        print("You have entered an invalid sort_by type.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog="Sort a List",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--file', type=str, default=None, help="Provide any text to convert to cipher.",nargs='?')
    parser.add_argument('--sortby', type=str, default=None, help="Type `int` to sort by integer, `str` to sort by string and `float` to sort by float.", nargs='?')
    parser.add_argument('--order', type=str, default="asc", help="Type `asc` for ascending order and `desc` for descending order.", nargs='?')

    args = parser.parse_args()
    FILE = args.file
    SORT_BY = args.sortby
    ORDER = args.order

    assert ORDER in ['asc', 'desc'], "Invalid order. Please provide `asc` or `desc`."
    
    lst = []

    if FILE:
        with open(FILE) as file:
            for line in file.readlines():
                lst.append(line.strip())
    else:
        n = int(input("Enter number of elements in list: "))
        print("Enter List Element: ")
        for _ in range(n):
            lst.append(input().strip())
    
    if SORT_BY:
        assert SORT_BY in ["int", "str", "float"], "Invalid sort type. Please provide `int`, `str` or `float`."
        if SORT_BY == 'int':
            dtype = int
        elif SORT_BY == 'float':
            dtype = float
        else:
            dtype = str
    else:
        dtype = find_dtype(lst)
    
    sorted_list = sort_list(lst, dtype, ORDER)
    print(f'\nSorted List')
    for item in sorted_list:
        print(item)