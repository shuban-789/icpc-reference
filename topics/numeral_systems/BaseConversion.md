# BaseConversion

```java
public class BaseConversion {


  public static void main(String[] args) {


    // ==========================================


    // 1. BASE 10 ---> BASE 2 (Decimal to Binary)


    // ==========================================


    int decimalNum = 13;

        // Built-in method: Integer.toBinaryString(int)

        String binaryStr = Integer.toBinaryString(decimalNum);

        System.out.println("Decimal 13 to Binary: " + binaryStr); // Output: "1101"



        // ==========================================


        // 2. BASE 2 ---> BASE 10 (Binary to Decimal)


        // ==========================================


        String binaryInput = "1101";



        // Built-in method: Integer.parseInt(string, base)


        int decimalOutput = Integer.parseInt(binaryInput, 2);


        System.out.println("Binary 1101 to Decimal: " + decimalOutput); // Output: 13


    }


}
```
