# f = open('D:/Programs/Python Programs/Python for Genomics/dna.example.fasta')

def header_count(filename):
    """ Finds the number of headers in a sequence. """
    count = 0
    with open(filename, 'r') as f :
        for line in f :
            if line.startswith('>') :
                count += 1
    
    return print('The total number of headers in the file is ' + str(count) + ".")

def longest_sequence(filename):
    """ Finds the longest DNA sequence. """
    current_sequence = ''
    longest_sequence = 0
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if len(current_sequence) > longest_sequence:
                    longest_sequence = len(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line.strip()

        if len(current_sequence) > longest_sequence:
            longest_sequence = len(current_sequence)

        
    return print('The longest sequence has a length of ' + str(longest_sequence) + '.')


file_path = 'D:/Programs/Python Programs/Python for Genomics/dna.example.fasta'

header_count(file_path)

longest_sequence(file_path)
