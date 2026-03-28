# Exercism-solutions
This is a repository where I post solutions for Exercism. If you notice any ways to improve them, please let me know. I’ll save them here, but in future, as my skills improve, I might choose to revise the answer without going through Exercism.

## Notes I’ve learnt from the exercises

### Learn with meltdown_mitigation.py
- You don’t always need to use if / elif / else: if the conditions are independent, you can use multiple if statements; if, on the other hand, the cases are mutually exclusive, elif is more suitable.
- Within a function, if a branch already has a return statement, the final else is often unnecessary, because the function exits immediately.

26/03/26

---

### Learn with black_jack.py
- Use a list when you need an ordered sequence of elements.
  - ‘x in list’ iterates through the elements one by one until it finds a match.
- Use a set when you only need to know whether a value is present or not.
  - ‘x in set’ is on average much faster, because it uses a hash-based structure.
- If you need to perform many membership checks, a set is almost always more efficient than a list.
- If, on the other hand, you need to maintain the order or work with a true sequence, then a list remains the best choice.
- For information on data structures.

- [data structures in Python - Italian](https://docs.python.org/it/3/tutorial/datastructures.html)
- [Open Data Structures](https://opendatastructures.org/)
- [Introduction to data structures](https://www.geeksforgeeks.org/dsa/introduction-to-data-structures/)
- [Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

28/03/26
