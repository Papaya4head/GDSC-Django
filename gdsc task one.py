#!/usr/bin/env python
# coding: utf-8

# In[10]:


para=str(input('write a para'))
dic={}
def a():
    word=para.split(' ')
    print(word)
    print(type(word))
    return word
word=a()
def b():
    for i in word:
        num=word.count(i)
        dic[i]=num
        print(dic)
    
word=a()
b()
    


# In[24]:


def prompt():
    para=input('enter a paragraph: ')
    return para
def token(para):
    words=para.split()
    return words
def freq(words):
    freq={}
    for word in words:
        if word not in freq:
            freq[word]=0
        freq[word]+=1
    return freq
def display(freq):
    for word,freq in sorted(freq.items(),key=lambda item:item[1],reverse=True):
        print(f'{word}: {freq}')
def ser(word,words):
    freq=words.count(word)
    if freq>0:
        print(f"this word {word} appears {freq} times")
    else:
        print(f'this {word} dose not exist')
para = prompt()
words= freq(para)
freq= display(freq)
    
          
    
    
    
    


# In[16]:


def input_text():
    """Prompts the user to enter a paragraph of text and stores it in a variable."""
    paragraph = input("Please enter a paragraph of text: ")
    return paragraph

def word_tokenization(paragraph):
    """Splits the input text into individual words and stores them in a list."""
    words = paragraph.lower().split()
    return words

def word_frequency_calculation(words):
    """Counts the frequency of each word in the text and stores the frequencies in a dictionary."""
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

def display_word_frequencies(word_frequencies, descending=True, top_n=None):
    """Displays the word frequencies in descending order. Optionally, only displays the top N most frequent words."""
    if descending:
        sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
    else:
        sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1])

    if top_n:
        sorted_word_frequencies = sorted_word_frequencies[:top_n]

    for word, frequency in sorted_word_frequencies:
        print(f"{word}: {frequency}")

def word_search(word, words):
    """Prompts the user to enter a word and searches for it in the text."""
    frequency = words.count(word)
    if frequency > 0:
        print(f"The word '{word}' appears {frequency} times.")
    else:
        print(f"The word '{word}' does not appear in the text.")

# Main program
paragraph = input_text()
words = word_tokenization(paragraph)
word_frequencies = word_frequency_calculation(words)

print("Displaying all word frequencies:")
display_word_frequencies(word_frequencies)

print("\nDisplaying the top 5 most frequent words:")
display_word_frequencies(word_frequencies, top_n=5)

search_word = input("\nEnter a word to search for: ")
word_search(search_word, words)


# In[ ]:





# In[ ]:





# In[ ]:




