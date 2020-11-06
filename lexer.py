from ply import lex
import math


class Lexer:
    reserved_words = {
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN',
        'fun': 'FUNCTION',
        'True': 'TRUE',
        'False': 'FALSE',
        'print': 'PRINT',
        'return': 'RETURN',
        'main': 'MAIN',
        'if': 'IF',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        'while': 'WHILE',
        'on': 'ON',
        'where': 'WHERE',
        'for': 'FOR',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN'
    }

    tokens = [
        # IDENTIFIER
        'ID',
        # NUMBERS
        'INTEGERNUMBER', 'FLOATNUMBER',
        # RESERVED WORDS
        #'INTEGER', 'FLOAT', 'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN',
        #'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR', 'AND', 'OR', 'NOT', 'IN',
        # OPERATORS
        'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE',
        # BRACKETS
        'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        # COLONS
        'SEMICOLON', 'COLON', 'COMMA',
        # ERROR
        'ERROR'

    ]
    tokens += reserved_words.values()

    # RESERVED WORDS
    t_INTEGER = r'int'
    t_FLOAT = r'float'
    t_BOOLEAN = r'bool'
    t_FUNCTION = r'fun'
    t_TRUE = r'True'
    t_FALSE = r'False'
    t_PRINT = r'print'
    t_RETURN = r'return'
    t_MAIN = r'main'
    t_IF = r'if'
    t_ELSE = r'else'
    t_ELSEIF = r'elseif'
    t_WHILE = r'while'
    t_ON = r'on'
    t_WHERE = r'where'
    t_FOR = r'for'
    t_AND = r'and'
    t_OR = r'or'
    t_NOT = r'not'
    t_IN = r'in'
    # OPERATOR
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'\%'
    t_GT = r'\>'
    t_GE = r'\>\=' #??
    t_LT = r'\<'
    t_LE = r'\<\=' #??
    t_EQ = r'\=\=' #??
    t_NE = r'\!\=' #??
    # BRACKETS
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    # COLONS
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','

    def t_ERROR(self, t):
        r'([0-9]+[a-zA-z_]+)|([A-Z]+[a-zA-z_]*)'
        return t

    def t_FLOATNUMBER(self, t):
        r'[0-9]+\.[0-9]+'
        if math.floor(float(t.value)) >= 1000000000:
            t.type = 'ERROR'
        else:
            t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        r'[0-9]+'
        if int(t.value) >= 1000000000:
            t.type = 'ERROR'
        else:
            t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-z_][a-zA-Z0-9_]*'
        if t.value in self.reserved_words:
            t.type = self.reserved_words[t.value]
        return t


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    # TODO
    # Float number (< 10 digit)
    # No consecutive operators