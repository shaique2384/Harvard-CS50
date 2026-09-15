//print() will just print the string to the console
//printf() will print the string to the console and allow for formatted output, such as inserting variables into the string, like f'str of python
//we gotta finish our thought with a semicolon at the end of the line, otherwise it will throw an error
//programming is line based, and error shows up while compiling, not while running the program, so we gotta fix it before we can run it
//C comes with a bunch of header files that contain useful functions, like printf() and scanf(), which are used for input and output
//the header files are included at the top of the file with the #include directive, which tells the compiler to include the contents of the specified header file in the program
//they come with .h instead of .c because they are header files, which contain declarations of functions and variables, but not the actual implementation of the functions
//header files are libraries exactly like python modules, but they are not imported with import, but with #include
//to find their cs50 simpler version go to manual.cs50.io/3/printf
// after including <cs50.h> let's terminal gcc hello.c -lcs50 -o hello.exe
//-l (Link Flag): Instructs the compiler to link a static or dynamic library during the final compilation step.
//The linker automatically prepends lib and appends .a (or .so/.dll), so passing -lcs50 directs it specifically to look for libcs50.a inside your lib directory.

#include <cs50.h>
#include <stdio.h>
// what it's doing for us is telling the includer, by the way IL did not write everything that are in the header file
//if we want to use a function from the header file, you need to include the header file in your program, otherwise the compiler will not know about the function and will throw an error

int main(void)
{
    string answer = get_string("what is your name? ");
//for c we need to include the cs50.h header file to use the get_string() function, which is a function that prompts the user for input and returns a string
//we need string anser to be declared before main() because we need to use it in main(), otherwise it will throw an error
//%s is a placeholder for a string, and it will be replaced by the value of the variable answer when the program is run
printf("hello, %s\n" , answer);
    return 0;
}



/*

\n [newline] - moves the cursor to the next line
\r [carriage return] - moves the cursor to the beginning of the current line
\t [tab] - moves the cursor to the next tab stop
\" [double quote] - allows you to include a double quote in a string
\' [single quote] - allows you to include a single quote in a string
\\ [backslash] - allows you to include a backslash in a string

cd is change directory, and it is used to navigate the file system in the terminal
cp is copy, and it is used to copy files and directories in the terminal
mv is move, and it is used to move files and directories in the terminal
ls is list, and it is used to list the files and directories in the current directory in the terminal
mkdir is make directory, and it is used to create a new directory in the terminal
rm is remove, and it is used to delete files and directories in the terminal
rmdir is remove directory, and it is used to delete empty directories in the terminal

*/

