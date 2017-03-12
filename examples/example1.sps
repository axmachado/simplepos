/*
 * Sample module with constants
 */
module example1;
const CT1 = "string constant 1";
const CI1 = 15;

int x = CI1, y;
string z;

y = 2 * x + 1;
z = strcat(CT1, inttostring(y));
