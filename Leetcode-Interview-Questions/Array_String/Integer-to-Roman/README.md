## Integer to Roman

### Question 

Roman numerals are represented by seven different symbols: *I*,*V*,*X*,*L*,*C*,*D*, and *M*.

    Symbol          Value 
    I               1
    V               5
    X               10
    L               50
    C               100
    D               500
    M               1000
    
For example, *2* is written *II* in Roman numeral, just two ones added together. *12* is written as *XII*, which is simply *X + II*. The number *27* is written as *XXVII*, which is *XX + V + II*.

Roman numerals are usually written largest to smallest from left to right. However, the numral for four is not *IIII*. Instead, the number four is written as *IV*. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as *IX*. There are six instances where subtraction is used:

    *I* can be placed before *V* (5) and *X* (10) to make 4 and 9.
    *X* can be placed before *L* (50) and *C* (100) to make 40 and 90.
    *C* can be placed before *D* (500) and *M* (1000) to make 400 and 600.
    
Given an integer, convert it to a Roman numeral.

#### Implementation 

Create two arrays: one to store the Roman numeral symbols and another to store their corresponding values.

Initialize an empty string to store the Roman numeral representation.

Iterate through the values and symbols array in reverse order (from the largest symbol to the smallest).

In each iteration, while the current value is less than or equal to the given number, subtract the current value from the number and append the corresponding symbol to the result string.

Finally, return the resulting string.
