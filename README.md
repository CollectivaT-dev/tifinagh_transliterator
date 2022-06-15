# tifinagh transliterator


# Installation

In order to clone this repository:
```
git clone https://github.com/CollectivaT-dev/tifinagh_transliterator
```

After, create a virtualenvironment and install all the requirements
```
python -m venv venv
source venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

# Usage

```
usage:  transliterator Latin <> Tifinag [-h] -d LAD_DIC [-i INPUT]
                                                   [-o OUTPUT] [-v] [-c]
required arguments:

  -h, --help            show help message and exit

  -i INPUT, --input INPUT
                        Sentence segmented text file to transliterate
  -o OUTPUT, --output OUTPUT
                        Output path
  -v, --interactive     Interactive transliterator
```

## Interactive mode

This mode opens an interactive panel where given sentence is translated. 

```
python main.py -v
```

## Translate sentence-segmented text file

This mode translates plain text file, line-by-line.

```
python main.py -i text.txt -o resultado/resultado.txt
```
