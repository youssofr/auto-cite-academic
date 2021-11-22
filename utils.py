from os import popen
from requests import get
from json import loads

def handle_request(url, requested_attr = ''):
    if requested_attr != '':
        requested_attr = '( ' + requested_attr + ' )'
    try: 
        response = get(url)
    except Exception as e:
        raise type(e)(e.message + f' While trying to access ' +url)
    
    # format response as dictionary
    message = loads(response.content)

    if message['status'] != 'ok':
        raise RuntimeError(f'Error retrieving data {requested_attr} from {url} with status != "ok"')
    
    return message

def read_doi_list(file_path, sep = '\n'):
    with open(file_path, 'r') as file:
        dois = file.read().split(sep)

    return dois

def write_reference_list(reference_list, file_path, mode = 'w'):
    with open(file_path, mode) as file:
        file.writelines(reference_list)

def get_reference_from_doi(doi_link, style = 'ieee', lang = 'en-US'):
    return popen(f'curl -LH "Accept: text/bibliography; style={style}; locale={lang}" {doi_link}').read()

def tidy_reference_list(reference_list, style = ''):
    if style == '':
        style = detect_style(reference_list[0])
    
    if style[:4] == 'ieee':
        return ['['+str(i+1)+']'+r[3:] for i, r in enumerate(reference_list)]
    elif style[:3] == 'apa':
        return reference_list.sort()
    else:
        return reference_list

def detect_style(reference_item):
    if reference_item[0] == '[':
        return 'ieee'
    else:
        raise ValueError('Unknown style. Provide a style explicitly.')