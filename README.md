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
```

# Usage

```
usage: transliterator Latin <> Tifinag [-h] [-t TEXT] [-v] [-d DIRECTION] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Source language.
  -v, --interactive     Interactive translator
  -d DIRECTION, --direction DIRECTION
                        1 for latin to tifinagh, 2 for tifinagh to latin
  -i INPUT, --input INPUT
                        Only transliterator Latin to Tifinag
  -o OUTPUT, --output OUTPUT
                        Output path
```

## Interactive mode

This mode opens an interactive panel where given sentence is transliterated. By default it transliterates from latin to tifinagh.

```
python src/main.py -v
```

For transliterating tifinagh to latin specify direction as 2.

```
python src/main.py -v -d 2
```

## Translate sentence-segmented text file

This mode transliterates plain text file, line-by-line.

```
python src/main.py -i test.txt -o test-result.txt
```
