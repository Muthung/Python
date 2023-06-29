## Remove Duplicates from Sorted array

### question

Given an integer array *nums* sorted in ***non-decreasing order**, remove the duplicates *in-place* such
that each unique element appears **once**. The **relative order** of the elements should be kept the **same**.
Then return the number of unique elements in *nums*.

Consider the number of unique elements of *nums* to be *k*, to get accepted, you need to do the following things: 
       - Change the array *nums* such that the first *k* elements of *nums* conatin the unique elements in
         the order they were present in *nums* initially. The remaining elements of *nums* are not important
         as well as te size of *nums*.
       - Return *k*.
       
#### Custom Judge:

The judge will test your solution with the following code:

> int[] nums = [...]; // Input array
> int[] expectedNums = [...]; // The expected answer with correct length
>
> int k = removeDuplicates(nums); // Calls your implementation
>
> assert k == expectedNums.length;
> for (int i = 0; i < k; i++) {
> assert nums[i] == expectedNums[i];
> }

If all assertions pass, then your solution will be **accepted**.

#### implementation

Compares each element with its previous element. If they are different, it means it has found a new unique 
element. It then updates the array by assigning the unique element to the *k* position and increment *k*.

Finally, it return *k*, which represents the number of unique elements in the array.
