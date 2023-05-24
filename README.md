# better_ctypes

Ideas:

- Create a decorator to simplify creation of ctypes structures.
  Something like `structure` decorator method from https://github.com/idlesign/ctyped
  but not attached to a any class. Also, get some ideas from https://github.com/dfint/peclasses.
- ...


Concept:

```python
@annotated
class POINT(Structure):
    x: c_int
    y: c_int
```
or
```python
@annotated
class POINT(Structure):
    x: int = field(type=c_int)
    y: int = field(type=c_int)
```
