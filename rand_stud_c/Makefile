CC = gcc
CFLAGS = -Wall -Werror -std=c99

PROGRAM = rand_studs
SRCS = rand_studs.c
OBJS = $(SRCS:.c=.o)

.PHONY: all clean

all: $(PROGRAM)

$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROGRAM) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(PROGRAM) $(OBJS)
