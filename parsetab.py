
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftP4leftP3leftP2leftP1leftORleftANDleftEQNEleftLTGTGELEleftSUMSUBleftMULDIVMODleftNOTAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block\n                    | MAIN LRB RRB blockdeclist : dec\n                   | declist decdec : vardec\n               | funcdectype : INTEGER\n                | FLOAT\n                | BOOLEANiddec : ID\n                 | ID LSB exp RSB\n                 | assign idlist : iddec\n                  | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n                   | FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslist\n                     | paramdecslist : paramdec\n                         | paramdecslist COMMA paramdecparamdec : ID COLON type\n                    | ID LSB RSB COLON typeblock : LCB stmtlist RCB\n                 | LCB RCBstmtlist : stmt\n                    | stmtlist stmtlvalue : ID\n                  | ID LSB exp RSBcase : WHERE const COLON stmtlistcases : case\n                 | cases casestmt : RETURN exp SEMICOLON\n                | exp SEMICOLON\n                | block\n                | vardec\n                | WHILE LRB exp RRB stmt\n                | ON LRB exp RRB LCB cases RCB SEMICOLON\n                | ON LRB exp RRB LCB RCB SEMICOLON\n                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n                | FOR LRB ID IN ID RRB stmt\n                | IF LRB exp RRB stmt elseiflist %prec P4\n                | IF LRB exp RRB stmt elseiflist ELSE stmt %prec P3\n                | PRINT LRB ID RRB SEMICOLONelseiflist : elseiflist ELSEIF LRB exp RRB stmt\n                      | exp : assign\n               | exp operator exp %prec P1\n               | exp relop exp %prec P2\n               | const\n               | lvalue\n               | ID LRB explist RRB\n               | LRB exp RRB\n               | ID LRB RRB\n               | SUB exp\n               | NOT expassign : lvalue ASSIGN expoperator : AND\n                    | OR\n                    | SUM\n                    | SUB\n                    | MUL\n                    | DIV\n                    | MODconst : INTEGERNUMBER\n                 | FLOATNUMBER\n                 | TRUE\n                 | FALSErelop : GT\n                 | LT\n                 | NE\n                 | EQ\n                 | LE\n                 | GEexplist : exp\n                   | explist COMMA exp'
    
