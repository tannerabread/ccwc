def count_file(file, byte_count, line_count, word_count, char_count):
    if not byte_count and not line_count and not word_count and not char_count:
        lines = get_lines(file)
        words = get_words(file)
        bytes = get_byte_count(file)

        print(f"{lines} {words} {bytes} {file}")
        return
    try:
        if byte_count:
            byte_count = get_byte_count(file)
            print(f"{len(byte_count)} {file}")
        if line_count:
            lines = get_lines(file)
            print(f"{len(lines)} {file}")
        if word_count:
            words = get_words(file)
            print(f"{len(words)} {file}")
        if char_count:
            chars = get_chars(file)
            print(f"{chars} {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")

def get_byte_count(file):
    with open(file, 'rb') as open_file:
        text = open_file.read()
        return len(text)

def get_lines(file):
    with open(file, 'r') as open_file:
        lines = open_file.readlines()
        return len(lines)
    
def get_words(file):
    with open(file, 'r') as open_file:
        words = open_file.read().split()
        return len(words)
    
def get_chars(file):
    with open(file, 'r') as open_file:
        lines = open_file.read()
        chars = 0
        for line in lines:
            chars += len(line.split('\n'))
        return chars
    
