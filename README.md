# HTML Table to JSON

> Convert HTML Table to JSON objects using Python

*Note: No rowspan and colspan attribute support !*

Firstname  | Lastname   | Age
---------  | --------   | ----
Jill       | Smith      | 50
Eve        | Jackson    | 94
John       | Doe        | 80

**With Table Header**
---

```json
[
    {
        "firstname": "Jill",
        "lastname": "Smith",
        "age": "50"
    },
    {
        "firstname": "Eve",
        "lastname": "Jackson",
        "age": "94"
    },
    {
        "firstname": "John",
        "lastname": "Doe",
        "age": "80"
    }
]

```

**Without Table Header**
---


```json
[
    [
        "Jill",
        "Smith",
        "50"
    ],
    [
        "Eve",
        "Jackson",
        "94"
    ],
    [
        "John",
        "Doe",
        "80"
    ]
]
```
