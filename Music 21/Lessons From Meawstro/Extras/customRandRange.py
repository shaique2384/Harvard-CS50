# A random randrange() 
import time

def main():
    # Pick a number between 0 and 9
    print(custom_randrange(10))

    # Pick an odd number between 1 and 20
    print(custom_randrange(0, 19, 2))

def custom_randrange(start, stop=None, step=1):
    # 1. Handle single-argument calls, e.g., custom_randrange(10) -> range(0, 10)
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("zero step for randrange()")

    # 2. Generate all valid numbers in the range
    valid_numbers = list(range(start, stop, step))
    
    if not valid_numbers:
        raise ValueError(f"empty range for randrange({start}, {stop}, {step})")

    # 3. Generate a pseudo-random integer using current time in nanoseconds
    seed = custom_time_ns()//200
    
    # 4. Pick an index using modulo arithmetic
    random_index = seed % len(valid_numbers)

    return valid_numbers[random_index]
    #return random_index

import ctypes
import os


def custom_time_ns() -> int:
    """Returns the current system time in nanoseconds since the Unix epoch (Jan 1, 1970)."""

    if os.name == "nt":  # Windows implementation
        # GetSystemTimeAsFileTime returns time in 100-nanosecond intervals since Jan 1, 1601
        class FILETIME(ctypes.Structure):
            _fields_ = [
                ("dwLowDateTime", ctypes.c_uint32),
                ("dwHighDateTime", ctypes.c_uint32),
            ]

        ft = FILETIME()
        ctypes.windll.kernel32.GetSystemTimeAsFileTime(ctypes.byref(ft))

        # Combine high and low bits into a single 64-bit integer
        filetime_100ns = (ft.dwHighDateTime << 32) + ft.dwLowDateTime

        # Convert epoch from Jan 1, 1601 to Jan 1, 1970 (11,644,473,600 seconds difference)
        EPOCH_DIFF_100NS = 116444736000000000

        # Convert 100-ns units to nanoseconds (* 100)
        return (filetime_100ns - EPOCH_DIFF_100NS) * 100


if __name__ == '__main__':
    main()