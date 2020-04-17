# plang: Patterns recognition Language

Plang is a simple patterns recognition language for JSON data stream inspired by Regular Expressions.

This project provides parser for pLang implemented with Antlr4. 

## Introduction

Image you have a stream lof "session" logs in JSON format:

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


## 1. Syntax

TODO


## Authors

* **Diego Billi**

## License

This project is licensed under the GNUv3 License - see the [LICENSE](LICENSE) file for details


