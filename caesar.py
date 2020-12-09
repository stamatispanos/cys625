import sys
import getopt


# exercise 1
def main(data_in, key_, mode_):
    global new_index
    # english alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
    # Return the encrypted/decrypted string
    return data_out


if __name__ == '__main__':
    syntaxShort = "hi:o:k:m:"
    syntaxLong = ["help", "input=", "output=", "key=", "mode="]
    # Variables initialization
    in_file = []
    out_file = []
    key = []
    mode = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], syntaxShort, syntaxLong)
        for option, a in opts:

            if option in ("-h", "--help"):
                print("usage: caesar.py [options]")
                print("short  long        function")
                print(" -h   --help       show this help")
                print(" -i   --input      input filename (text, for example input.txt)")
                print(" -o   --output     output filename (text, for example output.txt)")
                print(" -k   --key        encryption key to use (integer)")
                print(" -m   --mode       function mode. Type 'enc' for encryption mode")
                print("                                  Type 'dec' for decryption mode")
                sys.exit()
            elif option in ("-i", "--input"):
                in_file = a
            elif option in ("-o", "--output"):
                out_file = a
            elif option in ("-k", "--key"):
                key = int(a)
            elif option in ("-m", "--mode"):
                mode = str(a)

        # Open file, read it and load contents to data
        with open(in_file, 'rt') as filein:
            data = filein.read()
        # Call the encryption/decryption function
        output_data = main(data, key, mode)
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
