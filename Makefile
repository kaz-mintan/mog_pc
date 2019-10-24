#Makefile
TARGET=heart_fsr

CC=g++
OS=$(shell uname | cut -d_ -f1)

PROGRAM=$(addsuffix .cpp, $(TARGET))

$(TARGET): $(PROGRAM)
	$(CC) -o $(TARGET) $(PROGRAM) 

clean:
	rm -rf $(TARGET)
