/*
 * Sample return statement
 */

module exemple3;

int x = 5;

display (1,1, inttostring(f1(x)));


int f1(int x) {
    if (x < 1) {
        return x;
    }
    x++;
    if (x < 3) {
       return x+1;
    }
    x++;
    if (x < 5) {
        if (x > 4) {
           return 0;
        }
        x++;
        x++;
    }
    return x;
}
