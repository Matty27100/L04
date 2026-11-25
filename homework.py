import os


# Level 1 (easy)
def celsius_to_fahrenheit(c):
    """The temperature c, given in degrees Celsius, in degrees Fahrenheit (F = C * 9 / 5 + 32)"""
    return c * 9 / 5 - 32


# Level 2 (easy-medium)
def is_leap_year(year):
    """True for leap years: years divisible by 4, except years divisible by 100,
    which are leap years only if they are also divisible by 400 (2000 is, 1900 is not)"""
    return year % 4 == 0 and year % 100 != 0


# Level 3 (medium)
def median(numbers):
    """The middle value of the numbers once they are sorted. For an even count, the average
    of the two middle values. An empty list has median None. The list itself is not changed"""
    middle = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[middle]
    return (numbers[middle - 1] + numbers[middle]) / 2


# Level 4 (medium-hard)
def binary_search(items, target):
    """The index of target in the sorted list items, or -1 if target is not in the list"""
    low, high = 0, len(items) - 1
    while low < high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Level 5 (hard)
def ping(host):
    """Pings host once (Linux ping) and returns True if the ping succeeded.
    host must be a hostname or an IP address: only letters, digits, dots and dashes,
    starting with a letter or a digit. For any other host, return False without running anything"""
    return os.system(f"ping -c 1 {host}") == 0
