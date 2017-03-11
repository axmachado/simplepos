
module test (int a, string &b);
global
   int x, k;
   int y; string z, w;

x = 3;
y = x;
z = inttostring(x);

k = stringtoint("10") + y * z * (3 - x);

w = inttostring(y);

waitkey();

if ( ((k^2+5)/3) > 10 || (x > 3 && y)) {
    string localmsg;
    localmsg = "Condicao TRUE"; 
    display (1,1,localmsg);
    waitkey();
}
else {
    display (1,1,"Condicao FALSE");
    waitkey();
}

if ( !true ) {
    display (1,1,"false");
}

display(1,2,"Teste");
display(2,2,w);

x = 1;
while (x < 10) {
    if ((x % 2) == 0) {
        break;
    }
    x++;
}
