# cpp_makefile

```make
CXX ?= g++
CXXFLAGS ?= -std=c++17 -O2 -Wall -Wextra

.PHONY: all run clean

all: sol

sol: sol.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $< $(LDFLAGS) $(LDLIBS) -o $@

run: sol
	./sol

clean:
	$(RM) sol
```
