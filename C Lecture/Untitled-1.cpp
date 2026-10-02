#include <stdio.h> // Without this, BOTH functions below will crash!

int main(void) {
    int age;

    // 1. OUTPUT: Asking the user a question
    printf("Enter your age: "); 

    // 2. INPUT: Reading what the user types on the keyboard
    scanf("%d", &age); 

    // 3. OUTPUT: Printing the result back to the screen
    printf("Wow, you are %d years old!\n", age); 

    return 0;
}