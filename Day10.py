# Simple Log Analyzer (Day 10 Project)

logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters
counts = {
    "ERROR": 0,
    "INFO": 0,
    "WARNING": 0
}

# Process logs (ignore case sensitivity)
for log in logs:
    log_upper = log.upper()  # normalize case
    
    if "ERROR" in log_upper:
        counts["ERROR"] += 1
    elif "INFO" in log_upper:
        counts["INFO"] += 1
    elif "WARNING" in log_upper:
        counts["WARNING"] += 1

# Print counts
print("Log Counts:")
for key, value in counts.items():
    print(f"{key}: {value}")

# Bonus: Find most frequent log type
most_frequent = max(counts, key=counts.get)

print("\nMost Frequent Log Type:")
print(f"{most_frequent} ({counts[most_frequent]} times)")