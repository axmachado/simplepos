int x;
int y;

x = 5;
y = 3;

if (x > y) {
    display(1,1,"x > y");
}

if (!(x > y)) {
    display(1,1,"negado");
}

if (!x) {
    display(1,1, "simples");
}

if ( x > y || x < y ) {
    display(1,1, "or");
}

if ( x > y && x < y ) {
    display(1,1, "and");
}
