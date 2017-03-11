# API SimplePOS - POSXML

  The API can be divided into the folowing sections:

  * [Card reading functions](#card_reading_functions)
     * [getcard](#getcard)
     * [readcard](#readcard)
     * [input_transaction](#input_transaction)
  * [Flow control](#flow_control)
     * [execute](#execute)
     * [exit](#exit)
  * [Type conversions](#type_conversions)
     * [inttostring](#inttostring)
     * [stringtoint](#stringtoint)
     * [inttobase](#inttobase)
     * [basetoint](#basetoint)
     * [hexencode](#hexencode)
     * [hexdecode](#hexdecode)
  * [Cryptography](#cryptography)
     * [crc](#crc)
     * [crc_ccitt](#crc_ccitt)
     * [cipher_block](#cipher_block)
     * [decipher_block](#decipher_block)
     * [lrc](#lrc)
     * [xor](#xor)
  * [Date and Time](#date_and_time)
     * [getdatetime](#getdatetime)
     * [time_operation](#time_operation)
  * [Filesystem](#filesystem)
     * [listfiles](#listfiles)
     * [rename](#rename)
     * [filesize](#filesize)
     * [filesystem_space](#filesystem_space)
     * [filesystem_total](#filesystem_total)
     * [filesystem_used](#filesystem_used)
     * [filesystem_free](#filesystem_free)
     * [filesystem_countfiles](#filesystem_countfiles)
     * [open](#open)
     * [read](#read)
     * [write](#write)
     * [close](#close)
     * [dbread](#dbread)
     * [dbread_index](#dbread_index)
     * [dbupdate](#dbupdate)
     * [delete](#delete)
     * [downloadfile](#downloadfile)
  * Network and communications
  * Printing and printer control
  * String handling
  * User interface
  * Utilities
  
## Card Reading Functions

  Card data input.

### getcard 

  Reads the card magnetic stripe (track 2).
 
    string getcard(string firstmessage, int maximum, int minimum, int secondmessage)

  POSXML **getcardvariable** call: 
  [https://docs.cloudwalk.io/en/posxml/commands/getcardvariable]

### readcard

  Reads the card magnetic stripe (track 2) or the card number entered via keyboard.

    int readcard(string &cardvariable, string &keyvariable, int timeout)

  POSXML **system.readcard** call: 
  [https://docs.cloudwalk.io/en/posxml/commands/system.readcard]

### input_transaction

  Reads the card data from magnetic stripe, EMV, contactless reader or keyboard.

    int input_transaction(string inputtype, string keyboard, 
                          string &cardvariable, int timeout, 
                          string &keyvariable)`
  
  POSXML **system.inputtransaction** call:
  [https://docs.cloudwalk.io/en/posxml/commands/getcardvariable]
  
## Flow Control
  
  Program execution flow control.  
  
### execute 
  Calls a POSXML module directly. In most cases, it can be replaced by a `modulecall` instruction.  
  
    void execute(string filename)

  POSXML **execute** call:
  [https://docs.cloudwalk.io/en/posxml/commands/execute]
  
### exit
  Terminates the application
  
    void exit()

  POSXML **exit** call:
  [https://docs.cloudwalk.io/en/posxml/commands/exit]
  
## Type Conversions

  Conversions of data type and numeric base.

### inttostring
  Converts an integer value to a string representation.

    string inttostring(int variableinteger)
    
  POSXML **inttostring** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inttostring]

### stringtoint
  Converts a string value to an integer representation

     int stringtoint(string variablestring)
     
  POSXML **stringtoint** call:     
  [https://docs.cloudwalk.io/en/posxml/commands/stringtoint]

### inttobase
  Converts an integer value to the ASCII representation on requested base (2, 8, 10 or 16)

     string intotobase(int base, int number, int sizereturn)
     
  POSXML **integerconvert** call:
  [https://docs.cloudwalk.io/en/posxml/commands/integerconvert]
     
### basetoint
  Converts an ASCII representation of a number to integer, according with the 
  requested base (2, 8, 10 or 16) 
 
    int basetoint(int base, string number)
    
  POSXML **convert.toint** call:
  [https://docs.cloudwalk.io/en/posxml/commands/convert.toint]

### hexencode
  Encode the bytes of a string into hexadecimal ASCII representation.

    string hexencode(string string)
    
  POSXML **string.tohex** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.tohex]


### hexdecode
  Decode an hexadecimal ASCII string into a byte string.

    string hexdecode(string string)
    
  POSXML **string.fromhex** call: 
  [https://docs.cloudwalk.io/en/posxml/commands/string.fromhex]
  

## Cryptography

  Cryptography related calls.

### crc
  Calculates the CRC from a byte string.

    int crc(string buffer, int size)
    
  POSXML **crypto.crc** call, with **type** parameter set to **"CRC"**: 
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.crc]
  
### crc_ccitt
  Calculates de CRC from a byte string, using the CRC-CCITT algorithm.
  
    int crc_ccitt(string buffer, int size)
    
  POSXML **crypto.crc** call, with **type** parameter set to **"CRC-CCITT"**.
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.crc]
    
### cypher_block
  Ciphers a block of 8 bytes using the requested algorithm. 
  The allowed algorithms (parameter _cryptotype_) are:

  * DES
  * 3DES
  * 3DESTripleLenght
  * NEWDES


     string cypher_block(string cryptotype, string key, string message)

  POSXML **crypto.encryptdecrypt** call with **type** parameter set to **"0"** (cypher).
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.encryptdecrypt]
      
### decypher_block
  Deciphers a block of 8 bytes using the requested algorithm. 
  The allowed algorithms (parameter _cryptotype_) are:

  * DES
  * 3DES
  * 3DESTripleLenght
  * NEWDES


     string decypher_block(string cryptotype, string key, string message)

  POSXML **crypto.encryptdecrypt** call with **type** parameter set to **"1"** (decypher).
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.encryptdecrypt]
      
### lrc
  Calculates the LRC from a byte string.

    string lrc(string buffer, int size)
    
  POSXML **crypto.lrc** call:  
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.lrc]
     
### xor
  Calculates the binary XOR between two hexadecimal strings.
      
    string xor(string buffer1, string buffer2, int size)
          
  POSXML **crypto.xor** call:
  [https://docs.cloudwalk.io/en/posxml/commands/crypto.xor]
          
  ## Date and Time
  Date and time operations.
    
  ### getdatetime 
  Gets the terminal current date and time.

    string getdatetime(string format)
    
  POSXML **getdatetime** call:
  [https://docs.cloudwalk.io/en/posxml/commands/getdatetime]

### time_operation
  Arithmetic operations over date and time. The call in POSXML is 
  very confusing, and the first two parameters must be variable 
  references, even if the requested operation will not use the values.

    int time_operation(string &date, string &greaterdate, 
                       string operation, string type, int value)

  POSXML **time.calculate** call: 
  [https://docs.cloudwalk.io/en/posxml/commands/time.calculate]

## Filesystem
  Functions related to reading and writing data to permanten storage.

### listfiles
  Lists a directory contents and writes the list into the "_listfilename_" file.

    int listfiles (string dir, string listfilename)
    
  POSXML **filesystem.listfiles** call:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.listfiles]
    
### rename
  Renames a file.
    
    int rename(string oldname, string newname)
    
  POSXML **filesystem.renamefile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.renamefile]
    
### filesize
  Gets the size of a file in bytes.
    
    int filesize(string filename)
    
  POSXML **filesystem.filesize** call:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.filesize]
    
### filesystem_space
  Direct call to filesystem.stape POSXML tag.

    int filesystem_space (string dir, stirng type)
    
  POSXML **filesystem.space** call:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.space]
    
### filesystem_total
  Size of the devices filesystem. 

    int filesystem_total (string dir)
    
  POSXML **filesystem.space** call, with **type** parameter set to **"total"**:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.space]
    
### filesystem_used
  Total used space in the devices filesystem. 

    int filesystem_used (string dir)
    
  POSXML **filesystem.space** call, with **type** parameter set to **"used"**:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.space]
    
### filesystem_free
  Total free space in the devices filesystem. 

    int filesystem_free (string dir)
    
  POSXML **filesystem.space** call, with **type** parameter set to **"free"**:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.space]
    
### filesystem_countfiles
  Number of files in device's filesystem. 

    int filesytem_countfiles (string dir)
    
  POSXML **filesystem.space** call, with **type** parameter set to **"countfiles"**:
  [https://docs.cloudwalk.io/en/posxml/commands/filesystem.space]
    
### open
  Opens a file in the device's filesystem, returning a handle to 
  it or a negative value in case of error.
    
    int open(string filename, string mode)
    
  POSXML **file.open** call:
  [https://docs.cloudwalk.io/en/posxml/commands/file.open]

### read
  Read bytes from a file, getting them into a hexadecimal string.

    int read(int handle, int size, string &variablebuffer)

  POSXML **file.read** call:
  [https://docs.cloudwalk.io/en/posxml/commands/file.read]
    
### write
  Write bytes to a file. The buffer variable must contain an hexadecimal string.

    int write(int handle, int size, string variablebuffer)

  POSXML **file.write** call:
  [https://docs.cloudwalk.io/en/posxml/commands/file.write]
    
### close
  Closes an opened file.

    int close(int handle)
    
  POSXML **file.close** call:
  [https://docs.cloudwalk.io/en/posxml/commands/file.close]
 
### dbread
  Reads an entry from a POSXML-DB file (key=value).
    
    string dbread(string filename, string key)
    
  POSXML **readfile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/readfile]
    
### dbread_index
  Reads an entry from a POSXML-DB file (key=value) by 
  position (line) in the file.
    
    string dbread_index(string filename, int index, 
                        string &variablekey, string &variablevalue)

  POSXML **readfilebyindex** call:
  [https://docs.cloudwalk.io/en/posxml/commands/readfilebyindex]

### dbupdate
  Updates an entry in a POSXML-DB file (key=value).
 
    void dbupdate(string filename, string key, string value)
    
  POSXML **editfile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/editfile]
    
### delete
  Removes a file from the device's storage.
    
    void delete(string filename)
      
  POSXML **deletefile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/deletefile]

### downloadfile
   Downloads a file from the CloudWalk platform
   
     int downloadfile(string filename, string remotepath)
     
   POSXML **downloadfile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/downloadfile]
   