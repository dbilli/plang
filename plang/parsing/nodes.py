
#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class ExprTree(object):

    def __init__(self):
        self.preflush_stack = False
        
    def format(self, l=0):
        return self.prefix(l) + str(self) + '\n'

    def prefix(self, l=0):
        return "    " * l

    def unescape(self, s):
            last=''
            s2=''
            for c in s:
                    if last == '\\':
                            last = ''
                            if   c=='b' : c="\b"
                            elif c=='t' : c="\t"
                            elif c=='n' : c="\n"
                            elif c=='f' : c="\f"
                            elif c=='r' : c="\r"
                            elif c=='\"': c="\""
                            elif c=='\'': c="'"
                            else:         c=="\\"
                            s2 = s2 + c
                    else:
                            if c=='\\': last = c
                            else:       s2 = s2 + c
            return s2

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class ProgramTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "ProgramTree(" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class NullLiteralTree(ExprTree):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Null(%s)" % (self.text)

#----------------------------------------------------------------------#

class BooleanLiteralTree(ExprTree):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Bool(%s)" % (self.text)

#----------------------------------------------------------------------#

class NumericLiteralTree(ExprTree):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Num(%s)" % (self.text)

#----------------------------------------------------------------------#

class StringLiteralTree(ExprTree):

    def __init__(self, text):
        self.text = text[1:-1]

    def __repr__(self):
        return "String(%s)" % (self.text)

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class ArrayLiteralTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return "ArrayLiteral( %s )" % (self.elements)

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "ArrayLiteral(" + '\n'

        for e in self.elements:
            s += e.format(l+1)

        s += self.prefix(l) + ")" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class ExpressionSequenceTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "ExpressionSequence{" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + "}" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class ExpressionStatementTree(ExprTree):

    def __init__(self, e):
        self.e = e

    def format(self, l=0):
        return self.e.format(l)

#----------------------------------------------------------------------#
# id(<symbol>)                                                         #
#----------------------------------------------------------------------#

class createIdentifierTree(ExprTree):

    def __init__(self, symbol):

        if symbol[0] in ["'", '"']:
            symbol = symbol[1:-1]

        self.symbol = symbol

    def __repr__(self):
        return "id(%s)" % (self.symbol)

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class _StatementTree(ExprTree):
    pass

#----------------------------------------------------------------------#

class BreakStatementTree(_StatementTree):
    
    def __repr__(self):
        return "break"

#----------------------------------------------------------------------#

class ContinueStatementTree(_StatementTree):

    def __repr__(self):
        return "continue"


#class ReturnStatementTree(_StatementTree):
#    def __init__(self, expr):
#        self.expr = expr
#    def __repr__(self):
#        return "return"
#    def format(self, l=0):
#        s = ''
#        s += self.prefix(l) + "return (" + '\n'
#        if self.expr is not None:
#            s += self.expr.format(l+1)
#        s += self.prefix(l) + ")" + '\n'
#        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class StatementListTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "StatementListTree(" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

class StatementTree(ExprTree):
    
    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "StatementTree(" + '\n'

        for e in self.elements:
            s += e.format(l+1)

        s += self.prefix(l) + ")" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class BlockTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "Block(" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# e1 = e2
#
class AssignmentExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "assignement" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#----------------------------------------------------------------------#
# e1[e2]                                                               #
#----------------------------------------------------------------------#

class MemberIndexTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.e1.format(l+1)
        s += self.prefix(l) + "[" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + "]" + '\n'
        return s
        
#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# e1.<symbol>
#
class MemberDotTree(ExprTree):
    
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "<" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "." + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ">" + '\n'
        return s
        