_lr_action_items = {'MAIN':([0,2,4,5,6,14,45,73,97,110,134,],[3,13,-3,-5,-6,-4,-15,-25,-24,-17,-16,]),'FUNCTION':([0,2,4,5,6,14,45,73,97,110,134,],[8,8,-3,-5,-6,-4,-15,-25,-24,-17,-16,]),'ID':([0,2,4,5,6,8,14,17,19,20,28,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,89,97,98,100,101,102,103,104,105,106,110,113,115,126,128,129,131,134,135,139,140,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[9,9,-3,-5,-6,18,-4,9,29,29,46,29,29,29,82,-15,29,29,29,29,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,82,-25,-26,29,-35,-36,46,-24,-27,-34,29,29,119,29,29,122,-17,29,-33,82,29,138,82,-16,-37,-46,-44,29,82,-42,-39,-41,82,-38,82,82,-43,29,82,-40,82,-45,]),'$end':([1,43,71,73,97,],[0,-2,-1,-25,-24,]),'LRB':([3,13,18,19,20,29,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,79,80,81,82,83,84,97,98,100,101,102,103,104,105,113,115,119,126,128,131,135,139,140,145,146,147,150,153,154,155,156,157,158,159,160,161,162,164,165,],[15,21,28,34,34,50,34,34,34,34,-15,34,34,34,34,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,34,-25,-26,34,-35,-36,101,102,103,50,105,106,-24,-27,-34,34,34,34,34,34,34,-33,50,34,34,34,-37,-46,-44,34,34,-42,-39,-41,34,160,-38,34,34,-43,34,34,-40,34,-45,]),'COLON':([7,9,10,11,27,29,31,32,33,37,38,39,40,41,46,52,69,70,82,85,88,91,94,95,96,108,112,114,130,151,],[16,-10,-13,-12,-14,-28,-47,-50,-51,-65,-66,-67,-68,-57,86,-11,-55,-56,-10,-12,109,-54,-48,-49,-53,123,-52,-29,-11,157,]),'COMMA':([7,9,10,11,24,25,26,27,29,31,32,33,37,38,39,40,41,48,49,52,69,70,82,85,90,91,92,94,95,96,107,111,112,114,125,130,133,],[17,-10,-13,-12,-7,-8,-9,-14,-28,-47,-50,-51,-65,-66,-67,-68,-57,89,-20,-11,-55,-56,-10,-12,113,-54,-75,-48,-49,-53,-22,-21,-52,-29,-76,-11,-23,]),'LSB':([9,29,46,82,119,],[19,51,87,104,51,]),'ASSIGN':([9,12,29,33,52,82,114,119,130,],[-28,20,-28,20,-29,-28,-29,-28,-29,]),'RRB':([15,21,24,25,26,28,29,31,32,33,37,38,39,40,41,47,48,49,50,68,69,70,90,91,92,94,95,96,107,111,112,114,116,117,121,122,125,133,138,152,163,],[22,42,-7,-8,-9,-19,-28,-47,-50,-51,-65,-66,-67,-68,-57,88,-18,-20,91,96,-55,-56,112,-54,-75,-48,-49,-53,-22,-21,-52,-29,126,127,131,132,-76,-23,146,158,164,]),'INTEGER':([16,86,109,123,],[24,24,24,24,]),'FLOAT':([16,86,109,123,],[25,25,25,25,]),'BOOLEAN':([16,86,109,123,],[26,26,26,26,]),'SUB':([19,20,29,30,31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,82,85,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,117,118,119,120,121,125,126,128,130,131,135,137,139,140,145,146,147,150,152,153,154,156,157,158,159,160,161,162,163,164,165,],[35,35,-28,58,-47,-50,-51,35,35,35,-65,-66,-67,-68,58,35,-15,35,35,35,35,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,58,-55,-56,35,-25,-26,35,58,-35,-36,-28,-47,-54,58,58,58,58,-53,-24,-27,58,-34,35,35,35,35,35,-52,35,-29,-33,58,58,58,-28,58,58,58,35,35,-29,35,-37,58,-46,-44,35,35,-42,-39,58,-41,35,-38,35,35,-43,35,35,-40,58,35,-45,]),'NOT':([19,20,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,97,98,100,101,102,103,104,105,113,115,126,128,131,135,139,140,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[36,36,36,36,36,36,-15,36,36,36,36,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,36,-25,-26,36,-35,-36,-24,-27,-34,36,36,36,36,36,36,-33,36,36,36,-37,-46,-44,36,36,-42,-39,-41,36,-38,36,36,-43,36,36,-40,36,-45,]),'INTEGERNUMBER':([19,20,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,97,98,100,101,102,103,104,105,113,115,126,128,131,135,139,140,144,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[37,37,37,37,37,37,-15,37,37,37,37,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,37,-25,-26,37,-35,-36,-24,-27,-34,37,37,37,37,37,37,-33,37,37,37,-37,-46,-44,37,37,37,-42,-39,-41,37,-38,37,37,-43,37,37,-40,37,-45,]),'FLOATNUMBER':([19,20,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,97,98,100,101,102,103,104,105,113,115,126,128,131,135,139,140,144,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[38,38,38,38,38,38,-15,38,38,38,38,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,38,-25,-26,38,-35,-36,-24,-27,-34,38,38,38,38,38,38,-33,38,38,38,-37,-46,-44,38,38,38,-42,-39,-41,38,-38,38,38,-43,38,38,-40,38,-45,]),'TRUE':([19,20,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,97,98,100,101,102,103,104,105,113,115,126,128,131,135,139,140,144,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[39,39,39,39,39,39,-15,39,39,39,39,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,39,-25,-26,39,-35,-36,-24,-27,-34,39,39,39,39,39,39,-33,39,39,39,-37,-46,-44,39,39,39,-42,-39,-41,39,-38,39,39,-43,39,39,-40,39,-45,]),'FALSE':([19,20,34,35,36,44,45,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,78,97,98,100,101,102,103,104,105,113,115,126,128,131,135,139,140,144,145,146,147,150,153,154,156,157,158,159,160,161,162,164,165,],[40,40,40,40,40,40,-15,40,40,40,40,-58,-59,-60,-61,-62,-63,-64,-69,-70,-71,-72,-73,-74,40,-25,-26,40,-35,-36,-24,-27,-34,40,40,40,40,40,40,-33,40,40,40,-37,-46,-44,40,40,40,-42,-39,-41,40,-38,40,40,-43,40,40,-40,40,-45,]),'LCB':([22,24,25,26,42,44,45,72,73,74,77,78,88,97,98,100,115,124,126,127,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[44,-7,-8,-9,44,44,-15,44,-25,-26,-35,-36,44,-24,-27,-34,-33,44,44,136,44,-37,-46,-44,44,-42,-39,-41,44,-38,44,44,-43,44,-40,44,-45,]),'SEMICOLON':([23,24,25,26,29,31,32,33,37,38,39,40,41,69,70,76,82,85,91,94,95,96,99,112,114,118,119,130,132,137,142,148,],[45,-7,-8,-9,-28,-47,-50,-51,-65,-66,-67,-68,-57,-55,-56,100,-28,-47,-54,-48,-49,-53,115,-52,-29,128,-28,-29,140,145,150,156,]),'RSB':([29,30,31,32,33,37,38,39,40,41,69,70,87,91,93,94,95,96,112,114,120,],[-28,52,-47,-50,-51,-65,-66,-67,-68,-57,-55,-56,108,-54,114,-48,-49,-53,-52,-29,130,]),'AND':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,55,-47,-50,-51,-65,-66,-67,-68,55,55,-55,-56,55,-28,-47,-54,55,55,55,55,-53,55,-52,-29,55,55,55,-28,55,55,55,-29,55,55,55,]),'OR':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,56,-47,-50,-51,-65,-66,-67,-68,56,56,-55,-56,56,-28,-47,-54,56,56,56,56,-53,56,-52,-29,56,56,56,-28,56,56,56,-29,56,56,56,]),'SUM':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,57,-47,-50,-51,-65,-66,-67,-68,57,57,-55,-56,57,-28,-47,-54,57,57,57,57,-53,57,-52,-29,57,57,57,-28,57,57,57,-29,57,57,57,]),'MUL':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,59,-47,-50,-51,-65,-66,-67,-68,59,59,59,-56,59,-28,-47,-54,59,59,59,59,-53,59,-52,-29,59,59,59,-28,59,59,59,-29,59,59,59,]),'DIV':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,60,-47,-50,-51,-65,-66,-67,-68,60,60,60,-56,60,-28,-47,-54,60,60,60,60,-53,60,-52,-29,60,60,60,-28,60,60,60,-29,60,60,60,]),'MOD':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,61,-47,-50,-51,-65,-66,-67,-68,61,61,61,-56,61,-28,-47,-54,61,61,61,61,-53,61,-52,-29,61,61,61,-28,61,61,61,-29,61,61,61,]),'GT':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,62,-47,-50,-51,-65,-66,-67,-68,62,62,-55,-56,62,-28,-47,-54,62,62,62,62,-53,62,-52,-29,62,62,62,-28,62,62,62,-29,62,62,62,]),'LT':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,63,-47,-50,-51,-65,-66,-67,-68,63,63,-55,-56,63,-28,-47,-54,63,63,63,63,-53,63,-52,-29,63,63,63,-28,63,63,63,-29,63,63,63,]),'NE':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,64,-47,-50,-51,-65,-66,-67,-68,64,64,-55,-56,64,-28,-47,-54,64,64,64,64,-53,64,-52,-29,64,64,64,-28,64,64,64,-29,64,64,64,]),'EQ':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,65,-47,-50,-51,-65,-66,-67,-68,65,65,-55,-56,65,-28,-47,-54,65,65,65,65,-53,65,-52,-29,65,65,65,-28,65,65,65,-29,65,65,65,]),'LE':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,66,-47,-50,-51,-65,-66,-67,-68,66,66,-55,-56,66,-28,-47,-54,66,66,66,66,-53,66,-52,-29,66,66,66,-28,66,66,66,-29,66,66,66,]),'GE':([29,30,31,32,33,37,38,39,40,41,68,69,70,76,82,85,91,92,93,94,95,96,99,112,114,116,117,118,119,120,121,125,130,137,152,163,],[-28,67,-47,-50,-51,-65,-66,-67,-68,67,67,-55,-56,67,-28,-47,-54,67,67,67,67,-53,67,-52,-29,67,67,67,-28,67,67,67,-29,67,67,67,]),'RCB':([44,45,72,73,74,77,78,97,98,100,115,135,136,139,140,141,143,147,149,150,153,156,159,161,162,165,],[73,-15,97,-25,-26,-35,-36,-24,-27,-34,-33,-37,142,-46,-44,148,-31,-42,-32,-39,-41,-38,-43,-30,-40,-45,]),'RETURN':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[75,-15,75,-25,-26,-35,-36,-24,-27,-34,-33,75,75,-37,-46,-44,75,-42,-39,-41,75,-38,75,75,-43,75,-40,75,-45,]),'WHILE':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[79,-15,79,-25,-26,-35,-36,-24,-27,-34,-33,79,79,-37,-46,-44,79,-42,-39,-41,79,-38,79,79,-43,79,-40,79,-45,]),'ON':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[80,-15,80,-25,-26,-35,-36,-24,-27,-34,-33,80,80,-37,-46,-44,80,-42,-39,-41,80,-38,80,80,-43,80,-40,80,-45,]),'FOR':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[81,-15,81,-25,-26,-35,-36,-24,-27,-34,-33,81,81,-37,-46,-44,81,-42,-39,-41,81,-38,81,81,-43,81,-40,81,-45,]),'IF':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[83,-15,83,-25,-26,-35,-36,-24,-27,-34,-33,83,83,-37,-46,-44,83,-42,-39,-41,83,-38,83,83,-43,83,-40,83,-45,]),'PRINT':([44,45,72,73,74,77,78,97,98,100,115,126,131,135,139,140,146,147,150,153,154,156,157,158,159,161,162,164,165,],[84,-15,84,-25,-26,-35,-36,-24,-27,-34,-33,84,84,-37,-46,-44,84,-42,-39,-41,84,-38,84,84,-43,84,-40,84,-45,]),'ELSE':([45,73,77,78,97,100,115,135,139,140,147,150,153,156,159,162,165,],[-15,-25,-35,-36,-24,-34,-33,-37,-46,-44,-42,-39,-41,-38,-43,-40,-45,]),'ELSEIF':([45,73,77,78,97,100,115,135,139,140,147,150,153,156,159,162,165,],[-15,-25,-35,-36,-24,-34,-33,-37,-46,-44,-42,-39,-41,-38,-43,-40,-45,]),'WHERE':([45,73,74,77,78,97,98,100,115,135,136,139,140,141,143,147,149,150,153,156,159,161,162,165,],[-15,-25,-26,-35,-36,-24,-27,-34,-33,-37,144,-46,-44,144,-31,-42,-32,-39,-41,-38,-43,-30,-40,-45,]),'IN':([119,],[129,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[4,14,]),'vardec':([0,2,44,72,126,131,146,154,157,158,161,164,],[5,5,78,78,78,78,78,78,78,78,78,78,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,44,72,126,131,146,154,157,158,161,164,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'iddec':([0,2,17,44,72,126,131,146,154,157,158,161,164,],[10,10,27,10,10,10,10,10,10,10,10,10,10,]),'assign':([0,2,17,19,20,34,35,36,44,50,51,53,54,72,75,101,102,103,104,105,113,126,128,131,145,146,154,157,158,160,161,164,],[11,11,11,31,31,31,31,31,85,31,31,31,31,85,31,31,31,31,31,31,31,85,31,85,31,85,85,85,85,31,85,85,]),'lvalue':([0,2,17,19,20,34,35,36,44,50,51,53,54,72,75,101,102,103,104,105,113,126,128,131,145,146,154,157,158,160,161,164,],[12,12,12,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'type':([16,86,109,123,],[23,107,124,133,]),'exp':([19,20,34,35,36,44,50,51,53,54,72,75,101,102,103,104,105,113,126,128,131,145,146,154,157,158,160,161,164,],[30,41,68,69,70,76,92,93,94,95,76,99,116,117,118,120,121,125,76,137,76,152,76,76,76,76,163,76,76,]),'const':([19,20,34,35,36,44,50,51,53,54,72,75,101,102,103,104,105,113,126,128,131,144,145,146,154,157,158,160,161,164,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,151,32,32,32,32,32,32,32,32,]),'block':([22,42,44,72,88,124,126,131,146,154,157,158,161,164,],[43,71,77,77,110,134,77,77,77,77,77,77,77,77,]),'paramdecs':([28,],[47,]),'paramdecslist':([28,],[48,]),'paramdec':([28,89,],[49,111,]),'operator':([30,41,68,69,70,76,92,93,94,95,99,116,117,118,120,121,125,137,152,163,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'relop':([30,41,68,69,70,76,92,93,94,95,99,116,117,118,120,121,125,137,152,163,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'stmtlist':([44,157,],[72,161,]),'stmt':([44,72,126,131,146,154,157,158,161,164,],[74,98,135,139,153,159,74,162,98,165,]),'explist':([50,],[90,]),'cases':([136,],[141,]),'case':([136,141,],[143,149,]),'elseiflist':([139,],[147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','pparser.py',12),
  ('program -> MAIN LRB RRB block','program',4,'p_program','pparser.py',13),
  ('declist -> dec','declist',1,'p_declist','pparser.py',17),
  ('declist -> declist dec','declist',2,'p_declist','pparser.py',18),
  ('dec -> vardec','dec',1,'p_dec','pparser.py',22),
  ('dec -> funcdec','dec',1,'p_dec','pparser.py',23),
  ('type -> INTEGER','type',1,'p_type','pparser.py',27),
  ('type -> FLOAT','type',1,'p_type','pparser.py',28),
  ('type -> BOOLEAN','type',1,'p_type','pparser.py',29),
  ('iddec -> ID','iddec',1,'p_iddec','pparser.py',33),
  ('iddec -> ID LSB exp RSB','iddec',4,'p_iddec','pparser.py',34),
  ('iddec -> assign','iddec',1,'p_iddec','pparser.py',35),
  ('idlist -> iddec','idlist',1,'p_idlist','pparser.py',39),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist','pparser.py',40),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','pparser.py',44),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','pparser.py',48),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','pparser.py',49),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','pparser.py',53),
  ('paramdecs -> <empty>','paramdecs',0,'p_paramdecs','pparser.py',54),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','pparser.py',58),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','pparser.py',59),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','pparser.py',63),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','pparser.py',64),
  ('block -> LCB stmtlist RCB','block',3,'p_block','pparser.py',68),
  ('block -> LCB RCB','block',2,'p_block','pparser.py',69),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist','pparser.py',73),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','pparser.py',74),
  ('lvalue -> ID','lvalue',1,'p_lvalue','pparser.py',78),
  ('lvalue -> ID LSB exp RSB','lvalue',4,'p_lvalue','pparser.py',79),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','pparser.py',83),
  ('cases -> case','cases',1,'p_cases','pparser.py',87),
  ('cases -> cases case','cases',2,'p_cases','pparser.py',88),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','pparser.py',92),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt','pparser.py',93),
  ('stmt -> block','stmt',1,'p_stmt','pparser.py',94),
  ('stmt -> vardec','stmt',1,'p_stmt','pparser.py',95),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt','pparser.py',96),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt','pparser.py',97),
  ('stmt -> ON LRB exp RRB LCB RCB SEMICOLON','stmt',7,'p_stmt','pparser.py',98),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt','pparser.py',99),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt','pparser.py',100),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt','pparser.py',101),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt','pparser.py',102),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt','pparser.py',103),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','pparser.py',107),
  ('elseiflist -> <empty>','elseiflist',0,'p_elseiflist','pparser.py',108),
  ('exp -> assign','exp',1,'p_exp','pparser.py',117),
  ('exp -> exp operator exp','exp',3,'p_exp','pparser.py',118),
  ('exp -> exp relop exp','exp',3,'p_exp','pparser.py',119),
  ('exp -> const','exp',1,'p_exp','pparser.py',120),
  ('exp -> lvalue','exp',1,'p_exp','pparser.py',121),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp','pparser.py',122),
  ('exp -> LRB exp RRB','exp',3,'p_exp','pparser.py',123),
  ('exp -> ID LRB RRB','exp',3,'p_exp','pparser.py',124),
  ('exp -> SUB exp','exp',2,'p_exp','pparser.py',125),
  ('exp -> NOT exp','exp',2,'p_exp','pparser.py',126),
  ('assign -> lvalue ASSIGN exp','assign',3,'p_assign','pparser.py',130),
  ('operator -> AND','operator',1,'p_operator','pparser.py',134),
  ('operator -> OR','operator',1,'p_operator','pparser.py',135),
  ('operator -> SUM','operator',1,'p_operator','pparser.py',136),
  ('operator -> SUB','operator',1,'p_operator','pparser.py',137),
  ('operator -> MUL','operator',1,'p_operator','pparser.py',138),
  ('operator -> DIV','operator',1,'p_operator','pparser.py',139),
  ('operator -> MOD','operator',1,'p_operator','pparser.py',140),
  ('const -> INTEGERNUMBER','const',1,'p_const','pparser.py',144),
  ('const -> FLOATNUMBER','const',1,'p_const','pparser.py',145),
  ('const -> TRUE','const',1,'p_const','pparser.py',146),
  ('const -> FALSE','const',1,'p_const','pparser.py',147),
  ('relop -> GT','relop',1,'p_relop','pparser.py',151),
  ('relop -> LT','relop',1,'p_relop','pparser.py',152),
  ('relop -> NE','relop',1,'p_relop','pparser.py',153),
  ('relop -> EQ','relop',1,'p_relop','pparser.py',154),
  ('relop -> LE','relop',1,'p_relop','pparser.py',155),
  ('relop -> GE','relop',1,'p_relop','pparser.py',156),
  ('explist -> exp','explist',1,'p_explist','pparser.py',160),
  ('explist -> explist COMMA exp','explist',3,'p_explist','pparser.py',161),
]
