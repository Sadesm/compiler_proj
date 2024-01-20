import re

SAMPLE_CODE = """  sahih bozi; 
ashar arz;
ashar           tool;\\\ kjlsk gsursbv 
arz = begir(ashar);
tool = begir(ashar);
agar ( tool == arz ){
chap ("morba ast");
chap ("masahat");
chap ( arz * arz );
chap ("mohit");
chap ( arz * 4 );\\*djkhwycgagcd


   *\\
}
agar ( tool != arz ){
chap ("mostati ast");
chap ("masahat");
chap ( arz * tool );
chap ("mohit");
chap ( arz * 2 + tool * 2 );
}
"""

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


def get_first_token(line, token):
    if re.search(token, line) and re.search(token, line).start() == 0:
        return re.search(token, line).end(), re.search(token, line)


def build_code_list(code):
    if code == '':
        print("tamom shode :)")
        return 1
    current_token = (),
    flag_find_token = False
    _len = -1
    for token, token_p in list(tokens.items()):
        result = get_first_token(code, token_p)
        if result:
            if result[0] > _len:
                current_token = token, result[1]
                _len = result[0]
                flag_find_token = True
    if current_token[0] == 'IGNORE':
        return build_code_list(code[_len:])
    if flag_find_token:
        print('\x1b[6;30;42m' + f'token: {current_token[0]}' + '\x1b[0m')
        print(code[:_len])
        CODE_LIST.append(current_token)
        return build_code_list(code[_len:])

    print("rerrore code kharabe")
    print(code)
    return -1


def compile_code(code: str):
    if build_code_list(code) == 1:
        # TODO faze baad
        ...


if __name__ == '__main__':
    compile_code(SAMPLE_CODE)
