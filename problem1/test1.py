s = input("Enter a string: ")  # Taking input from the user
New = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in New:
        New.remove(s[left])
        left += 1
    New.add(s[right])
    max_length = max(max_length, right - left + 1)

print("Length of the longest substring without repeating characters:", max_length)