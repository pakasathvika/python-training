def compress_string(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            result+=(s[i] + str(count))
            count = 1

    result+=(s[-1] + str(count))  # Append the last group

    return result
# Example
a = "aaabbaaaaddd"
compressed_string = compress_string(a)
print(compressed_string)  # Output: a3b2a4d2