#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# IF (E1) { E2 } else { E3 }
#
class IfTree(ExprTree):

    def __init__(self, e1,e2,e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "if " + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + ") " + '\n'
        s += self.e2.format(l+1)
        if self.e3:
            s += self.prefix(l) + "else" + '\n'
            s += self.e3.format(l+1)
        return s


#
# do E1 while (E2)
#
class DoWhileTree(ExprTree):

    def __init__(self, e1,e2):
        self.e1=e1
        self.e2=e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "do" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "while" + '\n'
        s += self.e2.format(l+1)

        return s

#
# while (E1) { E2 }
#
class WhileTree(ExprTree):

    def __init__(self, e1,e2):
        self.e1=e1
        self.e2=e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "while" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "do" + '\n'
        s += self.e2.format(l+1)
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# { e1 , e2 , e3 , }
#
#
# o = {}
# e1
# e2
# e3
# 
#
class ObjectLiteral(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "Obj{" + '\n'
        for i, e in enumerate(self.elements):
            s += e.format(l+1)
        s += self.prefix(l) + "}" + '\n'

        return s

#
#  P1 = E2
#
class PropertyAssignment(ExprTree):
    
    def __init__(self, ctype, e1, e2):
        self.ctype = ctype if ctype != ':' else '='
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "P<" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "%s" % (self.ctype) + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ">" + '\n'
        return s

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# e1 ( ARGS )
#
class ArgumentsExpressionTree(ExprTree):
    def __init__(self, e1, elements):
        self.e1        = e1
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.e1.format(l)
        s += self.prefix(l) + "ARGS(" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s


#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

#
# + e
#
class UnaryPlusExpressionTree(ExprTree):

    def __init__(self, e):
        self.e = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "+" + '\n'
        s += self.e.format(l+1)
        return s

#
# ~ e
#
class UnaryMinusExpressionTree(ExprTree):

    def __init__(self, e):
        self.e = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "-" + '\n'
        s += self.e.format(l+1)
        return s


#
# ~ e
#
class BitNotExpressionTree(ExprTree):

    def __init__(self, e):
        self.e = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "~" + '\n'
        s += self.e.format(l+1)
        return s

#
# ! e
#
class NotExpressionTree(ExprTree):

    def __init__(self, e):
        self.e = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "!" + '\n'
        s += self.e.format(l+1)
        return s

#
# e1 ** e2
#
class PowerExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "***" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 * e2
#
class MultiplicativeExpressionTree(ExprTree):

    def __init__(self, etype, e1, e2):
        self.etype = etype
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "%s" % (self.etype) + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 + e2
# e1 - e2
#
class AdditiveExpressionTree(ExprTree):

    def __init__(self, etype, e1, e2):
        self.etype = etype
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "%s" % (self.etype) + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s


#
# e1 << e2
# e1 >> e2
#
class BitShiftExpressionTree(ExprTree):

    def __init__(self, etype, e1, e2):
        self.etype = etype
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "<<" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 <  e2
# e1 >  e2
# e1 <= e2
# e1 >= e2
#
class RelationalExpressionTree(ExprTree):
    
    def __init__(self, etype, e1, e2):
        self.etype = etype
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "%s" % (self.etype) + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s


#
# e1 == e2 
# e1 != e2
#
class EqualityExpressionTree(ExprTree):

    def __init__(self, etype, e1, e2):
        self.etype = etype
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "%s" % (self.etype) + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 & e2
#
class BitAndExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "&" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 ^ e2
#
class BitXOrExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "^" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 | e2
#
class BitOrExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "|" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 && e2
#
class LogicalAndExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "&&" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 || e2
#
class LogicalOrExpressionTree(ExprTree):

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "||" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#
# e1 ? e2 : e3
#
class TernaryExpressionTree(ExprTree):

    def __init__(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "(" + '\n'
        s += self.e1.format(l+1)
        s += self.prefix(l) + "?" + '\n'
        s += self.e2.format(l+1)
        s += self.prefix(l) + ":" + '\n'
        s += self.e3.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

class MatchTree(ExprTree):

    def __init__(self, e):
        self.e     = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "match " + '\n'
        s += self.e.format(l+1)
        s += self.prefix(l) + "" + '\n'
        return s


class MatchBodyTree(ExprTree):

    def __init__(self, prematch, match, onmatch):
        self.prematch = prematch
        self.match    = match
        self.onmatch   = onmatch

    def format(self, l=0):
        s = ''
        
        if self.prematch:
           s += self.prefix(l) + '-> PREMATCH' + '\n'
           s += self.prematch.format(l+1) #+ '\n'
        
        s += self.match.format(l) #+ '\n'
        
        if self.onmatch:
           s += self.prefix(l) + '-> ONMATCH' + '\n'
           s += self.onmatch.format(l+1) #+ '\n'
        
        return s

#------------------------------------------------------------------------------#

class InputMatchTree(ExprTree):

    def __init__(self, arg, options):
        self.arg     = arg
        self.options = options

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "input (" + '\n'
        s += self.arg.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        
        for option in self.options:
            name, value = option
            s += name.format(l) + value.format(l+1) + '\n'
        
        return s

#------------------------------------------------------------------------------#

class SequenceMatchTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "sequence(" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#

class ChoiceMatchTree(ExprTree):

    def __init__(self, elements):
        self.elements = elements

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "choice (" + '\n'
        for e in self.elements:
            s += e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#

class RepetitionMatchTree(ExprTree):

    def __init__(self, e):
        self.e     = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "+ (" + '\n'
        s += self.e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#

class StarRepetitionMatchTree(ExprTree):

    def __init__(self, e):
        self.e     = e

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "* (" + '\n'
        s += self.e.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#

class OptionalMatchTree(ExprTree):

    def __init__(self, match):
        self.match = match

    def format(self, l=0):
        s = ''
        s += self.prefix(l) + "? (" + '\n'
        s += self.match.format(l+1)
        s += self.prefix(l) + ")" + '\n'
        return s

#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

class BaseExprFactory:

    def __init__(self):
        pass

    def createNullLiteral(self, text):
        return NullLiteralTree(text)

    def createBooleanLiteral(self, text):
        return BooleanLiteralTree(text)

    def createNumericLiteral(self, text):
        return NumericLiteralTree(text)

    def createStringLiteral(self, text):
        return StringLiteralTree(text)

    def createArrayLiteral(self, elements):
        return ArrayLiteralTree(elements)

    def createIdentifier(self, text):
        return createIdentifierTree(text)


    def createIf(self, e1, e2, e3):
        return IfTree(e1,e2,e3)
    
    def createDoWhileStatement(self, e1, e2):
        return DoWhileTree(e1, e2)

    def createWhileStatement(self, e1, e2):
        return WhileTree(e1, e2)

    def createObjectLiteral(self, elements):
        return ObjectLiteral(elements)

    def createPropertyAssignment(self, ctype, e1, e2):
        return PropertyAssignment(ctype, e1,e2)

    def createMemberDot(self, e1, e2):
        return MemberDotTree(e1, e2)

    def createMemberIndex(self, e1, e2):
        return MemberIndexTree(e1, e2)

    def createProgram(self, elements):
        return ProgramTree(elements)        

    def createStatement(self, elements):
        return StatementTree(elements)        

    def createBlock(self, elements):
        return BlockTree(elements)  
        
    def createBreakStatement(self):
        return BreakStatementTree()
    
    def createContinueStatement(self):
        return ContinueStatementTree()
    
    def createExpressionSequence(self, elements):
        return ExpressionSequenceTree(elements)        

    def createExpressionStatement(self, e):
        return ExpressionStatementTree(e)

    def createArgumentsExpression(self, e, arguments):
        return ArgumentsExpressionTree(e, arguments)

    def createUnaryPlusExpression(self, e):
        return UnaryPlusExpressionTree(e)

    def createUnaryMinusExpression(self, e):
        return UnaryMinusExpressionTree(e)

    def createBitNotExpression(self, e):
        return BitNotExpressionTree(e)

    def createNotExpression(self, e):
        return NotExpressionTree(e)

    def createPowerExpression(self, e1, e2):
        return PowerExpressionTree(e1, e2)

    def createMultiplicativeExpression(self, etype, e1, e2):
        return MultiplicativeExpressionTree(etype, e1, e2)

    def createAdditiveExpression(self, etype, e1, e2):
        return AdditiveExpressionTree(etype, e1, e2)

    def createBitShiftExpression(self, etype, e1, e2):
        return BitShiftExpressionTree(etype, e1, e2)

    def createRelationalExpression(self, etype, e1, e2):
        return RelationalExpressionTree(etype, e1, e2)

    def createEqualityExpression(self, etype, e1, e2):
        return EqualityExpressionTree(etype, e1, e2)

    def createBitAndExpression(self, e1, e2):
        return BitAndExpressionTree(e1, e2)
    
    def createBitXOrExpression(self, e1, e2):
        return BitXOrExpressionTree(e1, e2)
    
    def createBitOrExpression (self, e1, e2):
        return BitOrExpressionTree(e1, e2)

    def createLogicalAndExpression(self, e1, e2):
        return LogicalAndExpressionTree(e1, e2)
        
    def createLogicalOrExpression(self, e1, e2):
        return LogicalOrExpressionTree(e1, e2)

    def createTernaryExpression(self, e1, e2, e3):
        return TernaryExpressionTree(e1, e2, e3)

    def createAssignmentExpression(self, e1, e2):
        return AssignmentExpressionTree(e1, e2)

    #------------------------------------------------------------------#
    # MATCH                                                            #
    #------------------------------------------------------------------#  

    def createMatchStatement(self, e):
        return MatchTree(e)

    def createMatchBody(self, p, m, a):
        return MatchBodyTree(p, m, a)
        
    def createRepetitionMatch(self, rtype, elements):
        if rtype == '+':
            return RepetitionMatchTree(elements)
        else:
            return StarRepetitionMatchTree(elements)
            
    def createSequenceMatch(self, elements):
        return SequenceMatchTree(elements)

    def createChoiceMatch(self, elements):
        return ChoiceMatchTree(elements)

    def createOptionalMatch(self, e):
        return OptionalMatchTree(e)

    def createInputMatch(self, arguments, options): 
        return InputMatchTree(arguments, options)
