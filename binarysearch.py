def binary_search(haystack, needle, start=0, end=-1):
    if end == -1:
        end = len(haystack)
    
    if len(haystack) == 1:
        return -1 if needle != haystack[0] else start - 1
    
    centre = len(haystack)//2-1

    if abs(haystack[centre]-needle) < abs(haystack[centre + 1]-needle):
        # left
        return binary_search(haystack[0:centre+1], needle, start, centre+start)
    else:
        # right
        return binary_search(haystack[centre+1:len(haystack)], needle, start+centre+1, end)

print(binary_search(range(10000000), 5094869))
