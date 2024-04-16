#!/usr/bin/python3

import sys

def print_statistics(total_size, status_counts):
    """
    Prints the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    """
    Main function to read stdin line by line and compute metrics.
    """
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                size = int(parts[-1])
                status_code = parts[-2]
                total_size += size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

            except ValueError:
                # Ignore lines that don't conform to the expected format
                pass

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

