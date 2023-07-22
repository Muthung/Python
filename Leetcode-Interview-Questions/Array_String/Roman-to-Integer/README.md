## Roman to integer

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
    
Given a roman numeral, convert it to an integer.

#### Implementation 

To convert a Roman numeral to an integer, you can iterate through the characters of the Roman numeral from left to right. Compare the current symbol with the next symbol to determine whether it represents a subtraction or addition.

Create a dictionary to map the Roman numerals to their respective values.

Initialize a variable called *results* to 0.

Iterate through the characters of the Roman numeral from left to right.

    Get the value of the current symbol from the dictionary.
    
    If there is a next symbol and its value is greater than the current symbol's value, subtract the current value from the result.
    
    Otherwise, add the current value to the result.
    
