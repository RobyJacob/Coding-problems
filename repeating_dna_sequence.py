import sys

def repeating_sequence(seq, l):
    # get distinct letters from the sequence
    distinct_letters = set(seq)

    # assign a value to each distinct letter
    letter_encode = {letter: index+1 for index, letter in enumerate(distinct_letters)}

    # keeps track of current hash value
    curr_hash = 0

    # output stores the repeating_sequence and visited keeps track of seen hash values or sequences
    output, visited = [], []

    # find the hash value of first l letter sequence
    for i, letter in enumerate(seq[:l]):
        curr_hash += letter_encode[letter] * (2 ** (i+1))

    visited.append(curr_hash)

    # loop through the sequence with l letter long window skipping the first letter, computing hash values for each sequence using rolling hash method
    for i in range(1, len(seq)-l+1):

        # get the next sequence from the window
        curr_seq = seq[i:i+l]

        # remove the value for previous letter from current hash
        curr_hash -= letter_encode[seq[i-1]] * 2

        # scale current hash downn to accomodate new letter
        curr_hash /= 2

        # compute the value for new letter
        curr_hash += letter_encode[curr_seq[-1]] * (2 ** l)

        # add current hash value to visited if not seen before
        # if seen before then add it to the output
        if curr_hash in visited:
            output.append(curr_seq)
        else:
            visited.append(curr_hash)

    # return the output of repeating_sequences
    return output

def main():
    if len(sys.argv) < 3:
        print("Provide length of sequence and the sequence without space")
        sys.exit(1)

    length = int(sys.argv[1])
    sequence = sys.argv[2]

    print(repeating_sequence(sequence, length))

if __name__ == "__main__":
    main()
