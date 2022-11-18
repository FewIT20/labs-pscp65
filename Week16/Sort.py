"""IG: few.pz"""


def merge_value(value):
    """ Merge Sorted by some where """
    if len(value) > 1:
        mid = len(value) // 2
        left = value[:mid]
        right = value[mid:]
        # Recursive call on each half
        merge_value(left)
        merge_value(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                value[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                value[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            value[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            value[k] = right[j]
            j += 1
            k += 1


def main():
    """ Main function """
    value = []
    while True:
        raw = input()
        if raw == "END":
            break
        value.append(int(raw))
    merge_value(value)
    for i in value:
        print(i)


main()
