
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSEMICOLONleftCOMMArightASSIGNleftORleftANDleftEQNEleftLTGTGELEleftSUMSUBleftMULDIVMODleftLRBRRBleftP7leftP6leftP5leftP4leftP3leftP2leftP1AND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB blockdeclist : dec\n                   | declist dec\n                   | emptydec : vardec\n               | funcdectype : INTEGER\n                | FLOAT\n                | BOOLEANiddec : ID %prec P6\n                 | ID LSB exp RSB %prec P6\n                 | ID ASSIGN exp %prec P4idlist : iddec\n                  | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n                   | FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslist\n                     | emptyparamdecslist : paramdec\n                         | paramdecslist COMMA paramdecparamdec : ID COLON type\n                    | ID LSB RSB COLON typeblock : LCB stmtlist RCBstmtlist : stmt\n                    | stmtlist stmt\n                    | emptylvalue : ID %prec P7\n                  | ID LSB exp RSB %prec P7case : WHERE const COLON stmtlistcases : case\n                 | cases case\n                 | emptystmt : RETURN exp SEMICOLON\n                | exp SEMICOLON\n                | block\n                | vardec\n                | WHILE LRB exp RRB stmt\n                | ON LRB exp RRB LCB cases RCB SEMICOLON\n                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n                | FOR LRB ID IN ID RRB stmt\n                | IF LRB exp RRB stmt elseiflist\n                | IF LRB exp RRB stmt elseiflist ELSE stmt\n                | PRINT LRB ID RRB SEMICOLONelseiflist : ELSEIF LRB exp RRB stmt\n                      | elseiflist ELSEIF LRB exp RRB stmt\n                      | emptyrelopexp : exp relop exp %prec P3\n                    | relopexp relop expexp : lvalue ASSIGN exp %prec P5\n               | exp operator exp %prec P2\n               | relopexp\n               | const\n               | lvalue\n               | ID LRB explist RRB\n               | LRB exp RRB\n               | ID LRB RRB\n               | SUB exp %prec P1\n               | NOT exp %prec P1operator : AND\n                    | OR\n                    | SUM\n                    | SUB\n                    | MUL\n                    | DIV\n                    | MODconst : INTEGERNUMBER\n                 | FLOATNUMBER\n                 | TRUE\n                 | FALSErelop : GT\n                 | LT\n                 | NE\n                 | EQ\n                 | LE\n                 | GEexplist : exp\n                   | explist COMMA expempty : '
    
