# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    '''
    [assignment] Add your code here.
    Let's first remove spaces and
    ensure all entries are converted to lower cases.
    This will take care of variations in user inputs
    when calling the function.
    '''
    word = word.replace(" ", "").lower()
    anagram = anagram.replace(" ", "").lower()

    # Let's sort the arguments/parameters and apply an if-else statement on them

    if sorted(word) != sorted(anagram):
        return False
    else:
        return True

'''
Note that the return statement, unlike the print function
gives back a value, which cannot be seen by the user but can
be used by the computer in further functions.
All functions will return a value and if this is not specified,
the function will return None.


'''
find_anagram("elbow", "below")
find_anagram("supersonic", "percussion")
# print(find_anagram("elbow", "below"))
# print(find_anagram("hello", "check"))
