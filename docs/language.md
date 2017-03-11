# SimplePOS Language

  The SimplePOS language is a "C" style DSL created to develop
  applications fot the CloudWalk platform using, generating 
  POSXML programs from SimplePOS source files.
  
  The language is structured, and inherits the limitations of
  the POSXML platform.
  
  For more information on the platform, see the 
  [CloudWalk](https://docs.cloudwalk.io/en/posxml/structure)
  documentation.
  
  This document is rather incomplete, and you can learn more from the
  tests and examples than from here. :-(
  
  The test code are in the directory test/integrated/compiler/data, and
  the exemples are in the examples directory.
  
  
## Language Structure
  
  A program in POSXML is a **module**, and is's composed by 
  the main program body and functions.
  
  The main program body is all that is specified outside function
  definitions, and if the program is composed from more then one
  source file, all the code of the main program body in all the 
  source files are concatenated in the final program, in the order
  they where passed to the linker.
  
  All variables declared in the main program body are globals.
  
  Unlinke POSXML itself, the SimplePOS functions have local scope
  for variables, and the linker manages the variable names to ensure
  no side effects of different functions using the name name for 
  local variables.
    
### The main Module file
  The "module" command specifies a starting point for a SimplePOS
   program, and it's advised that the module name be the same of the
   program name in the CloudWalk platform, so the modulecall command
   will work seamlessly.
   
   The minimal structure of the module is:
   
     module mod_name ;
     /* 
     comment
      it can have lots of statements and function definitions.
     */
     exit; // exit statement, optional 
     
### Rules
  TODO: this section must be rewritten.
   
  * Comments can be inserted in the multiline form (`/* */`) or in the
     single line form (`// to the end of the line`)
  * There are only two data types allowed: **int** and **string**.
  * Variables must be declared before utilized
  * Variables are declared like in "C", but can't be initialized
    on declaration.
  * String constants are defined using double quotes (`"string"`)
  
### Flow Control
  
  * Functions are defined only in the global scope (it's not possible
     to define a function inside a function)
  * Although it's possible to make recursive function calls, it's not
     advised, because of the lack of stack control in POSXML (local 
     variables will be rewritten in the recursive calls)
  * `if / else` blocks will work as usual
  * `for` and `while` loops have a syntac like "C" and will work as
     usual too.
  * increment and decrement operators will work like "C" prefixed 
     increment and decrement, unregarded the way they appear in the
     source (prefixed or postfixed).
  * the return instruction in functions **does not work as 
    expected yet**: it will stablish the return value of the
    function but will not perform the immediate return. The function
    will continue to execute after the return statement until the
    last line.
     