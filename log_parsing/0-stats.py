#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys
import re


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    pattern = re.compile(
        r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            match = pattern.match(line.strip())
            if not match:
                continue

            status_code, file_size = match.groups()

            total_size += int(file_size)

            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
