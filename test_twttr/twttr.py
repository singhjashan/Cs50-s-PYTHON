##

def main():
    txt = input("Text: ")
    print(shorten(txt))


def shorten(word):
    word_without_vowels = ""

    for lttr in word :
        if not lttr.lower() in ['a','e','i','o','u'] :
            word_without_vowels += lttr

    return word_without_vowels


if __name__ == "__main__":
    main()
