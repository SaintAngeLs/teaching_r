#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_NAME_LENGTH 50
#define MAX_STUDENTS 100

void print_usage(char *program_name) {
    printf("Usage: %s filename num_students\n", program_name);
}

void choose_students(char student_list[MAX_STUDENTS][MAX_NAME_LENGTH], int count, int num_students, char selected_students[MAX_STUDENTS][MAX_NAME_LENGTH]) {
    int selected_count = 0;
    int i;
    
    // Seed the random number generator
    srand(time(NULL));
    
    // Randomly select the specified number of students
    while (selected_count < num_students) {
        i = rand() % count;
        if (strlen(student_list[i]) > 0) {
            strncpy(selected_students[selected_count], student_list[i], MAX_NAME_LENGTH);
            selected_count++;
            // Remove the selected student from the list
            student_list[i][0] = '\0';
        }
    }
}

void print_students(char selected_students[MAX_STUDENTS][MAX_NAME_LENGTH], int num_students) {
    int i;
    printf("Selected Students:\n");
    for (i = 0; i < num_students; i++) {
        printf("%s\n", selected_students[i]);
    }
}

int main(int argc, char *argv[]) {
    char *filename, name[MAX_NAME_LENGTH];
    int num_students, count = 0;
    char student_list[MAX_STUDENTS][MAX_NAME_LENGTH], selected_students[MAX_STUDENTS][MAX_NAME_LENGTH];
    FILE *fp;
    
    // Check if the correct number of arguments are provided
    if (argc != 3) {
        print_usage(argv[0]);
        return 1;
    }
    
    // Parse the arguments
    filename = argv[1];
    num_students = atoi(argv[2]);
    
    // Open the file for reading
    fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Could not open file %s\n", filename);
        return 1;
    }
    
    // Read the students' names from the file
    while (fgets(name, MAX_NAME_LENGTH, fp) != NULL) {
        // Remove the trailing newline character
        name[strcspn(name, "\n")] = 0;
        strncpy(student_list[count], name, MAX_NAME_LENGTH);
        count++;
    }
    
    // Close the file
    fclose(fp);
    
    // Check if there are enough students in the list
    if (num_students > count) {
        printf("Error: There are only %d students in the list\n", count);
        return 1;
    }
    
    // Choose the specified number of students
    choose_students(student_list, count, num_students, selected_students);
    
    // Print the selected students
    print_students(selected_students, num_students);
    
    return 0;
}
