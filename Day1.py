def clean_and_sort(lst):
    seen = set()
    result = []

    for item in lst:
        if item is not None and item != "" and item not in seen:
            seen.add(item)
            result.append(item)        

    return sorted(result)
lst = ["apple", "banana", None, "apple", "", "orange", "banana"]
cleaned_sorted_lst = clean_and_sort(lst)
print(cleaned_sorted_lst)