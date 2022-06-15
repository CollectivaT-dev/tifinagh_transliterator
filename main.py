import os
import util
import argparse
from tqdm import tqdm

def main():
    
    parser = argparse.ArgumentParser("transliterator Latin <> Tifinag")
    parser.add_argument("-t", "--text", help="Source language.", required=False)
    parser.add_argument("-v", "--interactive", help="Interactive translator", default=False, action='store_true')
    parser.add_argument("-i", "--input", help="Only transliterator Latin to Tifinag", default=None)
    parser.add_argument("-o", "--output", help="Output path", required=False)
    args = parser.parse_args()

    in_text = args.text
    root_file = args.input
    root_transliterate = args.output

    
    if args.interactive:
        print("Enter sentence to transliterar (type 0 to exit):")
        while True:
            in_sent = input()
            if in_sent == '0':
                sys.exit()
            print(util.transliterator(in_sent,2))
    
    
    elif args.input and args.output:
        print("Transliterate text")
        with open(root_file, 'r', encoding="utf-8") as f_in, open(root_transliterate, 'w') as f_out:
            translate_iter = f_in.readlines()
            with tqdm(total=len(translate_iter)) as pbar:
                for l in translate_iter:
                    f_out.write(util.transliterator(l,2))
                    pbar.update(1)
        print("Transliterate text save!")
    
if __name__ == '__main__':
    main()
