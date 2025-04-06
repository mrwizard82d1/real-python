ARCHFLAGS="-arch arm64 -arch arm64e"
# echo $ARCHFLAGS
#clang -shared -fPIC fibonacci.c -o fibonacci.so

cd parallel
clang -arch arm64 -c parallel.c -o parallel.o
clang -arch arm64 -shared -fPIC -o parallel.so parallel.o
cd ..
