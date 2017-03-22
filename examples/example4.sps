/*
 * inline function call
 */

 module example4;

 string v = delimited_init("|", 10);

 display(0,0,delimited_element("|", 3, v));