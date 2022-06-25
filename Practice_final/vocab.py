# Description
# Processing large data with a computer is very useful, requiring converting real-world data into a numerical
# form that can be processed by computer. For example, human language cannot be processed directly since
# words (strings) are not computable. Thus, we need to encode text to numbers. Assuming we have a dictionary
# recording which word should be encoded to which number, e.g. {'i': 1, 'like': 2, 'python': 3}, then text
# 'i like python' can be encoded to [1, 2, 3], which is a list of numbers, and the i-th number in the list is the number encoded from the i-th word in the text.
#
# Here you need to write a Vocabulary class and implement the following functions: <br>
# \__init\__(self, filepath): <br>
# This function takes a filepath as an argument. You need to open the file, which contains some text.
# Then you need to build the dictionary using the text in the file.
# Follow this tutorial to build the dictionary: <br>
# (1) Initialize the dictionary as {'< unk\>': 1}. < unk\> is a special word to refer to a word that doesn't exist in the text in the file. <br>
# (2) For every line in the file, split it by space. This shall convert each line of text into a list of words. <br>
# (3) Loop over the list of words you get from (2), for every word, first convert it to lower case. Then if a word is already in the dictionary, don't make any change. If however a word is not in the dictionary, you need to add it to the dictionary and set the corresponding number to the
# length of the dictionary after adding the new word. <br>
# e.g. If the dictionary is {'< unk\>': 1}, and the first line you are looping is ['The', 'more', 'the', 'better', '.'],
# When you go to 'The', convert it to 'the', since it's not in dictionary, you add it to dictionary and get {'< unk\>':1, 'the':2}
# Then you go to 'more', add it to dictionary and get {'< unk\>':1, 'the':2, 'more':3}
# The you go to 'the', it's already in the dictionary, pass.
# ... After looping over this line, the dictionary is {'< unk\>':1, 'the':2, 'more':3, 'better':4, '.':5}
# You need to loop over all the lines in file, and finally get a complete dictionary that maps words on to indices.
#
# index(self, word): <br>
# This function takes a word (string) as argument, and returns the number that this word should be encoded to.
# If this word in not in the dictionary, return the corresponding number for '< unk\>'.
#
# encode_text(self, text): <br>
# This function takes a sentence (string) as argument, you need to encode it as follow: <br>
# (1) split the text by space to get a list of words. <br>
# (2) return a list of numbers, with the i-th number in the list is the encoded number for the i-th word in list (provided the word has not already been encoded).
#
# decode_index(self, index): <br>
# This function takes a list of number as argument (called index), you need to decode it to a sentence as follow: <br>
# (1) The i-th word in the sentence is the i-th number in the index list. <br>
# (2) This function should return one string (the sentence), with individual words separated by one blank space. E.g. 'this is good'.

# Examples:
# \> voc = Vocabulary('corpus.txt') <br>
# \> {'<unk>': 1, 'this': 2, 'sentence': 3, 'is': 4, 'for': 5, 'you': 6, 'to': 7, 'test': 8, ',': 9, 'can': 10, 'check': 11, 'if': 12, 'your': 13, 'words': 14, 'the': 15, 'same': 16, 'as': 17, 'in': 18, 'example': 19, '.': 20, ...} <br>
# The length of your dictionary should be 533. In the example above, only first few entries of the dictionary are shown. <br>
# \> print(voc.index('I'), voc.index('in'), voc.index('Indiana')) <br>
# \> 82 18 1 <br>
# \> print(voc.encode_text('This sentence is irrelevant to the corpus .')) <br>
# \> [2, 3, 4, 1, 7, 15, 1, 20] <br>
# \> print(voc.decode_index([2, 3, 4, 1, 7, 15, 1, 20])) <br>
# \> 'this sentence is < unk\> to the < unk\> .' <br>
# \> print(voc.encode_text('who ruled the country of normandy ?')) <br>
# \> [398, 526, 15, 509, 48, 70, 511] <br>
# \> print(voc.decode_index([398, 526, 15, 509, 48, 70, 511])) <br>
# \> 'who ruled the country of normandy ?' <br>
# \> print(voc.encode_text('there are too many words not in the corpus , we need to expand our data .')) <br>
# \> [293, 89, 1, 254, 14, 310, 18, 15, 1, 9, 1, 1, 7, 1, 1, 1, 20] <br>
# \> print(voc.decode_index([117, 15, 118])) <br>
# \> 'william the conqueror'

special_word = '<unk>'
class Vocabulary:
    def __init__(self, filepath):
        ###
        ### YOUR CODE HERE
        ###

    def index(self, word):
        ###
        ### YOUR CODE HERE
        ###

    def encode_text(self, text):
        ###
        ### YOUR CODE HERE
        ###

    def decode_index(self, index):
        ###
        ### YOUR CODE HERE
        ###
