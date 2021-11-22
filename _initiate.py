import h5py
import utils

_supported_attributes_urls = {'style' : 'https://api.crossref.org/styles',
                         'locale' : 'https://api.crossref.org/locales'}

# to save list of strings to hdf5
encode_as_ascii = lambda s : s.encode('ascii', 'ignore')     

with h5py.File('metadata.hdf5', 'w') as file:
    for attr in _supported_attributes_urls:
        # create data group for url and data
        group = file.create_group(attr)
        # store url used
        group.create_dataset('url', data = _supported_attributes_urls[attr])
        # get data
        message = utils.handle_request(_supported_attributes_urls[attr], attr)
        # save relevant information
        group.create_dataset('version', data = message['message-version'])
        group.create_dataset('total-available', data = message['message']['total-results'])
        group.create_dataset('items', data = list(map(encode_as_ascii, message['message']['items'])))
