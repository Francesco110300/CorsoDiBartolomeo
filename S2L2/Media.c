#include <stdio.h>
#define media (a+b)/2
int main(){
    //variabili
    int a;
    int b;
    //via
    printf("Numero 1: ");
    scanf("%d", &a);
    printf("Numero 2: ");
    scanf("%d", &b);
    printf("La media fra %d e %d e': %d",a,b,media);
}