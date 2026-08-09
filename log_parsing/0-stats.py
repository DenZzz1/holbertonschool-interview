#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            try:
                file_size = int(parts[-1])
            except ValueError:
                continue

            status_code = parts[-2]

            total_size += file_size

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
