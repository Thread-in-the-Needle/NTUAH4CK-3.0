#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>


int main(int argc, char *argv[]) {

    FILE *file;
    
    file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Could not open flag.txt\n");
        return 1;
    }
    
    fseek(file, 0, SEEK_END);
    int fileSize = ftell(file);
    rewind(file);
    char *contents = (char *)malloc(fileSize + 1);
    unsigned char *encrypted = (unsigned char *)malloc(fileSize);

    fread(contents, 1, fileSize, file);
    contents[fileSize] = '\0';
    
    fclose(file);

    unsigned char *randomNumbers = (unsigned char *)malloc(fileSize * 4);

    FILE *urandom = fopen("/dev/urandom", "r");
    if (urandom == NULL) {
        printf("Could not open /dev/urandom\n");
        free(contents);
        free(randomNumbers);
        free(encrypted);
        return 1;
    }

    fread(randomNumbers, fileSize * 4, 1, urandom);
    fclose(urandom);
    int me;
    me = open(argv[0], O_RDONLY);
    if (me < 0) {
        printf("Could not open file\n");
        free(contents);
        free(encrypted);
        free(randomNumbers);
        return 1;
    }
    for (int i = 0; i < fileSize; i++) {
        int ind = 0;
        for (int j = 0; j < 4; j++) {
            ind += randomNumbers[4*i + j];
        }
        int offset = 0;
        while (1) {
            lseek(me, ind + offset, SEEK_SET);
            char n;
            read(me, &n, 1);
            if (n != 0) {
                encrypted[i] = contents[i] ^ n;
                break;
            }
            offset += 1;
        }
        
        
    }
    close(me);
    
    me = open("encrypted", O_CREAT | O_RDWR, 0666);

    if (write(me, randomNumbers, 4*fileSize) < 0) {
        printf("Failed to write to output\n");
    }
    if (write(me, encrypted, fileSize)< 0) {
        printf("Failed to write to output\n");
    }
    close(me);
    free(contents);
    free(encrypted);
    free(randomNumbers);

    return 0;
}
