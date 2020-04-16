
from io import StringIO

import antlr4
from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from antlr4.tree.Trees import Trees
from antlr4.Utils import escapeWhitespace

from . import LangLexer 
from . import LangParser 

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class _SimpleErrorListener( ErrorListener ):

    def __init__(self):
        super(_SimpleErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "Error at position: %s:%s. %s" % (line, column, msg)
        raise Exception(msg)

def _stringToAST(s):

    input_stream  = antlr4.InputStream(s)
    
    error_listener = _SimpleErrorListener()
    
    #
    # Lexer
    #
    lexer = LangLexer.LangLexer(input_stream, output=None)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    tokens = CommonTokenStream(lexer)

    #
    # Parser
    #
    parser = LangParser.LangParser(tokens, output=None)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    parsed_tree = parser.program()
    
    return parser, parsed_tree

def stringToAST(s):

    parser, parsed_tree = _stringToAST(s)
    
    return parsed_tree

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class _MyTrees(Trees):

    @classmethod
    def toStringTree(cls, t, ruleNames=None, recog=None, level=0):

        if recog is not None:
            ruleNames = recog.ruleNames

        s = escapeWhitespace(cls.getNodeText(t, ruleNames), False)

        if t.getChildCount()==0:
            return '  ' * level + s

        with StringIO() as buf:
            buf.write('  ' * level + s + '\n')
            for i in range(0, t.getChildCount()):
                if i > 0:
                    buf.write('  ' * level + '\n')
                buf.write(cls.toStringTree(t.getChild(i), ruleNames, recog=recog, level=level+1))
            return buf.getvalue()

def printAST(s):

    parser, parsed_tree = _stringToAST(s)
    
    print( _MyTrees.toStringTree(parsed_tree, None, parser) )


