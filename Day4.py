# Given logs
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters
error_count = 0
info_count = 0
warning_count = 0

# Dictionary to store counts
log_counts = {}

# Process logs
for log in logs:
    # Convert to lowercase (ignore case sensitivity)
    log_lower = log.lower()
    
    if "error" in log_lower:
        error_count += 1
        log_counts["ERROR"] = log_counts.get("ERROR", 0) + 1
        
    elif "info" in log_lower:
        info_count += 1
        log_counts["INFO"] = log_counts.get("INFO", 0) + 1
        
    elif "warning" in log_lower:
        warning_count += 1
        log_counts["WARNING"] = log_counts.get("WARNING", 0) + 1

# Print counts
print("Log Counts:")
print("ERROR:", error_count)
print("INFO:", info_count)
print("WARNING:", warning_count)

# Find most frequent log type
most_frequent = max(log_counts, key=log_counts.get)

print("\nMost Frequent Log Type:", most_frequent)