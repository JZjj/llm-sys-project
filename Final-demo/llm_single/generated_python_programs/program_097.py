import sys

def longest_increasing_subsequence(nums):
    """
    Compute the length of the longest strictly increasing subsequence in the list nums.
    Uses a dynamic programming approach with O(n log n) complexity.
    """
    if not nums:
        return 0

    import bisect
    subseq = []
    for num in nums:
        # Find the position to insert num in subseq to keep it sorted
        pos = bisect.bisect_left(subseq, num)
        if pos == len(subseq):
            subseq.append(num)
        else:
            subseq[pos] = num
    return len(subseq)


def process_line(line, line_number):
    """
    Process a single line of comma-separated integers,
    return the length of the longest increasing subsequence.
    Raises ValueError if the line contains invalid data.
    """
    # Strip whitespace and split by comma
    parts = line.strip().split(',')
    if not parts or (len(parts) == 1 and parts[0] == ''):
        # Empty line or line with only whitespace
        raise ValueError(f"Line {line_number}: Empty or invalid line")

    nums = []
    for part in parts:
        part = part.strip()
        if part == '':
            raise ValueError(f"Line {line_number}: Empty value detected between commas")
        try:
            num = int(part)
        except ValueError:
            raise ValueError(f"Line {line_number}: Invalid integer '{part}'")
        nums.append(num)

    return longest_increasing_subsequence(nums)


def main():
    """
    Main function to read a file specified by the user,
    process each line, and print the length of the longest increasing subsequence.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, 1):
                # Skip empty lines silently
                if not line.strip():
                    continue
                try:
                    lis_length = process_line(line, line_number)
                    print(lis_length)
                except ValueError as e:
                    print(f"Error processing line {line_number}: {e}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"IOError while reading file '{input_file}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()