<div align="center">

# Sort a List

Sort any list containing data of any datatype and in any order.

</div>

## Features
- Can automatically detect data type and sort accordingly if not specified.
- Support both command line input and file input.
- Sort in both ascending and descending order.

## To Run the Code

### With Default Values

```bash
python3 main.py
```

### Sorting a List Stored in File

```bash
python3 main.py --file <file>
```

### Sorting a List in Descending Order

```bash
python3 main.py --file <file> --order desc
```

### Providing item datatype to sort with

```bash
python3 main.py --file <file> --sortby int
```

## Getting Help

```bash
python3 main.py --help
```

## Output

```bash
$ python3 main.py
Enter number of elements in list: 3
Enter List Element: 
Tomato
Potato
Cucumber

Sorted List
Cucumber
Potato
Tomato
```

```bash
$ python3 main.py --file ./sample.txt --order desc

Sorted List
345
123.23
23
3
```