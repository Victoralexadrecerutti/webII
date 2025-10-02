#include <stdio.h>

int main() {

    // https://www.w3schools.com/c/c_variables_multiple.php
    int x, y, z;
    x = y = z = 50;
    printf("%d\n", x + y + z);

    // https://www.w3schools.com/c/c_data_types.php
    // check other types in the link

    // Create variables
    int myNum = 5;             // Integer (whole number)
    float myFloatNum = 5.99;   // Floating point number
    char myLetter = 'D';       // Character

    // Print variables
    printf("%d\n", myNum);
    printf("%f\n", myFloatNum);
    printf("%c\n", myLetter);

    // https://www.w3schools.com/c/c_operators.php

    // ++ before or after
    int a = 1;
    printf("%i\n", ++a); // 2
    printf("%i\n", a++); // 2
    printf("%i\n", ++a); // 4

    // and bit by bit
    x = 5;
    x &= 3; // x = x and 3
    printf("%d\n", x);   // 1

    // or
    x = 5;
    x = x | 3;
    printf("%d\n", x);   // 7

    // xor
    x = 5;
    x = x ^ 3;
    printf("%d\n", x);  // 6

    // bit inversion
    x = 5;   // 00000101
    x = ~ x; // 11111010 = 
    printf("%d\n", x);  //

    /*
    // bit shift
    x = 5; // 101
    x = x << 3; // bits shifted to rigth three times
    // 000101 = 8+32 = 40
    printf("%d\n", x);  // 40
    */
}
