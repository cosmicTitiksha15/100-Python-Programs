# Count the total words inside a paragraph of text.

def count_words(paragraph):
    words = paragraph.split(" ")
    total_words = len(words)
    return total_words


paragraph = input("Enter a paragraph of text: ").strip()
total_words = count_words(paragraph)
print(f"Total words in the paragraph: {total_words}")