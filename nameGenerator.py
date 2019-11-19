#!/bin/bash/env python
import argparse, random, os, sys

class Options:
    '''
    Class representing options for name generator program. Contains default
    values for initialization without arguments.
    '''
    def __init__(self, type='basic', length=random.randint(2,3), numbers=False):
        self.type = type
        self.length = length
        self.numbers = numbers

def optionsParse(args):
    '''
    Parses the arguments and returns an options object representing
    the configuration options for the script.
    '''
    options = Options()
    # parse name type
    types = ['camel', 'snake', 'l33t', 'basic']
    if args.type and args.type in types:
        print(args.type)
        options.type = args.type
    # parse name length
    if args.length:
        options.length = args.length
    # parse numbers
    if args.numbers:
        options.numbers = True

    return options

def importWordLists():
    '''
    Make a big list of all words from our wordlist files. 
    TODO: find a way to do it that wont murder our memory
    '''
    big_list = []
    wordlists = os.listdir('wordlists')
    for wordlist in wordlists:
        if os.path.isfile(os.path.join('wordlists/', wordlist)):
            with open(os.path.join('wordlists/', wordlist)) as wl:
                for line in wl:
                    big_list.append(line.lower().strip())
    return big_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random username.')
    parser.add_argument('-l', '--length', type=int,
                        help='Specify the word length for username (default: 2-3)')
    parser.add_argument('-t', '--type', type=str,
                        help='Specify a name type to generate (default: random selection of type)')
    parser.add_argument('-n', '--numbers', action="store_true",
                        help="Switch to add numeric values to the username")

    args = parser.parse_args()
    random.seed(int.from_bytes(os.urandom(4), sys.byteorder))

    # parse out the arguments
    options = optionsParse(args)
    big_list = importWordLists()
    leet_map = {'a':'@','e':'3','l':'1','o':'0','s':'$'};

    username = ''
    for x in range(options.length):
        word = random.choice(big_list)
        if options.type == 'camel':
            word = word[0].upper() + word[1:]
        elif options.type == 'snake':
            if x < options.length - 1:
                word = word + '_'
        elif options.type == 'l33t':
            for key in leet_map.keys():
                word = word.replace(key, leet_map[key])
        
        username = username + word

    if options.numbers:
        number = random.randint(1,100)
        username = username + str(number)

    print(username)

