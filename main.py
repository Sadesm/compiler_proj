import re

tokens = {
    'PRINT': r'chap',
    'INPUT': r'begir',
    'OPEN_PARA': r'\(',
    'CLOSE_PARA': r'\)',
    'SEMI_COLON': r'\;',
    'DOT': r'\.',
    'ASSIGNMENT': r'\=',
    'SUM': r'\+',
    'SUB': r'\-',
    'MUL': r'\*',
    'DIV': r'\/',
    'LOGICAL_EQUAL': r'==',
    'LOGICAL_NOT_EQUAL': r'!=',
    'LOGICAL_HIGHER': r'>',
    'LOGICAL_HIGHER_OR_EQUAL': r'>=',
    'LOGICAL_LOWER': r'<',
    'LOGICAL_LOWER_OR_EQUAL': r'<=',
    'NUMBER': r'\d+',
    'INT_VALUE': r'[0-9]+',
    'FLOAT_VALUE': r'[0-9]+\.[0-9]+',
    'INT': r'sahih',
    'FLOAT': r'ashar',
    'OPEN_BRACE': r'\{',
    'CLOSE_BRACE': r'\}',
    'IF': r'agar',
    'STRING': r'(".*"' + r"|'.*')",
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'IGNORE': r'(\\\*(.|\n)*\*\\|\\\\.*\n|\s|\t)',
}
CODE_LIST = []
length = 0
not_change_code = ''


class Token:
    def __init__(self, _type, _mohtava, _koja):
        self.type = _type
        self.mohtava = _mohtava
        self.makan = _koja


def mohasebe_ja(andaze):
    global not_change_code
    if andaze > len(not_change_code):
        return -1, -1
    _len = 0
    for i in range(len(not_change_code.splitlines())):
        for j in range(len(not_change_code.splitlines()[i])):
            if _len == andaze:
                return i, j
            _len += 1
        _len += 1

def get_first_token(line, token):
    if re.search(token, line) and re.search(token, line).start() == 0:
        return re.search(token, line).end(), re.search(token, line)

def build_code_list(code, flag=True):
    global length
    if code == '':
        print("tamom shode :)")
        return 1
    current_token = Token(None, None, None)
    flag_find_token = False
    _len = -1
    for token, token_p in list(tokens.items()):
        result = get_first_token(code, token_p)
        if result:
            if result[0] > _len:
                _len = result[0]
                current_token = Token(token, code[:_len], mohasebe_ja(length))
                flag_find_token = True

    if current_token.type == 'IGNORE' and flag:
        length += _len
        return build_code_list(code[_len:])

    if flag_find_token and flag:
        print('\x1b[6;30;42m' + f'token: {current_token.type}' + '\x1b[0m')
        print(current_token.mohtava, current_token.makan)
        CODE_LIST.append(current_token)
        length += _len
        return build_code_list(code[_len:])

    if flag:
        print('\u001b[41m' + f'token: ERROR' + '\x1b[0m')
        for i in range(len(code)):
            if build_code_list(code[i:], False) == 0:
                current_token = Token('ERROR', code[:i], mohasebe_ja(length))
                print(current_token.mohtava, current_token.makan)
                _len = i
                break
        length += _len
        CODE_LIST.append(current_token)
        return build_code_list(code[_len:])

    if flag_find_token:
        return 0

    return -1

def tree_code(list_of_token):
    ...

def compile_code(code: str):
    global not_change_code
    not_change_code = code
    if build_code_list(code) == 1:
        # TODO faze baad
        ...
