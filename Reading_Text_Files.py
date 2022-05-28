# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
# N.B. for this script to work, please ensure the story.txt file
# is in thesame directory level as this python script.

def read_file_content(filename):
    # [assignment] Add your code here
    with open("story.txt", "r") as f:
        contents = f.read()


    return contents

# End of first function call
print("++++" * 20)

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here

    # Remove punctuations (, ? .)
    text = text.replace(',', '')

    text = text.replace('?', '')

    text = text.replace('.', '')
    #print(text)

    # Remove empty spaces. The split function splits
    # a string into a list where each word is a list item
    list_of_words = text.split(" ")

    # End of string manipulations. See the final words
    print(text)
    print("++++" * 20)

    # Create an empty dictionary to contain
    # the word and its count (word:count) as key:value pairs
    text_dict = {}

    # Use a list comprehension to iterate through the list_of_words
    # Use the count method on the list_of_words and then
    # assign a variable word_freq to the outcome of the count.
    # Finally use the zip function to create a dictionary
    # and print/return the result

    word_freq = [list_of_words.count(word) for word in list_of_words]
    text_dict = dict(zip(list_of_words, word_freq))
    return text_dict
    #print(text_dict)


 ### Run Script ###
read_file_content('story.txt')
count_words()
