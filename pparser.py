from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block"""
        pass

    def p_declist(self, p):
        """declist : dec
                   | declist dec
                   | empty"""
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
                 | ID ASSIGN exp"""
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
                     | empty"""
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
        """block : LCB stmtlist RCB"""
        pass

    def p_stmtlist(self, p):
        """stmtlist : stmt
                    | stmtlist stmt
                    | empty"""
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
                 | cases case
                 | empty"""
        pass

    def p_stmt(self, p):
        """stmt : RETURN exp SEMICOLON
                | exp SEMICOLON
                | block
                | vardec
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
                | FOR LRB ID IN ID RRB stmt
                | IF LRB exp RRB stmt elseiflist
                | IF LRB exp RRB stmt elseiflist ELSE stmt
                | PRINT LRB ID RRB SEMICOLON"""
        pass

    def p_elseiflist(self, p):
        """elseiflist : ELSEIF LRB exp RRB stmt
                      | elseiflist ELSEIF LRB exp RRB stmt
                      | empty"""
        pass

    def p_relopexp(self, p):
        """relopexp : exp relop exp
                    | relopexp relop exp"""
        pass

    def p_exp(self, p):
        """exp : lvalue ASSIGN exp
               | exp operator exp
               | relopexp
               | const
               | lvalue
               | ID LRB explist RRB
               | LRB exp RRB
               | ID LRB RRB
               | SUB exp
               | NOT exp"""
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

    def p_empty(self, p):
        "empty : "
        pass

    """precedence = (
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )"""

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
