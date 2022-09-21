[![Build Status](https://travis-ci.org/sphoneix22/italian_dictionary.svg?branch=master)](https://travis-ci.org/sphoneix22/italian_dictionary)
[![codecov](https://codecov.io/gh/sphoneix22/italian_dictionary/branch/master/graph/badge.svg)](https://codecov.io/gh/sphoneix22/italian_dictionary)
[![PyPI version](https://badge.fury.io/py/italian-dictionary.svg)](https://badge.fury.io/py/italian-dictionary)
![Python](https://img.shields.io/pypi/pyversions/Django.svg)
![PRS](https://img.shields.io/badge/PRs-Welcome-green.svg)

# ItalianDictionary

This package searches for word meanings on [dizionario-italiano](https://www.dizionario-italiano.it).

## Install

```bash
pip install italian-dictionary
```

## Usage

```python
import italian_dictionary

# Use this to get only the meaning
definition = italian_dictionary.get_definition('cane', limit=3, all_data=False)

#Use this to get all datas of a word (all_data default is True)
datas = italian_dictionary.get_definition('albero')

#For IT-EN Dictionary, replace above method with .get_en_definition()
definition = italian_dictionary.get_en_definition('mangiare', limit=3, all_data=False)
data = italian_dictionary.get_en_definition('albero')

```

#### Complete data response

This function will return a dictionary like this:

```python
{
'sillabe': ['al', 'be', 'ro'],
'lemma': 'àlbero',
'pronuncia': ' /ˈalbero/',
'grammatica': ['sostantivo maschile'],
'definizione': ['pianta con fusto alto, legnoso, provvisto di rami nella parte superiore',
               "MARINERIA --  palo che regge i pennoni con le vele e tutta l'attrezzatura",
               'MECCANICA --  parte rotante, generalmente cilindrica, che, in una macchina, ha la funzione di trasmettere potenza meccanica da un organo a un altro'],
'locuzioni': ["linea d'asse o d'alberi di una nave",
             'ad albero che cade dàgli dàgli',
             'svasare un albero',
             'albero portaelica',
             'albero a calcese',
             'albero castalio',
             'albero matricino',
             'alberi a mezzovento',
             'albero optronico',
             'albero pizzuto',
             'andare agli alberi pizzuti',
             'alberi rinterzati',
             'albero del sego']
}
```

.get_en_definition() will return a dictionary like this:

```python
# Position of word definition should line up with corresponding part of speech position, ex. definition[0] => 'part of speech'[0]
# Definitions will return as strings for 1 def/pos, and lists for 2+ defs/pos

{
'definition': ['reason', ['(affinché) in order that, so that', '(causale) because'], 'why'],
'syllables': ['per', 'chè'],
'lemma': 'perché',
'pronunciation': ' /perˈke/',
'part of speech': ['sostantivo maschile', 'congiunzione', 'avverbio'],
'url': 'https://www.dizionario-inglese.com/dizionario-italiano-inglese.php?parola=perch%C3%A8'
}
```

## Tests

To run tests you need `pytest`
When in project folder:
`python -m pytest`
