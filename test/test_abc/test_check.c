#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1000
#define MAX_NUM_QUESTIONS 30
#define MAX_NUM_STUDENTS 100

typedef struct {
    char name[MAX_LINE_LENGTH];
    float score;
} Student;

Student students[MAX_NUM_STUDENTS];
int correct_answers[MAX_NUM_QUESTIONS] = {0};
float total_score = 0;
int num_students = 0;

void process_student(FILE *fptr, char answers[MAX_NUM_QUESTIONS][MAX_LINE_LENGTH]) {
    fgets(students[num_students].name, MAX_LINE_LENGTH, fptr); // Reads student name

    printf("%s\n", students[num_students].name);

    char student_answer[MAX_LINE_LENGTH];
    students[num_students].score = 0;

    for (int i = 0; i < MAX_NUM_QUESTIONS; i++) {
        fgets(student_answer, MAX_LINE_LENGTH, fptr);
        if (strcmp(answers[i], student_answer) == 0) {
            students[num_students].score += 20.0/MAX_NUM_QUESTIONS;
            correct_answers[i] += 1;
        } else {
            printf("Incorrect answer for question %d. Correct answer is %s\n", i+1, answers[i]);
        }
    }
    printf("Score: %.2f\n", students[num_students].score);

    total_score += students[num_students].score;
    num_students++;
}

void print_statistics() {
    printf("\n*** Test Statistics ***\n");
    printf("Average Score: %.2f\n", total_score / num_students);

    for (int i = 0; i < MAX_NUM_QUESTIONS; i++) {
        printf("Question %d - Correct Answers: %d, Percentage: %.2f%%\n", i+1, correct_answers[i], 
               (double) correct_answers[i] / num_students * 100);
    }

    printf("\n*** Student Scores ***\n");
    printf("Student Name, Score\n"); // Add header
    for (int i = 0; i < num_students; i++) {
        printf("%s     Score: %.2f\n", students[i].name, students[i].score);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Please provide the correct file paths.\n");
        return -1;
    }

    FILE *answer_file = fopen(argv[1], "r");
    FILE *student_file = fopen(argv[2], "r");

    if (!answer_file || !student_file) {
        printf("Unable to open files.\n");
        return -1;
    }

    char answers[MAX_NUM_QUESTIONS][MAX_LINE_LENGTH];

    for (int i = 0; i < MAX_NUM_QUESTIONS; i++) {
        fgets(answers[i], MAX_LINE_LENGTH, answer_file);
    }

    while (!feof(student_file)) {
        process_student(student_file, answers);
    }

    print_statistics();

    fclose(answer_file);
    fclose(student_file);

    return 0;
}
