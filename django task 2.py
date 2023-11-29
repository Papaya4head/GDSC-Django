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
def display_word_frequencies(word_frequencies, top_n=None):
    """Displays the word frequencies in descending order. Optionally, only displays the top N most frequent words."""
    sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)

    sorted_word_frequencies = sorted_word_frequencies[:top_n]

    for word, frequency in sorted_word_frequencies:
        print(f"{word}: {frequency}")
Para=prompt()
Words=token(Para)
freq=freq(Words)

print('disiplaying all freq :')
display(freq)

search_word = input("\nEnter a word to search for: ")
ser(search_word,Words)

N=int(input("enter the number of most used words you want: "))
print("\nDisplaying the top  most frequent words:")
display_word_frequencies(freq, top_n=N)
