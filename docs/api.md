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
  * [Network and communications](#network_and_communications)
     * [predial](#predial)
     * [preconnect](#preconnect)
     * [initmodem](#initmodem)
     * [shutdownmodem](#shutdownmodem)
     * [gprs_signal_level](#gprs_signal_level)
     * [disconnect](#disconnect)
     * [ping](#ping)
     * [send](#send)
     * [receive](#receive)
  * [Printing and printer control](#printing_and_printer_control)
     * [print](#print)
     * [printbig](#printbig)
     * [printbitmap](#printbitmap)
     * [printbarcode](#printbarcode)
     * [checkpaper](#checkpaper)
     * [paperfeed](#paperfeed)
  * [String handling](#string_handling)
     * [char_at](#charat)
     * [delimited_element](#delimited_element)
     * [delimited_count](#delimited_count)
     * [delimited_insert](#delimited_insert)
     * [delimited_remove](#delimited_remove)
     * [delimited_replace](#delimited_replace)
     * [str_find](#str_find)
     * [str_replace](#str_replace)
     * [strmap_get](#strmap_get)
     * [trim](#trim)
     * [strlen](#strlen)
     * [strpad](#strpad)
     * [substr](#substr)
     * [strcat](#strcat)
  * [User interface](#user_interface)
     * [menu](#menu)
     * [menuwithheader](#menuwithheader)
     * [displaybitmap](#displaybitmap)
     * [display](#display)
     * [cleandisplay](#cleandisplay)
     * [gettouch](#gettouch)
     * [inputfloat](#inputfloat)
     * [inputformat](#inputformat)
     * [inputint](#inputint)
     * [inputoption](#inputoption)
     * [inputmoney](#inputmoney)     
  * [Utilities](#utilities)
     * [backlight](#backlight)
     * [qrcode](#qrcode)
     * [beep](#beep)
     * [checkbattery](#checkbattery)
     * [systeminfo](#systeminfo)
     * [systemrestart](#systemrestart)
     * [unzip](#unzip)
     * [waitkey](#waitkey)
     * [waitkeytimeout](#waitkeytimeout)
     * [readkey](#readkey)
     * [wait](#wait)
  * [ISO8583](#iso8583)
     * [iso8583_loadconfig](#iso8583_loadconfig)
     * [iso8583_init_message](#iso8583_init_message)
     * [iso8583_put_string](#iso8583_put_string)
     * [iso8583_put_int](#iso8583_put_int)
     * [iso8583_end_message](#iso8583_end_message)
     * [iso8583_transact](#iso8583_transact)
     * [iso8583_analyze](#iso8583_analyze)
     * [iso8583_get_int](#iso8583_get_int)
     * [iso8583_get_string](#iso8583_get_string)
          
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
   
## Network and Communications
   
   Network related api. Remember that all communication 
   is routed through CloudWalk servers.
   
###  predial
  Perform a dial-up connection
   
    int predial(int option)
    
  POSXML **predial** call:
  [https://docs.cloudwalk.io/en/posxml/commands/predial]

### preconnect
  Establish a connection to the CloudWalk servers.

    int preconnect()
    
  POSXML **preconnect** call:
  [https://docs.cloudwalk.io/en/posxml/commands/preconnect]
  
### initmodem
  Configures the device modem to do dial up calls.
  
     int initmodem()
     
  POSXML **network.start** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.start]

### shutdownmodem
  Terminates the dial-up connection.
  
    void shutdownmodem()
   
  POSXML **shutdownmodem** call:
  [https://docs.cloudwalk.io/en/posxml/commands/shutdownmodem]
  
### gprs_signal_level
  Measures the GPRS signal level:
  
    int gprs_signal_level() 
  
  POSXML **network.checkgprssignal** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.checkgprssignal]
  
### disconnect
  Disconnects from CloudWalk servers, but do not shut down the network connection.
  
    void disconnect()
  
  POSXML **network.hostdisconnect** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.hostdisconnect]
  
### ping
  "PING"s a host through the network.
  
    void ping(string host)
    
  POSXML **network.ping** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.ping]
  
### send
  Sends a buffer through an already established connection.
  
    int send (string buffer, int size)
    
  POSXML **network.send** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.send]
  
### receive
  Receives data from the network
  
    int receive(int maxsize, int &variablereceivedbytes,
                string &variablebuffer)
                
  POSXML **network.receive** call:
  [https://docs.cloudwalk.io/en/posxml/commands/network.receive]
   
## Printing and Printer Control
   Using device's printer
   
### print
  Prints text in normal font
   
    void print(string message)
     
  POSXML **print** call:
  [https://docs.cloudwalk.io/en/posxml/commands/print]
   
### printbit
  Prints text on big font
   
    void printbig(string message)
     
  POSXML **printbig** call:
  [https://docs.cloudwalk.io/en/posxml/commands/printbig]
  
### printbitmap 
  Prints a monochrome bitmap
  
    int printbitmap(string filename)
    
  POSXML **printbitmap** call:
  [https://docs.cloudwalk.io/en/posxml/commands/printbitmap]
  
### printbarcode
  Prints a bar code
  
    int printbardode(int horizontal, string number)
    
  POSXML **printbarcode** call:
  [https://docs.cloudwalk.io/en/posxml/commands/printbarcode]
  
### checkpaper
  Checks if the printer has paper in it.
  
    int checkpaper(void)
    
  POSXML **checkpaperout** call:
  [https://docs.cloudwalk.io/en/posxml/commands/checkpaperout]
  
### paperfeed
  Feeds one line of paper to the printer
  
    void paperfeed()
    
  POSXML **paperfeed** call:
  [https://docs.cloudwalk.io/en/posxml/commands/paperfeed]
  
### String Handling
  String handling functions.
  
### char_at
  Gets the character at a position.
  
    string char_at(int character_index, string string)
    
  POSXML **string.charat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.charat]
  
### delimited_element
  Gets the nth element on a delimited string.
  
    string delimited_element(string delimiter, int element_index, 
                             string string)
                             
  POSXML **string.elementat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.elementat]
  
### delimited_count
  Count the number of delimited elements in a string.
  
    int delimited_count(string delimiter, string string)
    
  POSXML **string.elements** call::
  [https://docs.cloudwalk.io/en/posxml/commands/string.elements]
  
### delimited_insert
  Inserts an element into a delimited string.
  
    string delimited_insert(string delimiter, int element_index, 
                            string string, string string_to_be_inserted)

  POSXML **string.insertat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.insertat]
                                
### delimited_remove
  Removes an element from a delimited string
  
    string delimited_remove(string delimiter, int element_index, 
                            string string)
  
  POSXML **string.removeat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.removeat]
                                
### delimited_replace
  Replaces an element in a delimited string
  
    string.delimited_replace(string delimiter, int element_index, 
                             string new_element, string string)

  POSXML **string.replaceat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.replaceat]
                               
### str_find
  Locates a substring inside a string
  
    int str_find (int start, string string, string substring)
    
  POSXML **string.find** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.find]
  
### str_replace
  Replaces a substring inside a string.
  
    string str_replace(string new_substring, string old_substring,
                       string original_string)
                       
  POSXML **string.replace** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.replace]
                         
### strmap_get
  Gets the value from a string map ("key=value;key=value")
  
    string strmap_get(string key, string string)
  
  POSXML **string.getvaluebykey** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.getvaluebykey]
  
### trim
  Trims out the whitespace at the start and the end of the string.
  
    string trim(string string) 
    
  POSXML **string.trim** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.trim]
  
### strlen
  Gets the length of a string.
  
    int strlen(string value)
    
  POSXML **string.length** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.length]
  
### strpad
  Pads a string to the desired size.
    
    string strpad(string character, int length, string align,
                  string origin)
                  
  POSXML **string.pad** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.pad]
  
### substr
  Gets a substring from a string
  
    string substr(int length, int start, string string)
    
  POSXML **string.substring** call:
  [https://docs.cloudwalk.io/en/posxml/commands/string.substring]
  
### strcat
  Concatenates two strings.  
  
    string strcat(string firstvalue, string secondvalue)
    
  POSXML **joinstring** call:
  [https://docs.cloudwalk.io/en/posxml/commands/joinstring]
  
## User interface
  User interface functions.

### menu
  Displays a list of options and returns the selected option.
  
    int menu (string options)
   
  POSXML **menu** call:
  [https://docs.cloudwalk.io/en/posxml/commands/menu]

### menuwithheader
  Displays a list of options, with a header line.
  
    int menuwithheader (string header, int timeoutheader,
                        string options, int timeout)
                        
  POSXML **menuwithheader** call:
  [https://docs.cloudwalk.io/en/posxml/commands/menuwithheader]
  
### displaybitmap
  Displays a bitmap on screen.
  
    int displaybitmap(string filename)
    
  POSXML **displaybitmap** call
  [https://docs.cloudwalk.io/en/posxml/commands/displaybitmap]

### display
  Displays text on screen.
  
    int display(int line, int column, string message)
    
  POSXML **display** call:
  [https://docs.cloudwalk.io/en/posxml/commands/display]
  
### cleandisplay
  Clears the screen of the device.
  
    void cleandisplay ()

  POSXML **cleandisplay** call:
  [https://docs.cloudwalk.io/en/posxml/commands/cleandisplay]
  
### gettouch
  Reads a "touch" on the touch screen
  
    int gettouch (int &axisx, int &axisy)
    
  POSXML **system.gettouchscreen** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.gettouchscreen]

### inputfloat
  Inputs a floating point value as string
  
    string inputfloat(int line, int column, int message)
    
  POSXML **inputfloat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inputfloat]
  
### inputformat
  Inputs a value according to a format

    string inputformat (int line, int column, int message, string format)
    
  POSXML **inputformat** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inputformat]
  
### inputint
  Inputs an integer
  
    int inputint(int line, int column, string  message,
                 int minimum, int maximum)
                    
  POSXML **inputinteger** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inputinteger]
                      
### inputoption
  Inputs an integer without the need of the user to press the ENTER key
  
    int inputoption(int line, int column, int message, 
                    int minimum, int maximum)
  
  POSXML **inputoption** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inputoption]
  
### inputmoney
  Input a money value, in cents.
  
    int inputmoney(int line, int column, string message)
    
  POSXML **inputmoney** call:
  [https://docs.cloudwalk.io/en/posxml/commands/inputmoney]
  
## Utilities
  Utility functions

### backlight
  Sets the device's backlight level
  
    int backlight (int level)
    
  POSXML **system.backligh** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.backlight]
  
### qrcode
  Generates a QRCode bitmap.
  
    void qrcode(string filename, string input, string size, 
                string version)
  
  POSXML **system.qrcode** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.qrcode]
          
### beep
  Generates a "beep" sound.

    void beep()
    
  POSXML **system.beep** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.beep]
  
### checkbattery
  Checks the battery level
  
     int checkbattery()
  
  POSXML **system.checkbattery** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.checkbattery]
  
### systeminfo
  Gets information about the device.
  
    string systeminfo(string type)
    
  POSXML **system.info** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.info]
  
### systemrestart
  Restarts the device
  
    void systemrestart()
    
  POSXML **systemrestart** call:
  [https://docs.cloudwalk.io/en/posxml/commands/system.restart]
  
### unzip
  Unzips a "zip" file
  
    int unzip (string filename)
    
  POSXML **unzipfile** call:
  [https://docs.cloudwalk.io/en/posxml/commands/unzipfile]
  
### waitkey
  Waits for a key to be pressed.
  
    void waitkey()
    
  POSXML **waitkey** call:
  [https://docs.cloudwalk.io/en/posxml/commands/waitkey]
  
### waitkeytimeout
  Waits for a key to be pressed or a timeout.
  
    void waitkeytimeout(int seconds)
    
  POSXML **waitkeytimeout** call:
  [https://docs.cloudwalk.io/en/posxml/commands/waitkeytimeout]
  
### readkey
  Reads a pressed key or a timeout
  
    string readkey (int milliseconds)
    
  POSXML **readkey** call:
  [https://docs.cloudwalk.io/en/posxml/commands/readkey]
  
### wait
  Waits for a timeout to expire
  
    string wait(int milliseconds)
    
  POSXML **wait** call:
  [https://docs.cloudwalk.io/en/posxml/commands/wait]
  
## ISO8583

### iso8583_loadconfig
  Loads the iso8583 bitmap config table.

    int iso8583_loadconfig(string filename)

  POSXML **iso8583.initfieldtable** call:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.initfieldtable]

### iso8583_init_message
  Initialize a ISO8583 message buffer
  
    int iso8583_init_message (string format, string id, 
                              string &variablemessage)
                              
  POSXML **iso8583.initmessage** call:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.initmessage]

### iso8583_put_string
  Puts a string into a iso8583 field
  
    int iso8583_put_string(int fieldnumber, string value)
    
  POSXML **iso8583.putfield** call with **type** parameter set 
  to **"string"**:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.putfield]

### iso8583_put_int
  Puts an integer into a iso8583 field
  
    int iso8583_put_int(int fieldnumber, int value)
  
  POSXML **iso8583.putfield** call with **type** parameter set
  to **"integer"**:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.putfield]

### iso8583_end_message
  Finalizes the iso8583 message generation, formatting the message
  and storing it into the variable passed to the `iso8583_init_message`
  function.
  
    int iso8583_end_message(int &variableSize)
    
  POSXML **iso8583.endmessage** call:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.endmessage]

### iso8583_transact
  Generates the message with size header, sends it to the authorizer, 
  and receives the response message.
   
    int iso8583_transact (string channel, string header, string trailler,
                          string isomsg, string &variableresponse)
                          
  POSXML **iso8583.transactmessage** call:
  [https://docs/cloudwalk.io/en/posxml/commands/iso8583.transactmessage]                            

### iso8583_analyze
  Parses the iso8583 message and initializes the global state of the
  iso interpreting process.
   
    int iso8583_analyze (string format, int size, string &variableid,
                         string &variablemessage)
                          
  POSXML **iso8583.analyzemessage** call:
  [https://docs/cloudwalk.io/en/posxml/commands/iso8583.analyzemessage]
                              
### iso8583_get_int
  Gets the value of an integer field from an iso8583 message.
  
    int iso8583_get_int(int fieldnumber, int &variablevalue)

  POSXML **iso8583.getfield** call with **type** parameter set
  to **"integer"**:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.getfield]

### iso8583_get_string
  Gets the value of a string field from an iso8583 message.
  
    int iso8583_get_string (int fieldnumber, string &variablevalue)

  POSXML **iso8583.getfield** call with **type** parameter set
  to **"string"**:
  [https://docs.cloudwalk.io/en/posxml/commands/iso8583.getfield]

