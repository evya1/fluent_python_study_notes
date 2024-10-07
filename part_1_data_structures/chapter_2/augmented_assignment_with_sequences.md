# Augmented Assignment with Sequences

### Key Points and Tips

1. **Augmented Assignment Operators**: Operators like `+=` and `*=` behave differently based on the type of the first operand (mutable or immutable sequence).

2. **`__iadd__` for `+=`**: The `__iadd__` method is responsible for *in place* addition. If this method is not implemented, Python falls back to `__add__`, which creates a new object rather than modifying the original one *in place*.

3. **Mutable Sequences**: For **mutable** sequences (e.g., `list`, `bytearray`), `__iadd__` is usually implemented, and `+=` will modify the object *in place* (similar to `extend()`). The object's identity remains unchanged.

4. **Immutable Sequences**: For **immutable** sequences (e.g., `tuple`), `+=` results in a new object, as `__iadd__` cannot modify the original object *in place*. The identity of the object changes after the operation.

5. **In-Place vs. New Object**: When using `+=`:
   - For **mutable** sequences: modification happens *in place*.
   - For **immutable** sequences: a new object is created, leading to inefficiency in repeated concatenation.

6. **`__imul__` for `*=`**: Similar to `+=`, the `*=` operator calls `__imul__` for *in place* multiplication of **mutable** sequences. If unavailable, Python falls back to creating a new object with `__mul__`.

7. **Performance Concern**: Repeated concatenation of **immutable** sequences is inefficient because Python has to copy the entire sequence to create a new one. This is slower compared to *in place* modification of **mutable** sequences.  
   <span style="color:pink">Performance Note:</span> This inefficiency is especially evident when concatenating large **immutable** sequences multiple times.

8. **Immutable Sequences Corner Case**: Tuples, despite being **immutable**, can demonstrate interesting behavior in certain contexts (e.g., concatenation via `+=` or `*=`) that exposes how "immutability" works.

---

### Special Case: `str` Optimization

- **Exception for `str`**: Although repeated concatenation of **immutable** sequences is generally inefficient, the `str` type is an exception. In **CPython**, the interpreter is optimized for string concatenation using `+=` inside loops, which is common in many codebases.  
   <span style="color:pink">Performance Note:</span> This optimization makes string building with `+=` relatively efficient compared to other **immutable** sequence types like tuples, even though it involves creating new objects.
