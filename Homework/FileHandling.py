#Read the file and remove equal lines (if any).
def remove_equal_lines(file_path):
    with open(file_path, 'r') as file:
        lines=file.readlines()

    unique_lines = set(line.strip() for line in lines)

    with open(file_path, 'w') as file:
        for line in sorted(unique_lines):
            file.write(f'{line}\n')

remove_equal_lines('TestFile.txt')

#Print out all words with length of n-characters
def print_n_length_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        for word in words:
            word_to_print = ''.join(char for char in word )
            if len(word_to_print) == n:
                print(word_to_print)

print_n_length_words('TestFile.txt', 3)

#Combine two files into a third file
def combine_two_files(file1, file2, output_file):
    with open(file1, 'r') as f1:
        data1 = f1.read()

    with open(file2, 'r') as f2:
        data2 = f2.read()

    with open(output_file, 'w') as f_output:
        f_output.write(data1 + "\n" + data2)

combine_two_files('TestFile.txt', 'TestFile2.txt', 'FinalFile.txt')