 # asks the user for text
user_text = input("Enter a text/article/paragraph/sentence/ or poem: ").lower()

# asks the user to give three random letters
letter1 = input("Give me a random letter: ").lower()
letter2 = input("Give me a second letter: ").lower()
letter3 = input("Give me a third letter: ").lower()
print("------------")

# Step 1: Number of times each of those letters chose have appeared
letter_count1 = user_text.lower().count(letter1)
letter_count2 = user_text.lower().count(letter2)
letter_count3 = user_text.lower().count(letter3)
print("Number of times '" + letter1 + "' appears: " + str(letter_count1))
print("Number of times '" + letter2 + "' appears: " + str(letter_count2))
print("Number of times '" + letter3 + "' appears: " + str(letter_count3))
print("------------")

# Step 2: The number of words there are in the whole text
word_list = user_text.split() # word_list splits the text the user gave into seperate words
word_count = len(word_list) # word_count then counts the amount of words in word_list
print("The number of words in the text: " + str(word_count))

# Step 3: Find what the first and last letters of the text are
first_letter = user_text[0] # This finds what the first letter of the text is
last_letter = user_text[-1] # This finds what the last letter of the text is
print("The first letter of the text is: " + first_letter)
print("The last letter of the text is: " + last_letter)
print("------------")

# Step 4: Invert the order of the words of the text
inverted_word_list = word_list[::-1] # This inverts the text
inverted_text = ' '.join(inverted_word_list) # This joins all of the words with spaces from the inverted text
print("The inverted order of the text: " + inverted_text)
print("------------")

# Step 5: Find if the word "python" is inside the text
contains_python = "python" in user_text.lower()
python_true_false = {
    True: "The text contains the word 'python'.",
    False: "The text does not contain the word 'python'."
}
print(python_true_false[contains_python])