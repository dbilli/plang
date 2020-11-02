# plang: A Patterns-Recognition language (for logs analysis)

Plang is a simple language for log analysis with pattern-matching statements inspired by *Regular Expressions*.

Basic ideas:

* process JSON-documents
* Support classic patter-matching operators : single match, repetition, alternatives, ecc.

This project provides a pLang implementation for python (based on Antlr4).

**Basic example**

This simple plang program matches a sequence of login/logout actions.

    count = 0;
    
    while (1) {
        match 
            (
                {"type": "login" , "username": "foo" } 
                {"type": "logout", "username": "foo" }          
            ) 
            action {
                count = count + 1;
            }

## The Language

### Literals

#### The *null* value

    null

#### Booleans

    true
    false

#### Strings

Strings can be double-quoted or single-quoted and can contain escape sequence 

    "The quick brown fox jumps over the lazy dog"
    
    'Hello world'
    
    "This string contains \"double-quotes\""

#### Integers Numbers

* Decimal

    10
    2e-10

* Hexadecimal

    0xABCDEF
    x10

* Octals

    0755

### Expressions 

TODO

### Classic statements

#### Assign statement

    var = <expr> ;

#### If / then / else

    if ( <expr> ) 
        <statement 1>

    if ( <expr> ) 
        <statement 1>
    else
        <statement 2>

#### Loop statements

    while ( <expr> ) {
        <statement 1>
    }

    do {
        <statement>
    } while ( <expr> )

### Matching statements

A matching statement starts with:

    match <matching statement> ;

A matching statement can be:

* basic match                  
* sequence match              
* repetitionMatch            
* choice match                
* optional match             

#### basic match               

Match input JSON-data:

    match 
          <match statement>
    ;


The *match statement* must be a valid expression.

The *statement* is executed when the current input matches the *match expression*.

Examples:

    match 
        ( 1 ) action { print("Received integer value 1 from input"); }
    ;
    
    match 
        ( [1,2,3] ) action { print("Received an array from input"); }
    ;
    
    match 
        ( { "key1":"value1", "key2": "value2" } )
    ;
    
#### sequence match       

A sequence of *match statemens* between braces:

    { <match statement1>,  <match statement2>, ... } 
    
    { <match statement1>,  <match statement2>, ... } action { <statement> }

Examples

    match
         (
             1
             2 action { print("almost done"); }
             3
         )
         action { 
             print("Matched three integers sequence"); 
         }
    ;

#### repetition match  

These statementes correspond to the regula expression patters e* or e+ : 

    repetition * { <match statement> } 
    repetition * { <match statement> }  action  { <statement> }
    
    repetition + { <match statement> } 
    repetition + { <match statement> }  action  { <statement> }

Example

    match
         repetition + { input(1) } action { print("Matched three integers sequence"); }
    ;
    
#### choice match                      

The classic *choice* pattern pattern (e1|e2):

    choice { 
        case <match statement 1>
        case <match statement 2>
        case ...
    }

Example:

    match 
        choice { 
           case input(1) action { print("first"); } 
           case input(2) action { print("second"); } 
           case input(2) action { print("thired"); }
        }
    ;
    
#### optionalMatch                  

The e? pattern:

    optional { <match statement> } 
    optional { <match statement> } action { <statement> }  

Example:

    match
        {
          input(1),
          optional { input(2) } ,
          input(3)
        }
   ;


## A Full Example

Imagine a sequence of logs in JSON format:

    { "timestamp": 1587165530, "type": "login"  , "user": "foo" } 
    { "timestamp": 1587165530, "type": "logout" , "user": "foo" } 
    { "timestamp": 1587165530, "type": "logout" , "user": "foo" } 
    ...

With pLang you can write a OPEN/CLOSE connection pattern matching program:

    match {
        input( { type: "login" } )                                action { print("Login for user " + data["user"] }
        ,
        choice {
            case 
                input( 
                    { 
                        type      : "logout", 
                        user      : prev["user"], 
                        timestamp < prev["timestamp"] + 60 
                    } 
                )                                                 action { print("Logout of user:" + data["user"]); }
           case
               input(
                    { 
                        type      : "expired", 
                        user      : prev["user"], 
                    } 
               )                                                 action { print("expired connection of user:" + data["user"]); }
        }                                                        action { print("Pattern matched. "]); }
    } 
    action {
       print("Mached data: ");
       i = 0
       while (i < len(matched)) {
          print(matched[i]);
          i = i + 1;
       }
    }

## Python API

### Basic parsing

    import sys
    from plang.parsing import parse_string

    parsed_tree = parse_string(sys.argv[1])
    
    print(parsed_tree.format())


### Customized parsing and syntax trees

You can customize the parsed tree by implementing your custom version of the _BaseExprFactory_ :

    from plang.parsing.nodes import *
    from plang.parsing.nodes import BaseExprFactory
    
    class CustomFactory(BaseExprFactory):
        ... override ...

    parsed_tree = parse_string(s, tree_factory=CustomFactory() )
    
    print(parsed_tree.format())
    
    return compiled


## Authors

* **Diego Billi**

## License

This project is licensed under the GNUv3 License - see the [LICENSE](LICENSE) file for details



