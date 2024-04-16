Heap is a binary tree-based data where the value of each node is greater than or equal to the value of its children. Heaps are commonly used to implement a priorities queue where elements are retrieved based on their priority.
 Adding heaps in a heap 
 Insert node in the available position level. Compare the inserted node with the parent if it is larger swap it with the parent. Continue the second step until the order is restored.
  Removing items in a list
 Replace the element you want to delete with the last element.
Delete the last element Arrange the node placed at the element deleted to ensure the order of the heap
# Tuples
Tuples are immutable data structures that is immutable which makes them ,ideal for storing data that should not be modified.
**Properties**
They are indexed
They are immutable.
They are ordered
They can contain duplicate elements.
**Accessing elements in a tuple**
We access elements in a tuple using indexing where the first element is at index 0.
Example: names=(“Mary”, “Taylor”)
names[0]
**Adding and removing elements in a tuple**
Tuples are immutable so you cannot add a new element or remove an element in a tuple.
You can concatenate tuples with another tuple using + operator but the original remains the same and a new object is created.
