
from plang.parser.LangParser import LangParser
     
from plang.parser.LangListener import LangListener     

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

class TreeGenerator(LangListener):

    def __init__(self, factory, *args, **kwargs):
        super(TreeGenerator, self).__init__(*args, **kwargs)
        
        self.f = factory
        
        self.stack = []

    def getFullTree(self):
        return self.stack.pop()

    def exitProgram(self, ctx:LangParser.ProgramContext):
        elements = [ e for e in self.stack if e is not None ]
        self.stack = []
        self.stack.append( self.f.createProgram(elements)  )

    def exitLiteral(self, ctx:LangParser.LiteralContext):

        if ctx.null   :
            e = self.f.createNullLiteral(ctx.getText())
            self.stack.append(e)

        if ctx.boolean:
            e = self.f.createBooleanLiteral(ctx.getText())
            self.stack.append(e)

        if ctx.string :
            e = self.f.createStringLiteral(ctx.getText())
            self.stack.append(e)

    def exitNumericLiteral(self, ctx:LangParser.NumericLiteralContext):
        e = self.f.createNumericLiteral(ctx.getText())
        self.stack.append(e)


    def exitArgumentsExpression(self, ctx:LangParser.ArgumentsExpressionContext):
        arguments = self.stack.pop()
        e         = self.stack.pop()
        
        e = self.f.createArgumentsExpression(e, arguments)
        self.stack.append(e)

    def exitArguments(self, ctx:LangParser.ArgumentsContext):
        if ctx.args is not None:
            args = self.stack.pop()
        else:
            args = []
        self.stack.append(args)

    def exitArgumentslist(self, ctx:LangParser.ArgumentslistContext):

        num = ctx.getChildCount()
        if num > 1:
             n_exprs = (num + 1) // 2

             args = self.stack[-n_exprs:]

             self.stack = self.stack[:-n_exprs]
        elif num == 1:
             a = self.stack.pop()
             args = [a]
        else:
             args = []

        self.stack.append(args)

    def exitIdentifierExpression(self, ctx:LangParser.IdentifierExpressionContext):
        e = self.f.createIdentifier(ctx.getText())
        self.stack.append(e)

    def exitExpressionSequence(self, ctx:LangParser.ExpressionSequenceContext):
        
        num = ctx.getChildCount()
        
        # EOS
        if self.stack[-1] == None:
            self.stack.pop()
            num -= 1

        if num > 1:
            n_exprs = (num + 1) // 2
            
            elements = self.stack[-n_exprs:]
            self.stack = self.stack[:-n_exprs]
            
            e = self.f.createExpressionSequence(elements)
            
            self.stack.append(e)
        else:
            e = self.stack.pop()
            e = self.f.createExpressionSequence([e])
            self.stack.append(e)

    def exitExpressionStatement(self, ctx:LangParser.ExpressionStatementContext):
        e = self.stack.pop()
        e = self.f.createExpressionStatement(e)
        self.stack.append(e)

    def exitArrayLiteral(self, ctx:LangParser.ArrayLiteralContext):
        if ctx.elements is not None:
            elements = self.stack.pop()
        else:
            elements = []

        e = self.f.createArrayLiteral(elements)
        self.stack.append(e)

    def exitArrayElementsList(self, ctx:LangParser.ArrayElementsListContext):

        num = ctx.getChildCount()
        if num > 1:
            n_exprs = (ctx.getChildCount() + 1) // 2
            
            elements = self.stack[-n_exprs:]
       
            self.stack = self.stack[:-n_exprs]
        elif num == 1:
            e = self.stack.pop()
            elements = [e]
        else:
            elements = []

        self.stack.append( elements )

    def exitMemberIndexExpression(self, ctx:LangParser.MemberIndexExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()        
        e = self.f.createMemberIndex(e1, e2)
        self.stack.append(e)

    def exitMemberDotExpression(self, ctx:LangParser.MemberDotExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()        
        e = self.f.createMemberDot(e1,e2)
        self.stack.append(e)

    def exitUnaryPlusExpression(self, ctx:LangParser.UnaryPlusExpressionContext):
        e = self.stack.pop()
        e  = self.f.createUnaryPlusExpression(e)
        self.stack.append(e)

    def exitUnaryMinusExpression(self, ctx:LangParser.UnaryMinusExpressionContext):
        e = self.stack.pop()
        e  = self.f.createUnaryMinusExpression(e)
        self.stack.append(e)

    def exitBitNotExpression(self, ctx:LangParser.BitNotExpressionContext):
        e = self.stack.pop()
        e  = self.f.createBitNotExpression(e)
        self.stack.append(e)

    def exitNotExpression(self, ctx:LangParser.NotExpressionContext):
        e = self.stack.pop()
        e  = self.f.createNotExpression(e)
        self.stack.append(e)
        
    def exitPowerExpression(self, ctx:LangParser.AdditiveExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createPowerExpression(e1,e2)
        self.stack.append(e)

    def exitMultiplicativeExpression(self, ctx:LangParser.AdditiveExpressionContext):
        etype = ctx.etype.text
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createMultiplicativeExpression(etype,e1,e2)
        self.stack.append(e)

    def exitAdditiveExpression(self, ctx:LangParser.AdditiveExpressionContext):
        etype = ctx.etype.text
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createAdditiveExpression(etype, e1,e2)
        self.stack.append(e)

    def exitBitShiftExpression(self, ctx:LangParser.AdditiveExpressionContext):
        etype = ctx.etype.text
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createBitShiftExpression(etype,e1,e2)
        self.stack.append(e)    

    def exitRelationalExpression(self, ctx:LangParser.RelationalExpressionContext):
        etype = ctx.etype.text
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createRelationalExpression(etype, e1,e2)
        self.stack.append(e) 

    def exitEqualityExpression(self, ctx:LangParser.RelationalExpressionContext):
        etype = ctx.etype.text
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createEqualityExpression(etype, e1,e2)
        self.stack.append(e) 

    def exitBitAndExpression(self, ctx:LangParser.BitAndExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createBitAndExpression(e1,e2)
        self.stack.append(e) 

    def exitBitXOrExpression(self, ctx:LangParser.BitOrExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createBitXOrExpression(e1,e2)
        self.stack.append(e) 

    def exitBitOrExpression(self, ctx:LangParser.BitOrExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createBitOrExpression(e1,e2)
        self.stack.append(e) 

    def exitLogicalAndExpression(self, ctx:LangParser.LogicalAndExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createLogicalAndExpression(e1,e2)
        self.stack.append(e) 

    def exitLogicalOrExpression(self, ctx:LangParser.LogicalAndExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createLogicalOrExpression(e1,e2)
        self.stack.append(e) 

    def exitTernaryExpression(self, ctx:LangParser.TernaryExpressionContext):
        e3 = self.stack.pop()
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createTernaryExpression(e1,e2,e3)
        self.stack.append(e) 
        
    #-------------------------------------------------------------------
    # STATEMENS
    #-------------------------------------------------------------------

    def exitContinueStatement(self, ctx:LangParser.ContinueStatementContext):
            e = self.f.createContinueStatement()
            self.stack.append(e)

    def exitBreakStatement(self, ctx:LangParser.BreakStatementContext):
            e = self.f.createBreakStatement()
            self.stack.append(e)

    def exitAssignmentExpression(self, ctx:LangParser.AssignmentExpressionContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createAssignmentExpression(e1,e2)
        self.stack.append(e)

    def exitReturnStatement(self, ctx:LangParser.StatementContext):
        
        if ctx.expr is not None:
            e = self.stack.pop()
        else:
            e = None
        self.stack.append(e)

    def exitBlock(self, ctx:LangParser.BlockContext):

        if ctx.stmts is not None:
            elements = self.stack.pop()
        else:
            elements = []
        
        e = self.f.createBlock(elements)
        self.stack.append(e)

    def exitEmptyStatement(self, ctx:LangParser.EmptyStatementContext):
        self.stack.append(None)

    def exitIfStatement(self, ctx:LangParser.IfStatementContext):
        if ctx.s2 is not None:
            s2 = self.stack.pop()
        else:
            s2 = None
        s1 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createIf(e1,s1,s2)
        self.stack.append(e)

    def exitDoStatement(self, ctx:LangParser.DoStatementContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createDoWhileStatement(e1, e2)
        self.stack.append(e)

    def exitWhileStatement(self, ctx:LangParser.WhileStatementContext):
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createWhileStatement(e1, e2)
        self.stack.append(e)

    #------------------------------------------------------------------#
    #                                                                  #
    #------------------------------------------------------------------#
    
    def exitObjectLiteral(self, ctx:LangParser.ObjectLiteralContext):
        if ctx.ol_list is not None:
            e = self.stack.pop()
        else:
            e = []
        
        e = self.f.createObjectLiteral(e)
        self.stack.append(e)

    def exitObjectLiteralList(self, ctx:LangParser.ObjectLiteralContext):
        
        num = ctx.getChildCount()
        if num > 1:
            n_exprs = (ctx.getChildCount() + 1) // 2
            
            elements = self.stack[-n_exprs:]
       
            self.stack = self.stack[:-n_exprs]
        elif num == 1:
            e = self.stack.pop()
            elements = [e]
        else:
            elements = []
        
        self.stack.append(elements)

    def exitPropertyExpressionAssignment(self, ctx:LangParser.PropertyExpressionAssignmentContext):

        ctype = ctx.ctype.getChild(0).getText()
        
        e2 = self.stack.pop()
        e1 = self.stack.pop()
        e  = self.f.createPropertyAssignment(ctype, e1,e2)
        self.stack.append(e)

    def exitPropertyName(self, ctx:LangParser.PropertyNameContext):
        
        self.stack.pop()
        
        text = ctx.getText()
        
        e = self.f.createIdentifier(text)

        self.stack.append(e)

    def exitPropertyNameString(self, ctx:LangParser.PropertyNameStringContext):

        e = self.f.createStringLiteral(ctx.getText())
        self.stack.append(e)
        
    #------------------------------------------------------------------#
    #                                                                  #
    #------------------------------------------------------------------#

    def exitIdentifierName(self, ctx:LangParser.IdentifierExpressionContext):
        e = self.f.createIdentifier(ctx.getText())
        self.stack.append(e)

    def exitStatementList(self, ctx:LangParser.StatementListContext):
        num = ctx.getChildCount()

        if num > 1:
            n_exprs = num #(ctx.getChildCount() + 1) // 2
            
            elements = self.stack[-n_exprs:]
       
            self.stack = self.stack[:-n_exprs]
        elif num == 1:
            e = self.stack.pop()
            elements = [e]
        else:
            elements = []

        self.stack.append(elements)

    #------------------------------------------------------------------#
    # MATCH                                                            #
    #------------------------------------------------------------------#

    def exitMatchStatement(self, ctx:LangParser.MatchStatementContext):

        match = self.stack.pop()
        e = self.f.createMatchStatement(match)
        self.stack.append(e)
        
    # Exit a parse tree produced by LangParser#matchBody.
    def exitMatchBody(self, ctx:LangParser.MatchBodyContext):

        prematch = None
        match    = None
        onmatch  = None
        
        #num = ctx.getChildCount()
        #if num > 1:
        #    action = self.stack.pop()
        #match = self.stack.pop()
        #e = self.f.createMatchBody(match, action)
        
        if ctx.onmatch_stm:

            #onmatch = self.stack.pop()
            
            elements = self.stack.pop()
            onmatch = self.f.createBlock(elements)

        
        match = self.stack.pop()
           
        if ctx.prematch_stm:
            #prematch = self.stack.pop()        

            elements = self.stack.pop()
            prematch = self.f.createBlock(elements)

        
        e = self.f.createMatchBody(prematch, match, onmatch)
        
        self.stack.append(e)

    def exitInputMatch(self, ctx:LangParser.InputMatchContext):

        options = []
        
        if ctx.options:
             num = ctx.options.getChildCount()

             while num:
                 option_val = self.stack.pop()
                 option_name = self.stack.pop()
                 options.append( (option_name, option_val) )
                 num -= 2

             options.reverse()

        arguments = self.stack.pop()
        e = self.f.createInputMatch(arguments, options)
        self.stack.append(e)
        
    def exitRepetitionMatch(self, ctx:LangParser.RepetitionMatchContext):
        rtype = ctx.rtype.text
        e = self.stack.pop()
        e = self.f.createRepetitionMatch(rtype, e)
        self.stack.append(e)

    def exitSequenceMatch(self, ctx:LangParser.SequenceMatchContext):
        elements = self.stack.pop()
        
        if len(elements) == 1:
            self.stack.append(elements[0])
            return
        
        e = self.f.createSequenceMatch(elements)
        self.stack.append(e)

    def exitSequenceList(self, ctx:LangParser.SequenceListContext):
    
        num = ctx.getChildCount()
        if num > 1:
            #n_exprs = (ctx.getChildCount() + 1) // 2
            
            n_exprs = ctx.getChildCount()
            
            elements = self.stack[-n_exprs:]
       
            self.stack = self.stack[:-n_exprs]
        elif num == 1:
            elements = [ self.stack.pop() ]
        else:
            elements = []
    
        self.stack.append(elements)

    def exitChoiceMatch(self, ctx:LangParser.ChoiceMatchContext):
        elements = self.stack.pop()
        
        if len(elements) > 1:
            e = self.f.createChoiceMatch(elements)
        else:
            e = elements[0]
        self.stack.append(e)

    def exitChoiceList(self, ctx:LangParser.ChoiceListContext):
        num = ctx.getChildCount()
        if num > 1:
            n_exprs = (ctx.getChildCount() + 1) // 2
            
            elements = self.stack[-n_exprs:]
       
            self.stack = self.stack[:-n_exprs]
        elif num == 1:
            elements = [ self.stack.pop() ]
        else:
            elements = []

        self.stack.append(elements)

    #
    # optional { <M> } 
    #
    def exitOptionalMatch(self, ctx:LangParser.OptionalMatchContext):
        e = self.stack.pop()
        e = self.f.createOptionalMatch(e)
        self.stack.append(e)


