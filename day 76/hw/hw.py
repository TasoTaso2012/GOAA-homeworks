#1
def find_largest(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

largest_number = find_largest(10, 20, 15)
print('The largest number is:', largest_number)

#2
def count_vowels(word):
    count = 0
    vowels = 'aeiou'
    word = word.lower()  
    for i in range(len(word)):

        if word[i] in vowels:
            count += 1

    return count


word = "Hello World"
vowel_count = count_vowels(word)
print('The number of vowels in "' + word + '" is: ' + str(vowel_count))