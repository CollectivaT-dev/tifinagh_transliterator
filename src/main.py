import os
from util import latin_to_tifinagh, tifinagh_to_latin
import argparse
from tqdm import tqdm
import sys

def main():
    
    parser = argparse.ArgumentParser("transliterator Latin <> Tifinag")
    parser.add_argument("-t", "--text", help="Source language.", required=False)
    parser.add_argument("-v", "--interactive", help="Interactive translator", default=False, action='store_true')
    parser.add_argument("-d", "--direction", help="1 for latin to tifinagh, 2 for tifinagh to latin", default="1")
    parser.add_argument("-i", "--input", help="Only transliterator Latin to Tifinag", default=None)
    parser.add_argument("-o", "--output", help="Output path", required=False)
    args = parser.parse_args()

    in_text = args.text
    root_file = args.input
    root_transliterate = args.output
    direction = args.direction

    if direction == "1":
        transliterator = lambda x: latin_to_tifinagh(x)
    elif direction == "2":
        transliterator = lambda x: tifinagh_to_latin(x)
    else:
        print("ERROR: Direction needs to be 1 or 2")
        sys.exit()
    
    if args.interactive:
        print("Enter sentence to transliterate (type 0 to exit):")
        while True:
            in_sent = input()
            if not in_sent:
                sys.exit()

            print(transliterator(in_sent))
    
    
    elif args.input and args.output:
        print("Transliterate text")
        with open(root_file, 'r', encoding="utf-8") as f_in, open(root_transliterate, 'w') as f_out:
            translate_iter = f_in.readlines()
            with tqdm(total=len(translate_iter)) as pbar:
                for l in translate_iter:
                    f_out.write(transliterator(l))
                    pbar.update(1)
        print("Transliterate text save!")
    
if __name__ == '__main__':
    main()
