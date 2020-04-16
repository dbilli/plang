
if __name__ == "__main__":
    
    import sys
    
    from plang.parser import utils
    
    source_code = sys.stdin.read().strip()
    
    print("----------SOURCE PROGRAM--------")    
    print(source_code)
    print("---------------AST--------------")
    
    utils.printAST(source_code)
    
