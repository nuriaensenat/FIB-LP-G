grammar g;

root : instruccions EOF;

instruccions : (instr? NEWLINE)* instr? ;

instr
  : expr                                    #exprInstr
  | VAR ASSIGN expr                         #assignInstr
  ;

expr
  : <assoc=right> expr OPERADOR expr        #operacioOperadorExpr
  | expr flip expr                          #operacioFlipExpr
  | fold expr                               #operacioFoldExpr
  | atom VERB expr                          #operacioVerbExpr
  | atom                                    #atomExpr
  | ADVERB expr                             #operacioAdverbExpr
  | atom expr                               #aplicarFuncioExpr
  | OPERADOR expr                           #operacioUnariaOperadorExpr
  ;

atom
  : '(' expr ')'                            #parentesisAtom
  | vector                                  #vectorAtom
  | VAR                                     #varAtom
  | NUM                                     #numAtom
  | ADVERB                                  #adverbAtom
  | VERB                                    #verbAtom
  ;

flip: (VERB | OPERADOR) '~' ;
fold: VERB '/';
vector : NUM+ ;

VERB : '+' 
  | '-' 
  | '*' 
  | '%' 
  | '|' 
  | '^' 
  | '>' 
  | '<' 
  | '>=' 
  | '<=' 
  | '=' 
  | '<>' 
  ;
ADVERB : ']' 
  | 'i.' 
  | '+:' 
  | '-:' 
  | '*:' 
  | '%:' 
  | '|:' 
  | '^:' 
  ;
OPERADOR : '{' 
  | ',' 
  | '#' 
  | '@:' 
  ;

ASSIGN : '=:' ;
NUM : '_'?[0-9]+ ;
VAR : [a-zA-Z_][a-zA-Z0-9_]* ;

NEWLINE : [\r\n]+ ;
WS      : [ \t]+ -> skip ;
COMMENT : 'NB.' ~[\r\n]* -> skip ;