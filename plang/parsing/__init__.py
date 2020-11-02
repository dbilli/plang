
import antlr4

from plang.parser.utils import stringToAST as __stringToAST

from plang.parsing.nodes import BaseExprFactory
from plang.parsing.generator import TreeGenerator

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

def __fromASTToTree(ast, tree_factory=None):
    
    if not tree_factory:
        tree_factory =  BaseExprFactory()
    
    treegenerator = TreeGenerator( tree_factory )
    
    walker = antlr4.ParseTreeWalker()
    walker.walk(treegenerator, ast)
    
    parsed_tree = treegenerator.getFullTree()
    
    return parsed_tree

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#

def parse_string(s, tree_factory=None):
    
    #
    # Parse input
    #
    ast = __stringToAST(s)

    #
    # Get tree
    #
    tree = __fromASTToTree(ast, tree_factory=tree_factory)
    
    return tree

#----------------------------------------------------------------------#
#                                                                      #
#----------------------------------------------------------------------#


if __name__ == "__main__":

    import sys

    tree = parse_string(sys.argv[1])
    
    print(tree.format())
