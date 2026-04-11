# Contains Duplicate - Breakdown

## First Thoughts

* Need to sort the array so ame numbers would be adjacent if present
* What if I loop through the array and store each unique number in another list?

## Brute Force Idea

* Use a nested loop to check numbers againt the immediate predecessor
* That would be O(n²)

## Key Realisation

* Sets only have unique values

## Plan

* Loop over the array
* If the number is already in the set, the it is a duplicate

## Confidence Level

* High


