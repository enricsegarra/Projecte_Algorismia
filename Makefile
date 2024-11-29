# Compilador
CXX = g++

# Flags de compilación
CXXFLAGS = -std=c++17 -Wall -Wextra -I./resource

# Directorios
SRCDIR = .
BINDIR = .
OBJDIR = ./obj

# Archivos
MAIN = $(SRCDIR)/main.cpp
SRC_E = $(SRCDIR)/resource/ExperimentoE/ExperimentoE.cpp

# Objetos
OBJ_MAIN = $(OBJDIR)/main.o
OBJ_E = $(OBJDIR)/ExperimentoE.o

# Ejecutable
TARGET = $(BINDIR)/program

# Reglas
all: $(TARGET) 

$(TARGET): $(OBJ_MAIN) $(OBJ_E)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(OBJDIR)/main.o: $(MAIN)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(OBJDIR)/ExperimentoE.o: $(SRC_E)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJDIR)/*.o $(TARGET)

.PHONY: all clean
