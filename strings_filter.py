# inputs
strings = ["solve me", "lol hello there", "solve mez", "solve not me", "match solve me l", "solve mE ", "hi lol there"]
blocklist = ["lol", "solve me", "match me"]

"""
return True if block_word exists in data in order.
detect(["match", "solve", "me", "l"], ["solve", "me"]) returns true

d: max number of words in data
b: max number of words in block_word
Time Complexity: O(d*b)
Space Complexity: O(len(b)*d) this is for slicing
"""
def detect(data, block_word):
    if len(data) < len(block_word):
        return False
    i = 0
    while i < len(data):
        if data[i:i+len(block_word)] == block_word:
            return True
        i += 1
    return False
    
print(detect(["match", "solve", "me", "l"], ["solve", "me"]))
print(detect(["hi", "lol", "there"], ["lol"]))

"""
S: number of strings in strings
B: number of strings in blocklist
Time Complexity: O(S*B * d*b)
Space Complexity: O(S+B + len(b)*d)
"""
def solver(strings, blocklist):
    lst_data = []
    for s in strings:
        words = s.split(' ')
        words = [w.lower() for w in words]
        lst_data.append(words)
        
    lst_block_word = []
    for b in blocklist:
        words = b.split(' ')
        words = [w.lower() for w in words]
        lst_block_word.append(b.split(' '))

    output = []
    for data in lst_data:
        is_found = False
        for block_word in lst_block_word:
            if detect(data, block_word):
                is_found = True
                break
        if not is_found:
            output.append(' '.join(data))
    return output
    
print(solver(strings, blocklist))
# output: ['solve mez', 'solve not me']
