 Heap is a binary tree-based data where the value of each node is greater than or equal to the value of its children.
 Heaps are commonly used to implement a priorities queue where elements are retrieved based on their priority.
**Adding heaps in a heap**
Insert node in the available position level.
Compare the inserted node with the parent if it is larger swap it with the parent.
Continue the second step until the order is restored.
**Removing items in a list**
Replace the element you want to delete with the last element.
Delete the last element
Arrange the node placed at the element deleted to ensure the order of the heap

**Merge Sort**
Merge sort is a sorting algorithm that follows the divide-and-conquer approach. 
It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

Divide: Divide the list or array recursively into two halves until it can no longer be divided.
Conquer: Each subarray is sorted individually using the merge sort algorithm.
Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.

Best Case: O(n log n), When the array is already sorted or nearly sorted.
Average Case: O(n log n), When the array is randomly ordered.
Worst Case: O(n log n), When the array is sorted in reverse order.

Applications of Merge Sort:
Sorting large datasets
External sorting (when the dataset is too large to fit in memory)
Inversion counting (counting the number of inversions in an array)
Finding the median of an array**


**Buble Sort**
Bubble Sort is the simplest sorting algorithm that repeatedly swaps the adjacent elements if they are in the wrong order.
This algorithm is unsuitable for large data sets as its average and worst-case time complexity is quite high.

Advantages of Bubble Sort:
Bubble sort is easy to understand and implement.
It does not require any additional memory space.
It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
Disadvantages of Bubble Sort:
Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
Bubble sort is a comparison-based sorting algorithm, which requires a comparison operator to determine the relative order of elements in the input data set.
It can limit the efficiency of the algorithm in certain cases.








