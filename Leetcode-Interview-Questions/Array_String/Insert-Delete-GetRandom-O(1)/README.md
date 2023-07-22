## Insert Delete GetRandom O(1)

### Question 

Implement the *RandomizedSet* class:

    -*RandomizedSet()* initializes the *RandomizedSet* object.
    
    -*bool insert(int val)* inserts an item *val* into the set if not present.
     Returns *True* if the item was not present, *false* otherwise.
     
    -*bool remove(int val)* Removes an item *val* from the set if present.
     Returns *True* if the item was present, *false* otherwise.
     
    -*int getRandom()* Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.
    
You must implement the functions of the class such that each function works in **average** O(1) time complexity.

#### Implementation 

Use of a combination of a hash set and an array. The hash set will be used to check the presence of an element and remove it in O(1) average time complexity, while the array will be used to store the elements in the set and retrieve a random element in O(1) average time complexity.

The *RandomizedSet* class maintains a set *self.set* to store the elements and an array *self.arr* to store the elements in the order they were inserted.
The *insert* method checks if the element already exists in the set. If it does, it returns *False*; Otherwise, it adds the element to both the set and the array and returns *True*.

The *remove* method checks if the element exists in the set. If it does not, it returns *False*; Otherwise, it removes the element from both the set and the array and returns *True*.

The *getRandom* method simply selects a random element from the array using the *random.choice* function and returns it.

This satisfies the average O(1) time complexity requirement for each operation.

