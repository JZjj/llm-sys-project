def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Args:
        intervals (list of tuple): List of intervals represented as tuples (start, end).
        
    Returns:
        list of tuple: List of merged intervals sorted by start times.
        
    Raises:
        TypeError: If input is not a list or intervals are not tuples of two integers.
        ValueError: If interval start is greater than interval end.
    """
    if not isinstance(intervals, list):
        raise TypeError("Input must be a list of intervals.")
    
    # Validate intervals
    for interval in intervals:
        if not (isinstance(interval, tuple) and len(interval) == 2):
            raise TypeError("Each interval must be a tuple of two integers.")
        start, end = interval
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("Interval bounds must be integers.")
        if start > end:
            raise ValueError(f"Interval start ({start}) cannot be greater than end ({end}).")
    
    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    
    for interval in sorted_intervals:
        if not merged or merged[-1][1] < interval[0]:
            # No overlap, append interval
            merged.append(interval)
        else:
            # Overlap, merge intervals
            last_start, last_end = merged[-1]
            merged[-1] = (last_start, max(last_end, interval[1]))
    
    return merged


def main():
    example_intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    try:
        merged = merge_intervals(example_intervals)
        print("Merged intervals:", merged)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()