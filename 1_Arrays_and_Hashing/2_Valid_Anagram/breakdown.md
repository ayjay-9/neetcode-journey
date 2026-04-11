# Valid Anagram - Breakdown

## First Thoughts

* If two strings are considered anagrams, then they would have the same letters regardless of their order
* If I sort both string, the characters will be in ascending order based on their unicode
* That way I will know for sure that they are anamgrams or not

## Plan

* Equate and return the sorted strings

## Understanding the Optimal Solution

* Factor the lengths of the strings, if they are not equal they are automatically not anagrams
* Initialise an array to track to changes in the occurence(s) of the letters
* If any of the indices is not 0, then the two strings are not anagrams
