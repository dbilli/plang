# Generated from Lang.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#program.
    def visitProgram(self, ctx:LangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sourceElement.
    def visitSourceElement(self, ctx:LangParser.SourceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx:LangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#block.
    def visitBlock(self, ctx:LangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#statementList.
    def visitStatementList(self, ctx:LangParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#emptyStatement.
    def visitEmptyStatement(self, ctx:LangParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expressionStatement.
    def visitExpressionStatement(self, ctx:LangParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ifStatement.
    def visitIfStatement(self, ctx:LangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#DoStatement.
    def visitDoStatement(self, ctx:LangParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#WhileStatement.
    def visitWhileStatement(self, ctx:LangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#continueStatement.
    def visitContinueStatement(self, ctx:LangParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#breakStatement.
    def visitBreakStatement(self, ctx:LangParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sourceElements.
    def visitSourceElements(self, ctx:LangParser.SourceElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:LangParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arrayElementsList.
    def visitArrayElementsList(self, ctx:LangParser.ArrayElementsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arrayElement.
    def visitArrayElement(self, ctx:LangParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#objectLiteral.
    def visitObjectLiteral(self, ctx:LangParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#objectLiteralList.
    def visitObjectLiteralList(self, ctx:LangParser.ObjectLiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:LangParser.PropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#propertyName.
    def visitPropertyName(self, ctx:LangParser.PropertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#arguments.
    def visitArguments(self, ctx:LangParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#argumentslist.
    def visitArgumentslist(self, ctx:LangParser.ArgumentslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#argument.
    def visitArgument(self, ctx:LangParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expressionSequence.
    def visitExpressionSequence(self, ctx:LangParser.ExpressionSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:LangParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:LangParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#PowerExpression.
    def visitPowerExpression(self, ctx:LangParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:LangParser.ObjectLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:LangParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#NotExpression.
    def visitNotExpression(self, ctx:LangParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:LangParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:LangParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:LangParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:LangParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:LangParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:LangParser.BitXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:LangParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:LangParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:LangParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:LangParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:LangParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:LangParser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:LangParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:LangParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:LangParser.MemberDotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:LangParser.MemberIndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:LangParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:LangParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:LangParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#matchStatement.
    def visitMatchStatement(self, ctx:LangParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#repetitionMatchStatement.
    def visitRepetitionMatchStatement(self, ctx:LangParser.RepetitionMatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sequenceMatchStatement.
    def visitSequenceMatchStatement(self, ctx:LangParser.SequenceMatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#choiceMatchStatement.
    def visitChoiceMatchStatement(self, ctx:LangParser.ChoiceMatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#optionalMatchStatement.
    def visitOptionalMatchStatement(self, ctx:LangParser.OptionalMatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#basicMatchStatement.
    def visitBasicMatchStatement(self, ctx:LangParser.BasicMatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#matchAction.
    def visitMatchAction(self, ctx:LangParser.MatchActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sequenceMatch.
    def visitSequenceMatch(self, ctx:LangParser.SequenceMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#sequenceList.
    def visitSequenceList(self, ctx:LangParser.SequenceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#choiceMatch.
    def visitChoiceMatch(self, ctx:LangParser.ChoiceMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#choiceList.
    def visitChoiceList(self, ctx:LangParser.ChoiceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#choiceElement.
    def visitChoiceElement(self, ctx:LangParser.ChoiceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#repetitionMatch.
    def visitRepetitionMatch(self, ctx:LangParser.RepetitionMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#optionalMatch.
    def visitOptionalMatch(self, ctx:LangParser.OptionalMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#optionalArg.
    def visitOptionalArg(self, ctx:LangParser.OptionalArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#basicMatch.
    def visitBasicMatch(self, ctx:LangParser.BasicMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#inputMatch.
    def visitInputMatch(self, ctx:LangParser.InputMatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#literal.
    def visitLiteral(self, ctx:LangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#numericLiteral.
    def visitNumericLiteral(self, ctx:LangParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bigintLiteral.
    def visitBigintLiteral(self, ctx:LangParser.BigintLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#identifierName.
    def visitIdentifierName(self, ctx:LangParser.IdentifierNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#reservedWord.
    def visitReservedWord(self, ctx:LangParser.ReservedWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#keyword.
    def visitKeyword(self, ctx:LangParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#eos.
    def visitEos(self, ctx:LangParser.EosContext):
        return self.visitChildren(ctx)



del LangParser