_lr_action_items = {'MAIN':([0,2,3,4,5,6,12,39,99,104,126,],[-79,11,-2,-4,-5,-6,-3,-15,-17,-24,-16,]),'FUNCTION':([0,2,3,4,5,6,12,39,99,104,126,],[8,8,-2,-4,-5,-6,-3,-15,-17,-24,-16,]),'ID':([0,2,3,4,5,6,8,12,14,16,17,24,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,73,83,84,85,86,88,89,99,102,104,105,107,108,109,110,111,112,113,117,126,127,129,130,132,134,138,139,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[9,9,-2,-4,-5,-6,15,-3,9,25,25,40,25,25,25,-15,25,25,25,25,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,25,25,93,40,93,-25,-27,25,-36,-37,-17,25,-24,-26,-35,25,25,121,25,25,124,-34,-16,93,25,137,93,-38,-79,-44,25,93,-42,-47,-41,93,25,-39,93,93,-43,25,93,-40,93,93,-45,-46,]),'$end':([1,68,104,],[0,-1,-24,]),'COLON':([7,9,10,23,25,27,28,29,33,34,35,36,37,40,47,66,67,72,75,78,79,80,81,82,93,97,101,103,131,151,],[13,-10,-13,-14,-28,-54,-52,-53,-67,-68,-69,-70,-12,70,-11,-58,-59,98,-57,-51,-48,-50,-49,-56,-10,114,-55,-29,-11,158,]),'COMMA':([7,9,10,20,21,22,23,25,27,28,29,33,34,35,36,37,42,44,47,66,67,74,75,76,78,79,80,81,82,93,96,100,101,103,116,125,131,],[14,-10,-13,-7,-8,-9,-14,-28,-54,-52,-53,-67,-68,-69,-70,-12,73,-20,-11,-58,-59,102,-57,-77,-51,-48,-50,-49,-56,-10,-22,-21,-55,-29,-78,-23,-11,]),'LSB':([9,25,40,93,121,],[16,46,71,111,46,]),'ASSIGN':([9,25,27,93,103,121,131,],[17,-28,63,-28,-29,-28,-29,]),'LRB':([11,15,16,17,25,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,90,91,92,93,94,95,102,104,105,107,108,109,110,111,112,117,121,127,129,132,134,138,139,144,145,146,147,148,153,154,155,156,157,158,159,160,161,163,164,166,167,168,169,],[18,24,30,30,45,30,30,30,-15,30,30,30,30,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,30,30,30,30,-25,-27,30,-36,-37,108,109,110,45,112,113,30,-24,-26,-35,30,30,30,30,30,-34,45,30,30,30,-38,-79,-44,30,30,-42,156,-47,-41,30,161,30,-39,30,30,-43,30,30,-40,30,30,-45,-46,]),'INTEGER':([13,70,98,114,],[20,20,20,20,]),'FLOAT':([13,70,98,114,],[21,21,21,21,]),'BOOLEAN':([13,70,98,114,],[22,22,22,22,]),'SUB':([16,17,25,26,27,28,29,30,31,32,33,34,35,36,37,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,121,122,123,127,129,131,132,134,136,138,139,144,145,146,148,152,153,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[31,31,-28,53,-54,-52,-53,31,31,31,-67,-68,-69,-70,53,-15,31,31,31,31,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,31,31,53,-58,-59,31,-57,53,53,-51,-48,-50,53,-56,31,-25,-27,31,53,-36,-37,-28,-55,31,-29,-24,-26,53,-35,31,31,31,31,31,53,-34,53,53,53,-28,53,53,31,31,-29,31,-38,53,-79,-44,31,31,-42,-47,53,-41,31,31,-39,31,31,-43,31,53,31,-40,53,31,31,-45,-46,]),'NOT':([16,17,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,102,104,105,107,108,109,110,111,112,117,127,129,132,134,138,139,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[32,32,32,32,32,-15,32,32,32,32,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,32,32,32,32,-25,-27,32,-36,-37,32,-24,-26,-35,32,32,32,32,32,-34,32,32,32,-38,-79,-44,32,32,-42,-47,-41,32,32,-39,32,32,-43,32,32,-40,32,32,-45,-46,]),'INTEGERNUMBER':([16,17,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,102,104,105,107,108,109,110,111,112,117,127,129,132,134,138,139,143,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[33,33,33,33,33,-15,33,33,33,33,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,33,33,33,33,-25,-27,33,-36,-37,33,-24,-26,-35,33,33,33,33,33,-34,33,33,33,-38,-79,-44,33,33,33,-42,-47,-41,33,33,-39,33,33,-43,33,33,-40,33,33,-45,-46,]),'FLOATNUMBER':([16,17,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,102,104,105,107,108,109,110,111,112,117,127,129,132,134,138,139,143,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[34,34,34,34,34,-15,34,34,34,34,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,34,34,34,34,-25,-27,34,-36,-37,34,-24,-26,-35,34,34,34,34,34,-34,34,34,34,-38,-79,-44,34,34,34,-42,-47,-41,34,34,-39,34,34,-43,34,34,-40,34,34,-45,-46,]),'TRUE':([16,17,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,102,104,105,107,108,109,110,111,112,117,127,129,132,134,138,139,143,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[35,35,35,35,35,-15,35,35,35,35,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,35,35,35,35,-25,-27,35,-36,-37,35,-24,-26,-35,35,35,35,35,35,-34,35,35,35,-38,-79,-44,35,35,35,-42,-47,-41,35,35,-39,35,35,-43,35,35,-40,35,35,-45,-46,]),'FALSE':([16,17,30,31,32,39,45,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,83,84,85,86,88,89,102,104,105,107,108,109,110,111,112,117,127,129,132,134,138,139,143,144,145,146,148,153,154,156,157,158,159,160,161,163,164,166,167,168,169,],[36,36,36,36,36,-15,36,36,36,36,-60,-61,-62,-63,-64,-65,-66,-71,-72,-73,-74,-75,-76,36,36,36,36,-25,-27,36,-36,-37,36,-24,-26,-35,36,36,36,36,36,-34,36,36,36,-38,-79,-44,36,36,36,-42,-47,-41,36,36,-39,36,36,-43,36,36,-40,36,36,-45,-46,]),'RRB':([18,20,21,22,24,25,27,28,29,33,34,35,36,41,42,43,44,45,65,66,67,74,75,76,78,79,80,81,82,96,100,101,103,116,118,119,123,124,125,137,152,162,165,],[38,-7,-8,-9,-79,-28,-54,-52,-53,-67,-68,-69,-70,72,-18,-19,-20,75,82,-58,-59,101,-57,-77,-51,-48,-50,-49,-56,-22,-21,-55,-29,-78,127,128,132,133,-23,145,159,166,167,]),'SEMICOLON':([19,20,21,22,25,27,28,29,33,34,35,36,66,67,75,78,79,80,81,82,87,93,101,103,106,120,121,131,133,136,149,],[39,-7,-8,-9,-28,-54,-52,-53,-67,-68,-69,-70,-58,-59,-57,-51,-48,-50,-49,-56,107,-28,-55,-29,117,129,-28,-29,139,144,157,]),'LCB':([20,21,22,38,39,69,72,83,84,85,88,89,104,105,107,115,117,127,128,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-7,-8,-9,69,-15,69,69,69,-25,-27,-36,-37,-24,-26,-35,69,-34,69,135,69,-38,-79,-44,69,-42,-47,-41,69,-39,69,69,-43,69,-40,69,69,-45,-46,]),'RSB':([25,26,27,28,29,33,34,35,36,66,67,71,75,77,78,79,80,81,82,101,103,122,],[-28,47,-54,-52,-53,-67,-68,-69,-70,-58,-59,97,-57,103,-51,-48,-50,-49,-56,-55,-29,131,]),'AND':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,50,-54,-52,-53,-67,-68,-69,-70,50,50,-58,-59,-57,50,50,-51,-48,-50,50,-56,50,-28,-55,-29,50,50,50,50,50,-28,50,50,-29,50,50,50,50,]),'OR':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,51,-54,-52,-53,-67,-68,-69,-70,51,51,-58,-59,-57,51,51,-51,-48,-50,51,-56,51,-28,-55,-29,51,51,51,51,51,-28,51,51,-29,51,51,51,51,]),'SUM':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,52,-54,-52,-53,-67,-68,-69,-70,52,52,-58,-59,-57,52,52,-51,-48,-50,52,-56,52,-28,-55,-29,52,52,52,52,52,-28,52,52,-29,52,52,52,52,]),'MUL':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,54,-54,-52,-53,-67,-68,-69,-70,54,54,-58,-59,-57,54,54,-51,-48,-50,54,-56,54,-28,-55,-29,54,54,54,54,54,-28,54,54,-29,54,54,54,54,]),'DIV':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,55,-54,-52,-53,-67,-68,-69,-70,55,55,-58,-59,-57,55,55,-51,-48,-50,55,-56,55,-28,-55,-29,55,55,55,55,55,-28,55,55,-29,55,55,55,55,]),'MOD':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,56,-54,-52,-53,-67,-68,-69,-70,56,56,-58,-59,-57,56,56,-51,-48,-50,56,-56,56,-28,-55,-29,56,56,56,56,56,-28,56,56,-29,56,56,56,56,]),'GT':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,57,-54,57,-53,-67,-68,-69,-70,57,57,-58,-59,-57,57,57,-51,-48,-50,57,-56,57,-28,-55,-29,57,57,57,57,57,-28,57,57,-29,57,57,57,57,]),'LT':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,58,-54,58,-53,-67,-68,-69,-70,58,58,-58,-59,-57,58,58,-51,-48,-50,58,-56,58,-28,-55,-29,58,58,58,58,58,-28,58,58,-29,58,58,58,58,]),'NE':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,59,-54,59,-53,-67,-68,-69,-70,59,59,-58,-59,-57,59,59,-51,-48,-50,59,-56,59,-28,-55,-29,59,59,59,59,59,-28,59,59,-29,59,59,59,59,]),'EQ':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,60,-54,60,-53,-67,-68,-69,-70,60,60,-58,-59,-57,60,60,-51,-48,-50,60,-56,60,-28,-55,-29,60,60,60,60,60,-28,60,60,-29,60,60,60,60,]),'LE':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,61,-54,61,-53,-67,-68,-69,-70,61,61,-58,-59,-57,61,61,-51,-48,-50,61,-56,61,-28,-55,-29,61,61,61,61,61,-28,61,61,-29,61,61,61,61,]),'GE':([25,26,27,28,29,33,34,35,36,37,65,66,67,75,76,77,78,79,80,81,82,87,93,101,103,106,116,118,119,120,121,122,123,131,136,152,162,165,],[-28,62,-54,62,-53,-67,-68,-69,-70,62,62,-58,-59,-57,62,62,-51,-48,-50,62,-56,62,-28,-55,-29,62,62,62,62,62,-28,62,62,-29,62,62,62,62,]),'RCB':([39,69,83,84,85,88,89,104,105,107,117,134,135,138,139,140,141,142,146,148,150,153,157,158,160,163,164,168,169,],[-15,-79,104,-25,-27,-36,-37,-24,-26,-35,-34,-38,-79,-79,-44,149,-31,-33,-42,-47,-32,-41,-39,-79,-43,-30,-40,-45,-46,]),'RETURN':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,86,86,-25,-27,-36,-37,-24,-26,-35,-34,86,86,-38,-79,-44,86,-42,-47,-41,86,-39,86,86,-43,86,-40,86,86,-45,-46,]),'WHILE':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,90,90,-25,-27,-36,-37,-24,-26,-35,-34,90,90,-38,-79,-44,90,-42,-47,-41,90,-39,90,90,-43,90,-40,90,90,-45,-46,]),'ON':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,91,91,-25,-27,-36,-37,-24,-26,-35,-34,91,91,-38,-79,-44,91,-42,-47,-41,91,-39,91,91,-43,91,-40,91,91,-45,-46,]),'FOR':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,92,92,-25,-27,-36,-37,-24,-26,-35,-34,92,92,-38,-79,-44,92,-42,-47,-41,92,-39,92,92,-43,92,-40,92,92,-45,-46,]),'IF':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,94,94,-25,-27,-36,-37,-24,-26,-35,-34,94,94,-38,-79,-44,94,-42,-47,-41,94,-39,94,94,-43,94,-40,94,94,-45,-46,]),'PRINT':([39,69,83,84,85,88,89,104,105,107,117,127,132,134,138,139,145,146,148,153,154,157,158,159,160,163,164,166,167,168,169,],[-15,95,95,-25,-27,-36,-37,-24,-26,-35,-34,95,95,-38,-79,-44,95,-42,-47,-41,95,-39,95,95,-43,95,-40,95,95,-45,-46,]),'ELSEIF':([39,88,89,104,107,117,134,138,139,146,148,153,157,160,164,168,169,],[-15,-36,-37,-24,-35,-34,-38,147,-44,-42,-47,-41,-39,-43,-40,-45,-46,]),'ELSE':([39,88,89,104,107,117,134,138,139,146,148,153,157,160,164,168,169,],[-15,-36,-37,-24,-35,-34,-38,-79,-44,-42,-47,-41,-39,-43,-40,-45,-46,]),'WHERE':([39,84,85,88,89,104,105,107,117,134,135,138,139,140,141,142,146,148,150,153,157,158,160,163,164,168,169,],[-15,-25,-27,-36,-37,-24,-26,-35,-34,-38,143,-79,-44,143,-31,-33,-42,-47,-32,-41,-39,-79,-43,-30,-40,-45,-46,]),'IN':([121,],[130,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[3,12,]),'empty':([0,24,69,135,138,158,],[4,43,85,142,148,85,]),'vardec':([0,2,69,83,127,132,145,154,158,159,163,166,167,],[5,5,89,89,89,89,89,89,89,89,89,89,89,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,69,83,127,132,145,154,158,159,163,166,167,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'iddec':([0,2,14,69,83,127,132,145,154,158,159,163,166,167,],[10,10,23,10,10,10,10,10,10,10,10,10,10,10,]),'type':([13,70,98,114,],[19,96,115,125,]),'exp':([16,17,30,31,32,45,46,48,49,63,64,69,83,86,102,108,109,110,111,112,127,129,132,144,145,154,156,158,159,161,163,166,167,],[26,37,65,66,67,76,77,78,79,80,81,87,87,106,116,118,119,120,122,123,87,136,87,152,87,87,162,87,87,165,87,87,87,]),'lvalue':([16,17,30,31,32,45,46,48,49,63,64,69,83,86,102,108,109,110,111,112,127,129,132,144,145,154,156,158,159,161,163,166,167,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'relopexp':([16,17,30,31,32,45,46,48,49,63,64,69,83,86,102,108,109,110,111,112,127,129,132,144,145,154,156,158,159,161,163,166,167,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'const':([16,17,30,31,32,45,46,48,49,63,64,69,83,86,102,108,109,110,111,112,127,129,132,143,144,145,154,156,158,159,161,163,166,167,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,151,29,29,29,29,29,29,29,29,29,29,]),'paramdecs':([24,],[41,]),'paramdecslist':([24,],[42,]),'paramdec':([24,73,],[44,100,]),'operator':([26,37,65,66,67,76,77,78,79,80,81,87,106,116,118,119,120,122,123,136,152,162,165,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'relop':([26,28,37,65,66,67,76,77,78,79,80,81,87,106,116,118,119,120,122,123,136,152,162,165,],[49,64,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'block':([38,69,72,83,115,127,132,145,154,158,159,163,166,167,],[68,88,99,88,126,88,88,88,88,88,88,88,88,88,]),'explist':([45,],[74,]),'stmtlist':([69,158,],[83,163,]),'stmt':([69,83,127,132,145,154,158,159,163,166,167,],[84,105,134,138,153,160,84,164,105,168,169,]),'cases':([135,],[140,]),'case':([135,140,],[141,150,]),'elseiflist':([138,],[146,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','pparser.py',12),
  ('declist -> dec','declist',1,'p_declist','pparser.py',16),
  ('declist -> declist dec','declist',2,'p_declist','pparser.py',17),
  ('declist -> empty','declist',1,'p_declist','pparser.py',18),
  ('dec -> vardec','dec',1,'p_dec','pparser.py',22),
  ('dec -> funcdec','dec',1,'p_dec','pparser.py',23),
  ('type -> INTEGER','type',1,'p_type','pparser.py',27),
  ('type -> FLOAT','type',1,'p_type','pparser.py',28),
  ('type -> BOOLEAN','type',1,'p_type','pparser.py',29),
  ('iddec -> ID','iddec',1,'p_iddec','pparser.py',33),
  ('iddec -> ID LSB exp RSB','iddec',4,'p_iddec','pparser.py',34),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec','pparser.py',35),
  ('idlist -> iddec','idlist',1,'p_idlist','pparser.py',39),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist','pparser.py',40),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','pparser.py',44),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','pparser.py',48),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','pparser.py',49),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','pparser.py',53),
  ('paramdecs -> empty','paramdecs',1,'p_paramdecs','pparser.py',54),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','pparser.py',58),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','pparser.py',59),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','pparser.py',63),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','pparser.py',64),
  ('block -> LCB stmtlist RCB','block',3,'p_block','pparser.py',68),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist','pparser.py',72),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','pparser.py',73),
  ('stmtlist -> empty','stmtlist',1,'p_stmtlist','pparser.py',74),
  ('lvalue -> ID','lvalue',1,'p_lvalue','pparser.py',78),
  ('lvalue -> ID LSB exp RSB','lvalue',4,'p_lvalue','pparser.py',79),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','pparser.py',83),
  ('cases -> case','cases',1,'p_cases','pparser.py',87),
  ('cases -> cases case','cases',2,'p_cases','pparser.py',88),
  ('cases -> empty','cases',1,'p_cases','pparser.py',89),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','pparser.py',93),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt','pparser.py',94),
  ('stmt -> block','stmt',1,'p_stmt','pparser.py',95),
  ('stmt -> vardec','stmt',1,'p_stmt','pparser.py',96),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt','pparser.py',97),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt','pparser.py',98),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt','pparser.py',99),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt','pparser.py',100),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt','pparser.py',101),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt','pparser.py',102),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt','pparser.py',103),
  ('elseiflist -> ELSEIF LRB exp RRB stmt','elseiflist',5,'p_elseiflist','pparser.py',107),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','pparser.py',108),
  ('elseiflist -> empty','elseiflist',1,'p_elseiflist','pparser.py',109),
  ('relopexp -> exp relop exp','relopexp',3,'p_relopexp','pparser.py',113),
  ('relopexp -> relopexp relop exp','relopexp',3,'p_relopexp','pparser.py',114),
  ('exp -> lvalue ASSIGN exp','exp',3,'p_exp','pparser.py',118),
  ('exp -> exp operator exp','exp',3,'p_exp','pparser.py',119),
  ('exp -> relopexp','exp',1,'p_exp','pparser.py',120),
  ('exp -> const','exp',1,'p_exp','pparser.py',121),
  ('exp -> lvalue','exp',1,'p_exp','pparser.py',122),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp','pparser.py',123),
  ('exp -> LRB exp RRB','exp',3,'p_exp','pparser.py',124),
  ('exp -> ID LRB RRB','exp',3,'p_exp','pparser.py',125),
  ('exp -> SUB exp','exp',2,'p_exp','pparser.py',126),
  ('exp -> NOT exp','exp',2,'p_exp','pparser.py',127),
  ('operator -> AND','operator',1,'p_operator','pparser.py',131),
  ('operator -> OR','operator',1,'p_operator','pparser.py',132),
  ('operator -> SUM','operator',1,'p_operator','pparser.py',133),
  ('operator -> SUB','operator',1,'p_operator','pparser.py',134),
  ('operator -> MUL','operator',1,'p_operator','pparser.py',135),
  ('operator -> DIV','operator',1,'p_operator','pparser.py',136),
  ('operator -> MOD','operator',1,'p_operator','pparser.py',137),
  ('const -> INTEGERNUMBER','const',1,'p_const','pparser.py',141),
  ('const -> FLOATNUMBER','const',1,'p_const','pparser.py',142),
  ('const -> TRUE','const',1,'p_const','pparser.py',143),
  ('const -> FALSE','const',1,'p_const','pparser.py',144),
  ('relop -> GT','relop',1,'p_relop','pparser.py',148),
  ('relop -> LT','relop',1,'p_relop','pparser.py',149),
  ('relop -> NE','relop',1,'p_relop','pparser.py',150),
  ('relop -> EQ','relop',1,'p_relop','pparser.py',151),
  ('relop -> LE','relop',1,'p_relop','pparser.py',152),
  ('relop -> GE','relop',1,'p_relop','pparser.py',153),
  ('explist -> exp','explist',1,'p_explist','pparser.py',157),
  ('explist -> explist COMMA exp','explist',3,'p_explist','pparser.py',158),
  ('empty -> <empty>','empty',0,'p_empty','pparser.py',162),
]
