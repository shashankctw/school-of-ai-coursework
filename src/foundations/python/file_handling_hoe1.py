def count_words_and_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)
            
            
            print(f'Number of words: {word_count}')
            print(f'Number of lines: {line_count}')
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        
count_words_and_lines('sample.txt')