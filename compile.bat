nasm -f win64 -g -F cv8 hello.asm -o hello.o
ld hello.o /OUT:hello.exe /SUBSYSTEM:CONSOLE /ENTRY:start "C:\Windows\System32\kernel32.dll"

nasm test.asm -o test.o
