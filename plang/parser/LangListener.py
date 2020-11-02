# Generated from Lang.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#program.
    def enterProgram(self, ctx:LangParser.ProgramContext):
        pass

    # Exit a parse tree produced by LangParser#program.
    def exitProgram(self, ctx:LangParser.ProgramContext):
        pass


    # Enter a parse tree produced by LangParser#sourceElement.
    def enterSourceElement(self, ctx:LangParser.SourceElementContext):
        pass

    # Exit a parse tree produced by LangParser#sourceElement.
    def exitSourceElement(self, ctx:LangParser.SourceElementContext):
        pass


    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx:LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx:LangParser.StatementContext):
        pass


    # Enter a parse tree produced by LangParser#block.
    def enterBlock(self, ctx:LangParser.BlockContext):
        pass

    # Exit a parse tree produced by LangParser#block.
    def exitBlock(self, ctx:LangParser.BlockContext):
        pass


    # Enter a parse tree produced by LangParser#statementList.
    def enterStatementList(self, ctx:LangParser.StatementListContext):
        pass

    # Exit a parse tree produced by LangParser#statementList.
    def exitStatementList(self, ctx:LangParser.StatementListContext):
        pass


    # Enter a parse tree produced by LangParser#emptyStatement.
    def enterEmptyStatement(self, ctx:LangParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by LangParser#emptyStatement.
    def exitEmptyStatement(self, ctx:LangParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by LangParser#expressionStatement.
    def enterExpressionStatement(self, ctx:LangParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by LangParser#expressionStatement.
    def exitExpressionStatement(self, ctx:LangParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by LangParser#ifStatement.
    def enterIfStatement(self, ctx:LangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by LangParser#ifStatement.
    def exitIfStatement(self, ctx:LangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by LangParser#DoStatement.
    def enterDoStatement(self, ctx:LangParser.DoStatementContext):
        pass

    # Exit a parse tree produced by LangParser#DoStatement.
    def exitDoStatement(self, ctx:LangParser.DoStatementContext):
        pass


    # Enter a parse tree produced by LangParser#WhileStatement.
    def enterWhileStatement(self, ctx:LangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by LangParser#WhileStatement.
    def exitWhileStatement(self, ctx:LangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by LangParser#continueStatement.
    def enterContinueStatement(self, ctx:LangParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by LangParser#continueStatement.
    def exitContinueStatement(self, ctx:LangParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by LangParser#breakStatement.
    def enterBreakStatement(self, ctx:LangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by LangParser#breakStatement.
    def exitBreakStatement(self, ctx:LangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by LangParser#sourceElements.
    def enterSourceElements(self, ctx:LangParser.SourceElementsContext):
        pass

    # Exit a parse tree produced by LangParser#sourceElements.
    def exitSourceElements(self, ctx:LangParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by LangParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:LangParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by LangParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:LangParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by LangParser#arrayElementsList.
    def enterArrayElementsList(self, ctx:LangParser.ArrayElementsListContext):
        pass

    # Exit a parse tree produced by LangParser#arrayElementsList.
    def exitArrayElementsList(self, ctx:LangParser.ArrayElementsListContext):
        pass


    # Enter a parse tree produced by LangParser#arrayElement.
    def enterArrayElement(self, ctx:LangParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by LangParser#arrayElement.
    def exitArrayElement(self, ctx:LangParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by LangParser#objectLiteral.
    def enterObjectLiteral(self, ctx:LangParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by LangParser#objectLiteral.
    def exitObjectLiteral(self, ctx:LangParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by LangParser#objectLiteralList.
    def enterObjectLiteralList(self, ctx:LangParser.ObjectLiteralListContext):
        pass

    # Exit a parse tree produced by LangParser#objectLiteralList.
    def exitObjectLiteralList(self, ctx:LangParser.ObjectLiteralListContext):
        pass


    # Enter a parse tree produced by LangParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:LangParser.PropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by LangParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:LangParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by LangParser#PropertyExpressionBetween.
    def enterPropertyExpressionBetween(self, ctx:LangParser.PropertyExpressionBetweenContext):
        pass

    # Exit a parse tree produced by LangParser#PropertyExpressionBetween.
    def exitPropertyExpressionBetween(self, ctx:LangParser.PropertyExpressionBetweenContext):
        pass


    # Enter a parse tree produced by LangParser#propertyOperator.
    def enterPropertyOperator(self, ctx:LangParser.PropertyOperatorContext):
        pass

    # Exit a parse tree produced by LangParser#propertyOperator.
    def exitPropertyOperator(self, ctx:LangParser.PropertyOperatorContext):
        pass


    # Enter a parse tree produced by LangParser#propertyName.
    def enterPropertyName(self, ctx:LangParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by LangParser#propertyName.
    def exitPropertyName(self, ctx:LangParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by LangParser#propertyNameString.
    def enterPropertyNameString(self, ctx:LangParser.PropertyNameStringContext):
        pass

    # Exit a parse tree produced by LangParser#propertyNameString.
    def exitPropertyNameString(self, ctx:LangParser.PropertyNameStringContext):
        pass


    # Enter a parse tree produced by LangParser#arguments.
    def enterArguments(self, ctx:LangParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by LangParser#arguments.
    def exitArguments(self, ctx:LangParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by LangParser#argumentslist.
    def enterArgumentslist(self, ctx:LangParser.ArgumentslistContext):
        pass

    # Exit a parse tree produced by LangParser#argumentslist.
    def exitArgumentslist(self, ctx:LangParser.ArgumentslistContext):
        pass


    # Enter a parse tree produced by LangParser#argument.
    def enterArgument(self, ctx:LangParser.ArgumentContext):
        pass

    # Exit a parse tree produced by LangParser#argument.
    def exitArgument(self, ctx:LangParser.ArgumentContext):
        pass


    # Enter a parse tree produced by LangParser#expressionSequence.
    def enterExpressionSequence(self, ctx:LangParser.ExpressionSequenceContext):
        pass

    # Exit a parse tree produced by LangParser#expressionSequence.
    def exitExpressionSequence(self, ctx:LangParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by LangParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:LangParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:LangParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:LangParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:LangParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:LangParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:LangParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:LangParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:LangParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#PowerExpression.
    def enterPowerExpression(self, ctx:LangParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#PowerExpression.
    def exitPowerExpression(self, ctx:LangParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:LangParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:LangParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:LangParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:LangParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:LangParser.MemberDotExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:LangParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#NotExpression.
    def enterNotExpression(self, ctx:LangParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#NotExpression.
    def exitNotExpression(self, ctx:LangParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:LangParser.MemberIndexExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:LangParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:LangParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:LangParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:LangParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:LangParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:LangParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:LangParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:LangParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:LangParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#singleAtomicExpression.
    def enterSingleAtomicExpression(self, ctx:LangParser.SingleAtomicExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#singleAtomicExpression.
    def exitSingleAtomicExpression(self, ctx:LangParser.SingleAtomicExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:LangParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:LangParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:LangParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:LangParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:LangParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:LangParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:LangParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:LangParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:LangParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:LangParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:LangParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:LangParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:LangParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:LangParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:LangParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:LangParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:LangParser.ArrayLiteralExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:LangParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:LangParser.ObjectLiteralExpressionContext):
        pass

    # Exit a parse tree produced by LangParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:LangParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by LangParser#matchStatement.
    def enterMatchStatement(self, ctx:LangParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by LangParser#matchStatement.
    def exitMatchStatement(self, ctx:LangParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by LangParser#sequenceMatchStatement.
    def enterSequenceMatchStatement(self, ctx:LangParser.SequenceMatchStatementContext):
        pass

    # Exit a parse tree produced by LangParser#sequenceMatchStatement.
    def exitSequenceMatchStatement(self, ctx:LangParser.SequenceMatchStatementContext):
        pass


    # Enter a parse tree produced by LangParser#sequenceMatch.
    def enterSequenceMatch(self, ctx:LangParser.SequenceMatchContext):
        pass

    # Exit a parse tree produced by LangParser#sequenceMatch.
    def exitSequenceMatch(self, ctx:LangParser.SequenceMatchContext):
        pass


    # Enter a parse tree produced by LangParser#sequenceList.
    def enterSequenceList(self, ctx:LangParser.SequenceListContext):
        pass

    # Exit a parse tree produced by LangParser#sequenceList.
    def exitSequenceList(self, ctx:LangParser.SequenceListContext):
        pass


    # Enter a parse tree produced by LangParser#sequenceElement.
    def enterSequenceElement(self, ctx:LangParser.SequenceElementContext):
        pass

    # Exit a parse tree produced by LangParser#sequenceElement.
    def exitSequenceElement(self, ctx:LangParser.SequenceElementContext):
        pass


    # Enter a parse tree produced by LangParser#choiceMatch.
    def enterChoiceMatch(self, ctx:LangParser.ChoiceMatchContext):
        pass

    # Exit a parse tree produced by LangParser#choiceMatch.
    def exitChoiceMatch(self, ctx:LangParser.ChoiceMatchContext):
        pass


    # Enter a parse tree produced by LangParser#choiceList.
    def enterChoiceList(self, ctx:LangParser.ChoiceListContext):
        pass

    # Exit a parse tree produced by LangParser#choiceList.
    def exitChoiceList(self, ctx:LangParser.ChoiceListContext):
        pass


    # Enter a parse tree produced by LangParser#atomMatch.
    def enterAtomMatch(self, ctx:LangParser.AtomMatchContext):
        pass

    # Exit a parse tree produced by LangParser#atomMatch.
    def exitAtomMatch(self, ctx:LangParser.AtomMatchContext):
        pass


    # Enter a parse tree produced by LangParser#matchBody.
    def enterMatchBody(self, ctx:LangParser.MatchBodyContext):
        pass

    # Exit a parse tree produced by LangParser#matchBody.
    def exitMatchBody(self, ctx:LangParser.MatchBodyContext):
        pass


    # Enter a parse tree produced by LangParser#optionalMatchStatement.
    def enterOptionalMatchStatement(self, ctx:LangParser.OptionalMatchStatementContext):
        pass

    # Exit a parse tree produced by LangParser#optionalMatchStatement.
    def exitOptionalMatchStatement(self, ctx:LangParser.OptionalMatchStatementContext):
        pass


    # Enter a parse tree produced by LangParser#repetitionMatchStatement.
    def enterRepetitionMatchStatement(self, ctx:LangParser.RepetitionMatchStatementContext):
        pass

    # Exit a parse tree produced by LangParser#repetitionMatchStatement.
    def exitRepetitionMatchStatement(self, ctx:LangParser.RepetitionMatchStatementContext):
        pass


    # Enter a parse tree produced by LangParser#bracedMatchExpr.
    def enterBracedMatchExpr(self, ctx:LangParser.BracedMatchExprContext):
        pass

    # Exit a parse tree produced by LangParser#bracedMatchExpr.
    def exitBracedMatchExpr(self, ctx:LangParser.BracedMatchExprContext):
        pass


    # Enter a parse tree produced by LangParser#basicMatchStatement.
    def enterBasicMatchStatement(self, ctx:LangParser.BasicMatchStatementContext):
        pass

    # Exit a parse tree produced by LangParser#basicMatchStatement.
    def exitBasicMatchStatement(self, ctx:LangParser.BasicMatchStatementContext):
        pass


    # Enter a parse tree produced by LangParser#basicMatch.
    def enterBasicMatch(self, ctx:LangParser.BasicMatchContext):
        pass

    # Exit a parse tree produced by LangParser#basicMatch.
    def exitBasicMatch(self, ctx:LangParser.BasicMatchContext):
        pass


    # Enter a parse tree produced by LangParser#optionalMatch.
    def enterOptionalMatch(self, ctx:LangParser.OptionalMatchContext):
        pass

    # Exit a parse tree produced by LangParser#optionalMatch.
    def exitOptionalMatch(self, ctx:LangParser.OptionalMatchContext):
        pass


    # Enter a parse tree produced by LangParser#inputMatch.
    def enterInputMatch(self, ctx:LangParser.InputMatchContext):
        pass

    # Exit a parse tree produced by LangParser#inputMatch.
    def exitInputMatch(self, ctx:LangParser.InputMatchContext):
        pass


    # Enter a parse tree produced by LangParser#optionsList.
    def enterOptionsList(self, ctx:LangParser.OptionsListContext):
        pass

    # Exit a parse tree produced by LangParser#optionsList.
    def exitOptionsList(self, ctx:LangParser.OptionsListContext):
        pass


    # Enter a parse tree produced by LangParser#repetitionMatch.
    def enterRepetitionMatch(self, ctx:LangParser.RepetitionMatchContext):
        pass

    # Exit a parse tree produced by LangParser#repetitionMatch.
    def exitRepetitionMatch(self, ctx:LangParser.RepetitionMatchContext):
        pass


    # Enter a parse tree produced by LangParser#literal.
    def enterLiteral(self, ctx:LangParser.LiteralContext):
        pass

    # Exit a parse tree produced by LangParser#literal.
    def exitLiteral(self, ctx:LangParser.LiteralContext):
        pass


    # Enter a parse tree produced by LangParser#numericLiteral.
    def enterNumericLiteral(self, ctx:LangParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by LangParser#numericLiteral.
    def exitNumericLiteral(self, ctx:LangParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by LangParser#bigintLiteral.
    def enterBigintLiteral(self, ctx:LangParser.BigintLiteralContext):
        pass

    # Exit a parse tree produced by LangParser#bigintLiteral.
    def exitBigintLiteral(self, ctx:LangParser.BigintLiteralContext):
        pass


    # Enter a parse tree produced by LangParser#identifierName.
    def enterIdentifierName(self, ctx:LangParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by LangParser#identifierName.
    def exitIdentifierName(self, ctx:LangParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by LangParser#reservedWord.
    def enterReservedWord(self, ctx:LangParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by LangParser#reservedWord.
    def exitReservedWord(self, ctx:LangParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by LangParser#keyword.
    def enterKeyword(self, ctx:LangParser.KeywordContext):
        pass

    # Exit a parse tree produced by LangParser#keyword.
    def exitKeyword(self, ctx:LangParser.KeywordContext):
        pass


    # Enter a parse tree produced by LangParser#eos.
    def enterEos(self, ctx:LangParser.EosContext):
        pass

    # Exit a parse tree produced by LangParser#eos.
    def exitEos(self, ctx:LangParser.EosContext):
        pass


