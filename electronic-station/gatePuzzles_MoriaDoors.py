'''
http://www.checkio.org/mission/gate-puzzles/
The Doors of Durin were opened by Gandalf and the Fellowship entered in Moria. 
As they found, this underground kingdom has gates on every passageway. Each gate has a written message which contains the key word. 
Luckily, Gimli knows how to recognize the key in these messages. 
It's the most "like" word, which has the greatest average "likeness" coefficient with other words in the message.

You are given a message. You need to pick out all words (a consecutive sequence of letters or a single letter), 
calculate the "likeness" coefficients with other words, take an average of them and choose the greatest. 
Count "likeness" coefficient even for the same words (of course it's 100). 
If several words have the same resulting value, then choose the word closest to the end of the message. 
Words in the message can be separated by whitespaces and punctuation. There are no numbers.

"Likeness" coefficient for two words is measured in percentages using the following rules:
- Letter case does not matter ("A" == "a");
- If the first letters of the words are equal, then add 10%;
- If the last letters of the words are equal, then add 10%;
- Add length comparison as 
(length_of_word1 / length_of_word2) * 30%, if length_of_word1 <= length_of_word2, else (length_of_word2 / length_of_word1) * 30%
- Take all unique letters from the both words in one set and count how many letters appear in the both words. 
Add to the coefficient (common_letter_number / unique_letters_numbers) * 50;

So the maximum coefficient of likeness is 100%. For example: for the words "Bread" and "Beard". The result should be given in the lower case.

Let's look at an example. The message "Friend Fred and friend Ted." 
First, pick out words - ("friend", "fred", "and", "friend", "ted"). 
Next we calculate "likeness" for the first word with other. "friend" and "fred" have the same first and last letters, so add 20. 
Then length comparison: the length of "fred" is lesser than "friend", so add (4/6)*30=20. 
The last rule: for these words unique letters are "definr" and the intersected letters are "defr". 
So add (4/6)*50 = 33.333. And the summary is 73.333.
This way we will count all other coefficients and get the following table (results are rounded just for simplicity). 
The greatest average is 62.976 and the result is "friend".

        | friend  | fred    | and     | friend  | ted     |
--------|---------|---------|---------|---------|---------|
friend  | ------  | 73.333  | 39.286  | 100.0   | 39.286  |
fred    | 73.333  | ------  | 40.833  | 73.333  | 52.5    |
and     | 39.286  | 40.833  | ------  | 39.286  | 50.0    |
friend  | 100.0   | 73.333  | 39.286  | ------  | 39.286  |
ted     | 39.286  | 52.5    | 50.0    | 39.286  | ------  |
--------|---------|---------|---------|---------|---------|
sum     | 251.905 | 239.999 | 169.405 | 251.905 | 181.072 |
average | 62.976  | 60      | 42.351  | 62.976  | 45.268  |

Input: A message as a string (unicode)
Output: The keyword as a string.

How it is used: This is a fabricated algorithm which can be modified and be used for linguistic research and text pattern recognition.
Precondition: 0 < len(message); all(x in (string.ascii_letters + string.punctuation + " ") for x in message)
'''
import re

def calculate_likeness(word1, word2):
    if word1 == word2: return 100
    else:
        likeness = 0
        if word1[0] == word2[0]: likeness += 10
        if word1[-1] == word2[-1]: likeness += 10
        if len(word1) <= len(word2): likeness += 30 * len(word1) / len(word2)
        else: likeness += 30 * len(word2) / len(word1)
        
        word1 = set(word1)
        word2 = set(word2)
        likeness += 50 * len(word1.intersection(word2))/len(word1.union(word2))
        
        return likeness

def average(word, words):
    return sum([calculate_likeness(word, x) for x in words]) / len(words)

def find_word(message):
    message = re.findall('(\w+)', message)[::-1]
    words = [i.lower() for i in message]
    return max(words, key=lambda i: average(i, words))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert find_word("Friend Fred and friend Ted.") == "friend"

    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"