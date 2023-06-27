#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_NAME_LENGTH 100

typedef struct {
    char firstName[MAX_NAME_LENGTH];
    char lastName[MAX_NAME_LENGTH];
} Student;

void assignNumbers(char* filename, int n) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Failed to open the file.\n");
        return;
    }

    Student students[100];  // Assuming a maximum of 100 students
    int count = 0;

    while (fscanf(file, "%s %s", students[count].firstName, students[count].lastName) != EOF) {
        count++;
    }

    fclose(file);
    // Generate a seed based on current time
    time_t seed = time(NULL);
    srand(seed); // Seed the random number generator

    srand(time(0)); // Seed the random number generator

    for (int i = 0; i < count; i++) {
        int assignedNumber = rand() % n + 1;
        printf("Student: %s %s - Assigned Number: %d\n", students[i].firstName, students[i].lastName, assignedNumber);
    }
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: ./program_name file.log n\n");
        return 1;
    }

    char* filename = argv[1];
    int n = atoi(argv[2]);

    assignNumbers(filename, n);

    return 0;
}
