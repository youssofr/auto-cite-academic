import utils

# parameters to automatically cite a list of sources from a file
in_file_path = 'dois list.txt' # relative path (to the running location) or absolute path of the file containing doi reference list  here
style = 'ieee'
language = 'en-US'
out_file_path = 'reference list.txt'
writing_mode = 'w' # 'w' to overwrite the existing file 'a' to append output to existing file

# read the dois from the file
dois = utils.read_doi_list(in_file_path)

# create reference list
reference_list = []
for doi in dois:
    reference_list.append(utils.get_reference_from_doi, style, language)

# order if apa and number of ieee
reference_list = utils.tidy_reference_list(reference_list, style)

# save reference list
utils.write_reference_list(reference_list, out_file_path, writing_mode)