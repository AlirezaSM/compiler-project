from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block
                    | MAIN LRB RRB block"""
        pass

    def p_declist(self, p):
        """declist : dec
                   | declist dec"""
        pass

    def p_dec(self, p):
        """dec : vardec
               | funcdec"""
        pass

    def p_type(self, p):
        """type : INTEGER
                | FLOAT
                | BOOLEAN"""
        pass

    def p_iddec(self, p):
        """iddec : ID
                 | ID LSB exp RSB
                 | assign """
        pass

    def p_idlist(self, p):
        """idlist : iddec
                  | idlist COMMA iddec"""
        pass

    def p_vardec(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        pass

    def p_funcdec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
                   | FUNCTION ID LRB paramdecs RRB block"""
        pass

    def p_paramdecs(self, p):
        """paramdecs : paramdecslist
                     | """
        pass

    def p_paramdecslist(self, p):
        """paramdecslist : paramdec
                         | paramdecslist COMMA paramdec"""
        pass

    def p_paramdec(self, p):
        """paramdec : ID COLON type
                    | ID LSB RSB COLON type"""
        pass

    def p_block(self, p):
        """block : LCB stmtlist RCB
                 | LCB RCB"""
        pass

    def p_stmtlist(self, p):
        """stmtlist : stmt
                    | stmtlist stmt"""
        pass

    def p_lvalue(self, p):
        """lvalue : ID
                  | ID LSB exp RSB"""
        pass

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        pass

    def p_cases(self, p):
        """cases : case
                 | cases case"""
        pass

    def p_stmt(self, p):
        """stmt : RETURN exp SEMICOLON
                | exp SEMICOLON
                | block
                | vardec
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | ON LRB exp RRB LCB RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
                | FOR LRB ID IN ID RRB stmt
                | IF LRB exp RRB stmt elseiflist %prec P4
                | IF LRB exp RRB stmt elseiflist ELSE stmt %prec P3
                | PRINT LRB ID RRB SEMICOLON"""
        pass

    def p_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt
                      | """
        pass

    # def p_relopexp(self, p):
    #     """relopexp : exp relop exp
    #                 | relopexp relop exp"""
    #     pass

    def p_exp(self, p):
        """exp : assign
               | exp operator exp %prec P1
               | exp relop exp %prec P2
               | const
               | lvalue
               | ID LRB explist RRB
               | LRB exp RRB
               | ID LRB RRB
               | SUB exp
               | NOT exp"""
        pass

    def p_assign(self, p):
        """assign : lvalue ASSIGN exp"""
        pass

    def p_operator(self, p):
        """operator : AND
                    | OR
                    | SUM
                    | SUB
                    | MUL
                    | DIV
                    | MOD"""
        pass

    def p_const(self, p):
        """const : INTEGERNUMBER
                 | FLOATNUMBER
                 | TRUE
                 | FALSE"""
        pass

    def p_relop(self, p):
        """relop : GT
                 | LT
                 | NE
                 | EQ
                 | LE
                 | GE"""
        pass

    def p_explist(self, p):
        """explist : exp
                   | explist COMMA exp"""
        pass

    # else be akharin if bechasbe

    #precedence = (
    #    ('left', 'LT', 'GT', 'LE', 'GE', 'NE', 'EQ'),
    #    ('left', 'SUM', 'SUB'),
    #    ('left', 'MUL', 'DIV', 'MOD'),
    #    ('left', 'OR', 'AND'),
    #    ('left', 'LRB', 'RRB'),
    #    ('left', 'P7'),
    #    ('left', 'P6'),
    #    ('left', 'P5'),
    #    ('left', 'P4'),
    #    ('left', 'P3'),
    #    ('left', 'P2'),
    #    ('left', 'P1')
    #)

    precedence = (
        # ('left', 'SEMICOLON'),
        # ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'P4'),
        ('left', 'P3'),
        ('left', 'P2'),
        ('left', 'P1'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'LT', 'GT', 'GE', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'NOT')
        # ('left', 'LRB', 'RRB'),
        # ('left', 'P7'),
        # ('left', 'P6'),
        # ('left', 'P5'),
        # ('left', 'P4'),
        # ('left', 'P3'),
        # ('left', 'P2'),
        # ('left', 'P1')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
