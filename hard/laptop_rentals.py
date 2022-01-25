def laptopRentals(times):
    if not times:
        return 0
    start_times = sorted([time[0] for time in times])
    end_times = sorted([time[1] for time in times])
    start_index = 0
    end_index = 0
    laptop_count = 0
    while start_index < len(times) and end_index < len(times):
        if start_times[start_index] < end_times[end_index]:
            start_index += 1
            laptop_count += 1
            continue
        start_index += 1
        end_index += 1
    return laptop_count
