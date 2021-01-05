from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program_declist(self, p):
        """program : declist MAIN LRB RRB block"""
        pass

    def p_program_main(self, p):
        """program : MAIN LRB RRB block"""
        pass

    def p_declist_dec(self, p):
        """declist : dec"""
        pass

    def p_declist_declist(self, p):
        """declist : declist dec"""
        pass

    def p_dec_vardec(self, p):
        """dec : vardec"""
        pass

    def p_dec_funcdec(self, p):
        """dec : funcdec"""
        pass

    def p_type_integer(self, p):
        """type : INTEGER"""
        pass

    def p_type_float(self, p):
        """type : FLOAT"""
        pass

    def p_type_boolean(self, p):
        """type : BOOLEAN"""
        pass

    def p_iddec_id(self, p):
        """iddec : ID"""
        pass

    def p_iddec_id_lsb(self, p):
        """iddec : ID LSB exp RSB"""
        pass

    def p_iddec_assign(self, p):
        """iddec : assign """
        pass

    def p_idlist_iddec(self, p):
        """idlist : iddec"""
        pass

    def p_idlist_idlist(self, p):
        """idlist : idlist COMMA iddec"""
        pass

    def p_vardec(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        pass

    def p_funcdec_type_block(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block"""
        pass

    def p_funcdec_block(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB block"""
        pass

    def p_paramdecs_paramdecslist(self, p):
        """paramdecs : paramdecslist"""
        pass

    def p_paramdecs_lambda(self, p):
        """paramdecs : """
        pass

    def p_paramdecslist_paramdec(self, p):
        """paramdecslist : paramdec"""
        pass

    def p_paramdecslist_paramdecslist(self, p):
        """paramdecslist : paramdecslist COMMA paramdec"""
        pass

    def p_paramdec_id_colon(self, p):
        """paramdec : ID COLON type"""
        pass

    def p_paramdec_id_lsb(self, p):
        """paramdec : ID LSB RSB COLON type"""
        pass

    def p_block_lcb_stmtlist(self, p):
        """block : LCB stmtlist RCB"""
        pass

    def p_block_lcb_rcb(self, p):
        """block : LCB RCB"""
        pass

    def p_stmtlist_stmt(self, p):
        """stmtlist : stmt"""
        pass

    def p_stmtlist_stmtlist(self, p):
        """stmtlist : stmtlist stmt"""
        pass

    def p_lvalue_id(self, p):
        """lvalue : ID"""
        pass

    def p_lvalue_id_lsb(self, p):
        """lvalue : ID LSB exp RSB"""
        pass

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        pass

    def p_cases_case(self, p):
        """cases : case"""
        pass

    def p_cases_cases(self, p):
        """cases : cases case"""
        pass

    def p_stmt_return(self, p):
        """stmt : RETURN exp SEMICOLON"""
        pass

    def p_stmt_exp(self, p):
        """stmt : exp SEMICOLON"""
        pass

    def p_stmt_block(self, p):
        """stmt : block"""
        pass

    def p_stmt_vardec(self, p):
        """stmt : vardec"""
        pass

    def p_stmt_while(self, p):
        """stmt : WHILE LRB exp RRB stmt"""
        pass

    def p_stmt_on_cases(self, p):
        """stmt : ON LRB exp RRB LCB cases RCB SEMICOLON"""
        pass

    def p_stmt_on(self, p):
        """stmt : ON LRB exp RRB LCB RCB SEMICOLON"""
        pass

    def p_stmt_for_exp(self, p):
        """stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        pass

    def p_stmt_for_id(self, p):
        """stmt : FOR LRB ID IN ID RRB stmt"""
        pass

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        pass

    def p_stmt_if(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist %prec P3"""
        pass

    def p_stmt_if_else(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"""
        pass

    def p_elseiflist_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt"""
        pass

    def p_elseiflist_lambda(self, p):
        """elseiflist : """
        pass

    # def p_relopexp(self, p):
    #     """relopexp : exp relop exp
    #                 | relopexp relop exp"""
    #     pass

    def p_exp_assign(self, p):
        """exp : assign"""
        pass

    def p_exp_exp_operator(self, p):
        """exp : exp operator exp %prec P1"""
        pass

    def p_exp_exp_relop(self, p):
        """exp : exp relop exp %prec P2"""
        pass

    def p_exp_const(self, p):
        """exp : const"""
        pass

    def p_exp_lvalue(self, p):
        """exp : lvalue"""
        pass

    def p_exp_id_explist(self, p):
        """exp : ID LRB explist RRB"""
        pass

    def p_exp_lrb_exp(self, p):
        """exp : LRB exp RRB"""
        pass

    def p_exp_id_lrb(self, p):
        """exp : ID LRB RRB"""
        pass

    def p_exp_sub(self, p):
        """exp : SUB exp"""
        pass

    def p_exp_not(self, p):
        """exp : NOT exp"""
        pass

    def p_assign(self, p):
        """assign : lvalue ASSIGN exp"""
        pass

    def p_operator_and(self, p):
        """operator : AND"""
        pass

    def p_operator_or(self, p):
        """operator : OR"""
        pass

    def p_operator_sum(self, p):
        """operator : SUM"""
        pass

    def p_operator_sub(self, p):
        """operator : SUB"""
        pass

    def p_operator_mul(self, p):
        """operator : MUL"""
        pass

    def p_operator_div(self, p):
        """operator : DIV"""
        pass

    def p_operator_mod(self, p):
        """operator : MOD"""
        pass

    def p_const_integernumber(self, p):
        """const : INTEGERNUMBER"""
        pass

    def p_const_floatnumber(self, p):
        """const : FLOATNUMBER"""
        pass

    def p_const_true(self, p):
        """const : TRUE"""
        pass

    def p_const_false(self, p):
        """const : FALSE"""
        pass

    def p_relop_gt(self, p):
        """relop : GT"""
        pass

    def p_relop_lt(self, p):
        """relop : LT"""
        pass

    def p_relop_ne(self, p):
        """relop : NE"""
        pass

    def p_relop_eq(self, p):
        """relop : EQ"""
        pass

    def p_relop_le(self, p):
        """relop : LE"""
        pass

    def p_relop_ge(self, p):
        """relop : GE"""
        pass

    def p_explist_exp(self, p):
        """explist : exp"""
        pass

    def p_explist_explist(self, p):
        """explist : explist COMMA exp"""
        pass

    precedence = (
        ('right', 'ASSIGN'),
        ('left', 'P3'),
        ('left', 'ELSE', 'ELSEIF'),
        ('left', 'P2'),
        ('left', 'P1'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'LT', 'GT', 'GE', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'NOT')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
