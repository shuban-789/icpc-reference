# arrays

```python
fruits = ["Apple", "Banana", "Mango"]


# Option B: True Strict Primitive Array (Built-in module)


import array


# 'i' means signed integers only. Throws TypeError if you try to add a string.


scores = array.array('i', [90, 85, 77])


# 1. Get Length


size = len(fruits) # 3


# 2. Read / Write Elements


first = fruits[0]    # "Apple"
fruits[2] = "Blueberry" # Replaces "Mango"


# 3. Dynamic Operations (Only works on vanilla lists, not primitive Java arrays)


fruits.append("Orange") # Adds to the end


fruits.pop(1)       # Removes index 1 ("Banana")
```
