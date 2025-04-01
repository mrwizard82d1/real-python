#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  FILE *fp = fopen("write.txt", "w");
  fputs("Real Python!\n", fp);
  fclose(fp);
  return 1;
}
