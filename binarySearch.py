'''
Simon Anatole Orlovsky
Binary Search
1/3/17
'''

def binarySearch(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def main():
    lst = list(range(10))
    print(binarySearch(lst, 7))
    print(binarySearch(lst, 11))

main()
