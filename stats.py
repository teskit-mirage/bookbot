def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def get_num_words(text):

    words = text.split()

    return len(words)

def get_character_count(text):

    char_counts = dict()

    text = text.lower()

    for char in text:
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_counts(char_counts):

    sorted_counts = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_counts.append({"char": char, "num": count})

    sorted_counts.sort(key=lambda x: x["num"], reverse=True)

    return sorted_counts