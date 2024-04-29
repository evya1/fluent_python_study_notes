# Examples of Using the `as` Keyword in Pattern Matching

## Overview
This document provides examples of using the `as` keyword to bind parts of patterns to variables in Python's pattern matching.

## Table of Contents
1. [Example 1: Nested Lists](#example-1-nested-lists)
2. [Example 2: Multiple As Bindings](#example-2-multiple-as-bindings)
3. [Example 3: Complex Nested Structures](#example-3-complex-nested-structures)
4. [Example 4: Tuple with Mixed Types](#example-4-tuple-with-mixed-types)

## Example 1: Nested Lists
Binding parts of a nested list pattern:

```python
data = ["Alice", 25, "Engineer", [51.5074, -0.1278]]

match data:
    case [name, age, _, (lat, lon) as coord]:
        print(f"Name: {name}, Age: {age}, Coordinates: {coord}")
        # Output: Name: Alice, Age: 25, Coordinates: [51.5074, -0.1278]
```

## Example 2: Multiple As Bindings
Binding multiple parts within a single pattern:

```python
data = ("Frank", (40, "Director"), ["Java", "C++"])

match data:
    case (name, (age, title as job_title), skills as skillset):
        print(f"Name: {name}, Age: {age}, Job Title: {job_title}, Skills: {skillset}")
        # Output: Name: Frank, Age: 40, Job Title: Director, Skills: ['Java', 'C++']
```

## Example 3: Complex Nested Structures
Binding parts of a complex nested structure:

```python
data = {"user": {"id": 123, "name": "Dana"}, "location": {"city": "Paris", "coordinates": (48.8566, 2.3522)}}

match data:
    case {"user": {"id": user_id, "name": user_name as uname}, "location": {"coordinates": (lat, lon) as coord}}:
        print(f"User ID: {user_id}, Name: {uname}, Coordinates: {coord}")
        # Output: User ID: 123, Name: Dana, Coordinates: (48.8566, 2.3522)
```

## Example 4: Tuple with Mixed Types
Binding parts of a tuple with mixed types:

```python
data = ("Charlie", (34, "Manager"), ["Python", "JavaScript"])

match data:
    case (name, (age, title), skills as skillset):
        print(f"Name: {name}, Age: {age}, Title: {title}, Skills: {skillset}")
        # Output: Name: Charlie, Age: 34, Title: Manager, Skills: ['Python', 'JavaScript']
```

