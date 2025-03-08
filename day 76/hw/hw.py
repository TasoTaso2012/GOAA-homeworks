#1
def find_largest(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

largest_number = find_largest(10, 20, 15)
print('tthe largest number is:', largest_number)



#2
def count_vowels(word):
    count = 0
    vowels = 'aeiou'
    word = word.lower()  
    for i in range(len(word)):

        if word[i] in vowels:
            count += 1

    return count



word = "taso"
vowel_count = count_vowels(word)
print('the numbr of vowels in "' + word + '" is: ' + str(vowel_count))


#3
def palindrome(word):
    word = word.lower()  
    return word == word[::-1]  


word1 = "racecar"
word2 = "hello"
print('Is "' + word1 + '" a palindrome? ' + str(palindrome(word1)))
print('Is "' + word2 + '" a palindrome? ' + str(palindrome(word2)))



#4
def reverse(t):
    return t[::-1]


str = "taso"
reversed_string = reverse(str)
print('the reverse of "' + str + '" is: "' + reversed_string + '"')



#5
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


sentence = "im writin my hw in python"
longest_word = find_longest_word(sentence)
print('The longest word  is:', longest_word) 