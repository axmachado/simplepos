/*
 * Sample return statement
 */

module exemple3;

int x = 5;

display (1,1, inttostring(f1(x)));


int f1(int x) {
    int i;
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
    for (i = 0; i < 10; ++i) {
        x = (x + 1) * i;
        if (x > 10) {
            return x;
        }
    }
    return 0;
}
