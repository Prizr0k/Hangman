pi = 3.141592653589793
print(round(pi, 5))
# put your python code here

def contains(text, pattern):
    for i in range(len(text) - len(pattern)):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False

print(contains("0110110", "111"))
