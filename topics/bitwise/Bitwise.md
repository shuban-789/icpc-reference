# Bitwise

```java
int num = 45;

if ((num & 1) == 0) {
          System.out.println("Even");
} else {
          System.out.println("Odd"); // 45 is binary 101101 (ends in 1, so Odd)
}

// Define the bit positions (powers of 2)
final int READ       = 1; // 0001
final int WRITE      = 2; // 0010
final int EXECUTE = 4; // 0100

// 1. Combine permissions using OR (|)
int userPermissions = READ | WRITE; // 0011 (Can read and write)

// 2. Check if a user has a specific permission using AND (&)
boolean canWrite       = (userPermissions & WRITE) != 0;          // true (0011 & 0010 != 0)
boolean canExecute = (userPermissions & EXECUTE) != 0; // false (0011 & 0100 == 0)

int x = 10;
int y = 5;

x = x ^ y;
y = x ^ y; // y becomes 10
x = x ^ y; // x becomes 5

System.out.println("x: " + x + ", y: " + y); // x: 5, y: 10

int speed = 20;
int doubleSpeed = speed << 1; // 20 * 2 = 40
int halfSpeed         = speed >> 1; // 20 / 2 = 10
int quadSpeed         = speed << 2; // 20 * 4 = 80

int[] nums = {4, 1, 2, 1, 2};
int unique = 0;
for (int num : nums) {
         unique ^= num;
}
System.out.println("Unique number: " + unique); // Outputs 4
```
