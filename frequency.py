import sys
import getopt
import collections


# exercise 3
def counter(data_in):
    # english alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # turn input data to uppercase
    raw_text = data_in.upper()
    # initialize variable
    data_out = '"'
    # find letter frequency
    letters_count = collections.Counter(raw_text)

    for c in alphabet:
        # check if letter is valid
        index = alphabet.find(c)

        # if Character is valid (listed in the alphabet)
        if index != -1:
            # get letter appearances from counter list
            single_letter_count = letters_count[c]
            # append key and value to string
            data_out = data_out + "'" + str(c) + "': " + str(single_letter_count) + ","

    # Return frequencies string
    data_out += '"'
    return data_out


if __name__ == '__main__':
    syntaxShort = "hi:o:"
    syntaxLong = ["help", "input=", "output="]
    # Variables initialization
    in_file = []
    out_file = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], syntaxShort, syntaxLong)
        for option, a in opts:

            if option in ("-h", "--help"):
                print("usage: caesar.py [options]")
                print("short  long        function")
                print(" -h   --help       show this help")
                print(" -i   --input      input filename (text, for example input.txt)")
                print(" -o   --output     output filename (text, for example output.txt)")
                sys.exit()
            elif option in ("-i", "--input"):
                in_file = a
            elif option in ("-o", "--output"):
                out_file = a

        # Open file, read it and load contents to data
        with open(in_file, 'rt') as filein:
            data = filein.read()
        # Call the counter function
        output_data = counter(data)
        # print results to output file
        with open(out_file, 'wt') as fileout:
            fileout.write(output_data)

    except getopt.GetoptError as err:
        print('Error parsing args:', err)
        print('type -h or --help for options')
        sys.exit(1)
    except Exception as e:
        print('Error', e)
        print('type -h or --help for options')
        sys.exit(2)
