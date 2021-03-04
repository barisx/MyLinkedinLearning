## Python Truth Values

- False and None evaluate to false
- Numeric zeo values: 0, 0.0, 0j
- Decimal(0), Fraction(0, x)
- Empty sequences/collections: '', (), [], {}
- Empty sets and ranges: set(), range(0)

```py
class myClass:
    def __bool__(self):
        return False

    def __len__(self):
        return 0
```

| Boolean Operation | Resutl |
| ------------- |:-------------:|
| X and Y     | true if X and Y are both true |
| X or Y      | true if either X or Y are true |
| not X | If X is false, then true, else false |

