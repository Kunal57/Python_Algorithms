# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

def findWords(words):
  """
  :type words: List[str]
  :rtype: List[str]
  """
  row1 = "qwertyuiop"
  row2 = "asdfghjkl"
  row3 = "zxcvbnm"

  newWordList = words[:]

  for word in words:
    if word[0].lower() in row1:
      for letter in word:
        if letter.lower() not in row1:
          newWordList.remove(word)
          break
    if word[0].lower() in row2:
      for letter in word:
        if letter.lower() not in row2:
          newWordList.remove(word)
          break
    if word[0].lower() in row3:
      for letter in word:
        if letter.lower() not in row3:
          newWordList.remove(word)
          break
  return newWordList




words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))