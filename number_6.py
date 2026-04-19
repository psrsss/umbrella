"""Task number 6"""


def read_file():
    """Reads my file"""
    with open('Car.txt', 'r', encoding='utf-8') as file:
        return file.read()


R = read_file()


def write_to_file(text):
    """Writes in my file"""
    with open('Car.txt', 'a', encoding='utf-8') as file:
        file.write(text)


write_to_file("\nThis text will be in Car.txt")
print(R)


def get_file_stats():
    """Gets stats in my file"""
    try:
        with open('Car.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            full_text = "".join(lines)
            word_count = len(full_text.split())
            letter_count = sum(c.isalpha() for c in full_text)
            return line_count, word_count, letter_count
    except FileNotFoundError:
        return "File Car.txt not found", 0, 0


lines_count, words_count, letters_count = get_file_stats()
print(f"Lines: {lines_count}, Words: {words_count}, Letters: {letters_count}")
