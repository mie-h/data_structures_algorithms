


"""TC: O(n) SC: O(n)"""
def reverse_string(s):
    return s[::-1]

"""TC: O(n) SC: O(n)"""
def reverse_string2(s):
    output = []
    for i in range(len(s)-1, -1, -1):
        output.append(s[i])
    return "".join(output)


def main():
    s = "abcde"
    print(reverse_string(s))
    print(reverse_string2(s))

if __name__ == "__main__":
    main()
