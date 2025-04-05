ARCHFLAGS="-arch arm64 -arch arm64e"
# echo $ARCHFLAGS
#clang -shared -fPIC fibonacci.c -o fibonacci.so

clang -arch arm64 -c fibonacci.c -o fibonacci.o
clang -arch arm64 -shared -fPIC -o fibonacci.so fibonacci.o
