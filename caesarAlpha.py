import sys
import getopt


# exercise 2
def main(data_in, key_, mode_, custom_alphabet):
    global new_index
    # load custom alphabet
    alphabet = custom_alphabet
    # initialize variable
    data_out = ''
    # turn input data to lowercase
    data_in = data_in.lower()

    for c in data_in:

        # find character position
        index = alphabet.find(c)

        if index == -1:
            # if Character is not listed in the alphabet, return char
            data_out += c
        else:
            # find the shift based on mode and key
            if mode_ == 'enc':
                new_index = index + key_
            elif mode_ == 'dec':
                new_index = index - key_

            # find the shifted char position
            new_index %= len(alphabet)
            # append new char to string
            data_out += alphabet[new_index:new_index + 1]
    # Return the encrypted/decrypted text
    return data_out


if __name__ == '__main__':
    syntaxShort = "hi:o:k:a:m:"
    syntaxLong = ["help", "input=", "output=", "key=", "alphabet=", "mode="]
    # Variables initialization
    in_file = []
    out_file = []
    key = []
    alphabetFile = []
    mode = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], syntaxShort, syntaxLong)
        for option, a in opts:

            if option in ("-h", "--help"):
                print("usage: caesarAlpha.py [options]")
                print("short  long        function")
                print(" -h   --help       show this help")
                print(" -i   --input      input filename (text, for example input.txt)")
                print(" -o   --output     output filename (text, for example output.txt)")
                print(" -k   --key        encryption key to use (integer)")
                print(" -a   --alphabet   custom alphabet filename (text, for example alphabet.csv)")
                print(" -m   --mode       function mode. Type 'enc' for encryption mode")
                print("                                  Type 'dec' for decryption mode")
                sys.exit()
            elif option in ("-i", "--input"):
                in_file = a
            elif option in ("-o", "--output"):
                out_file = a
            elif option in ("-k", "--key"):
                key = int(a)
            elif option in ("-a", "--alphabet"):
                alphabetFile = a
            elif option in ("-m", "--mode"):
                mode = str(a)

        # Open file, read it and load contents to data
        with open(in_file, 'rt') as filein:
            data = filein.read()
        # Read alphabet file
        with open(alphabetFile, 'rt') as csvfile:
            raw_data = csvfile.read()
            # variable init
            alpha = []
            # remove most common csv delimiter chars like (;) and (,)
            if raw_data.find(";") != -1:
                alpha = raw_data.replace(";", "")
            elif raw_data.find(",") != -1:
                alpha = raw_data.replace(",", "")

        # Call the encryption/decryption function
        new_data = main(data, key, mode, alpha)
        # print results to output file
        with open(out_file, 'wt') as fileout:
            fileout.write(new_data)

    except getopt.GetoptError as err:
        print('Error parsing args:', err)
        print('type -h or --help for options')
        sys.exit(1)
    except Exception as e:
        print('Error', e)
        print('type -h or --help for options')
        sys.exit(2)
