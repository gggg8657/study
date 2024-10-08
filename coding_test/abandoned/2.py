from datetime import datetime, timedelta

def is_valid_time(time_str):
    # Remove the colons
    digits = time_str.replace(":", "")
    # Convert to a set to see how many unique digits there are
    unique_digits = set(digits)
    # Check if there are 2 or fewer unique digits
    return len(unique_digits) <= 2

def solutions(S, T):
    # Parse the input time strings into datetime objects
    start_time = datetime.strptime(S, "%H:%M:%S")
    end_time = datetime.strptime(T, "%H:%M:%S")
    
    valid_count = 0
    current_time = start_time
    
    # Loop from start_time to end_time
    while current_time <= end_time:
        time_str = current_time.strftime("%H:%M:%S")
        if is_valid_time(time_str):
            valid_count += 1
        # Increment time by one second
        current_time += timedelta(seconds=1)
    
    return valid_count

# Example usage:
S = "15:15:00"
T = "15:16:12"
print(solutions(S, T))  # Output: 1

S = "22:22:21"
T = "22:22:28"
print(solutions(S, T))  # Output: 3

'''
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def is_valid_time(time_str):
    return len(set(time_str.replace(":", ""))) <= 2

def count_valid_times(S, T):
    start_seconds = time_to_seconds(S)
    end_seconds = time_to_seconds(T)
    
    valid_count = 0
    for current_seconds in range(start_seconds, end_seconds + 1):
        time_str = seconds_to_time(current_seconds)
        if is_valid_time(time_str):
            valid_count += 1
    
    return valid_count

# 사용 예시
S = "15:15:00"
T = "15:16:12"
print(count_valid_times(S, T))  # 출력: 1

S = "22:22:21"
T = "22:22:28"
print(count_valid_times(S, T))  # 출력: 3
'''