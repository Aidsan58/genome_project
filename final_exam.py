# f = open('D:/Programs/Python Programs/Python for Genomics/dna.example.fasta')

def header_count(filename):
    """ Finds the number of headers in a sequence. """
    count = 0
    with open(filename, 'r') as f :
        for line in f :
            if line.startswith('>') :
                count += 1
    
    return print('The total number of headers in the file is ' + str(count) + ".")

def sequence_length(filename):
    """ Finds the longest DNA sequence, and the shortest DNA sequence. """
    current_sequence = ''
    longest_sequence = 0
    shortest_sequence = 2300000
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if len(current_sequence) > longest_sequence:
                    longest_sequence = len(current_sequence)
                if len(current_sequence) > 0:
                    if len(current_sequence) < shortest_sequence:
                        shortest_sequence = len(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line.strip()

        if len(current_sequence) > longest_sequence:
            longest_sequence = len(current_sequence)
            
        if len(current_sequence) < shortest_sequence:
            shortest_sequence = len(current_sequence)
            

        
    return print('The longest sequence has a length of ' + str(longest_sequence) + '. The shortest sequence has a length of ' + str(shortest_sequence) + '.')


file_path = 'D:/Programs/Python Programs/Python for Genomics/dna.example.fasta'

header_count(file_path)

sequence_length(file_path)
