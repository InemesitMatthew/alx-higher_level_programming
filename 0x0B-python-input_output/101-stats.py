#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for a log file
"""

import sys


def print_stats(total_size, status_codes):
    """Prints the computed statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for i, line in enumerate(sys.stdin, start=1):
            tokens = line.split()
            if len(tokens) > 2:
                total_size += int(tokens[-1])
                status_code = tokens[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
