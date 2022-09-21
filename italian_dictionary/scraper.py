import bs4
import urllib.request as request
from urllib import parse

from italian_dictionary import exceptions

URL = "https://www.dizionario-inglese.com/dizionario-italiano-inglese.php?parola={}"


def build_url(base_url):
    scheme, netloc, path, query, fragment = parse.urlsplit(base_url)
    query = parse.quote(query, safe="?=/")
    return parse.urlunsplit((scheme, netloc, path, query, fragment))  # replacing special characters


def get_soup(url):
    sauce = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, 'html.parser')
    return soup


def get_lemma(soup):
    lemma = soup.find('span', class_='lemma')
    if lemma is not None:
        return lemma.find(text=True, recursive=False).rstrip() # Getting only span text + removing white spaces at the end


def get_sillabe(soup, word):
    lemma = soup.find(class_='lemma')
    small_list = lemma.find_all_next('small')
    for el in small_list:
        if el.parent not in lemma.children:
            try:
                sillabe = el.span.find(text=True, recursive=False)
            except AttributeError:  # Word has no syllable division
                return [word]
            break

    split_indexes = [pos for pos, char in enumerate(sillabe) if char == "|"]
    # necessario perchè le sillabazioni contengono gli accenti di pronuncia
    tmp = list(word)
    for i in split_indexes:
        tmp = tmp[0:i] + ["|"] + tmp[i:]
        sillabe = ''.join(tmp).split("|")
    return sillabe


def get_pronuncia(soup):
    pronuncia = soup.find('span', class_="paradigma")
    return pronuncia.text[10:]


def get_grammatica(soup):
    gram = soup.find_all('span', class_="grammatica")
    return [x.text for x in gram]


def get_defs(soup):
    defs = []
    definitions = soup.find_all('span', class_='italiano')
    for definition in definitions:
        sibling = definition.previous_sibling.previous_sibling;
        sibling_type = sibling.name
        sibling_number = sibling.text
        if is_target_property(sibling_type, "b"):
            if is_target_property(sibling_number,'1'):
                defs.append([definition.text])
            else:
                defs[-1].append(definition.text)
        else:
            defs.append(definition.text)
    if len(defs) == 0:
        raise exceptions.WordNotFoundError()
    return defs

def is_target_property(type, target):
    is_target = False
    if type == target:
        is_target = True
    return is_target


def get_data(word, all_data=True):
    url = build_url(URL.format(word))
    soup = get_soup(url)
    if all_data is False:
        return get_defs(soup)

    data = {'definizione': get_defs(soup), 'sillabe': get_sillabe(soup, word), 'lemma': get_lemma(soup),
            'pronuncia': get_pronuncia(soup), 'grammatica': get_grammatica(soup),
            'url': url}
    print(data)        
    return data
