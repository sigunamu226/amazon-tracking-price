def _file_path(path: str):
    return 'templates/' + path + '.html'

def items_path(file):
    return _file_path('items/' + file)

def accounts_path(file):
    return _file_path('accounts/' + file)