#include <stdio.h> 
// This line includes the standard input-output library, which is necessary for using printf and scanf functions.

int main(void)
{
    // This is a single-line comment in C. It explains that the following line of code will print "Hello, World!" to the console.
    printf("Hello, World!\n");
}

/*  
This is a simple C program that prints "Hello, World!" to the console. 
GUI means Graphical User Interface and CLI means Command Line Interface.
Let's now terminal 
gcc hello.c -o myprogram
[
GCC stands for the GNU Compiler Collection,
hello.c is our source code file,
The -o flag stands for output and
-o hello tells the compiler to create an executable program named hello.exe.
{.exe is the default extension for executable files on Windows, 
while on Linux and macOS, the executable file will not have an extension.}
]
Then we can run the program by typing ./hello in the terminal.
./ means go into the current directory and run the program named hello.


*/

/*
// Given by gemini 
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
*/