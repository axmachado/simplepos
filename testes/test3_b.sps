int g;

g = 5;

int f1(int x) {
    return f2(x) / 2 + f3(x);
}

int f2(int x) {
    return f3(x) +1 ;
}

int f3(int x) {
    int y;
    y = (g + 1) / 2;
    g++;
    return x * y;
}
