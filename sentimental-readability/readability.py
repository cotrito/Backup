from cs50 import get_string
import sys

def main():
    try:
        text = get_string("text : ")
        le = count_letters(text)
        #print(f"total characters {le}")
        wo = count_words(text)
        #print(f"total words {wo}")
        se = count_sentenses(text)
        #print(f"total sentenses {se}")
        l = le/wo * 100
        s = se/wo * 100
        index = round(0.0588 * l - 0.296 * s - 15.8)
        #print(f"score: {index}")
        if (index < 1):
            print("Before Grade 1")
        elif(index > 15):
            print("Grade 16+")
        else:
            print(f"Grade {index}")
    except ValueError:
        sys.exit(1)


def count_letters(text):
    valid_chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ttl_le = 0
    for l in text :
        if l.lower() in valid_chars :
            ttl_le += 1
    return ttl_le


def count_words(text):
    valid_chars =[' ']
    ttl_wo = 1
    for l in text :
        if l.lower() in valid_chars :
            ttl_wo += 1
    return ttl_wo

def count_sentenses(text):
    valid_chars =['.','!','?']
    ttl_se = 0
    for l in text :
        if l.lower() in valid_chars :
            ttl_se += 1
    return ttl_se


main()
