import os


def parallel_assignment():
    """
    Demonstrates unpacking through parallel assignment,
    where values from an iterable are directly assigned to variables.
    """
    title = "Parallel Assignment"
    print("\n" + title)

    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates

    print("Latitude:", latitude)
    print("Longitude:", longitude)


def swap_variables():
    """
    Illustrates the elegant usage of unpacking by swapping variable values without the need for a temporary variable.
    """
    title = "Variable Swapping using Unpacking"
    print("\n" + title)

    a = 10
    b = 20

    print("Before swapping:")
    print("a =", a)
    print("b =", b)

    b, a = a, b

    print("\nAfter swapping:")
    print("a =", a)
    print("b =", b)


def unpacking_function_arguments():
    """
    Demonstrates unpacking by prefixing an argument with * when calling a function.

    This example illustrates how to unpack an iterable, such as a tuple, and pass its elements
    as arguments to a function using the * operator. It allows for concise and readable code,
    especially when dealing with functions that accept multiple arguments.
    """
    title = "Unpacking Function Arguments"
    print("\n" + title)

    t = (20, 8)

    quotient, remainder = divmod(*t)
    print(quotient, remainder)


def handle_multiple_return_values():
    """
    Demonstrates unpacking to handle multiple return values.

    Shows how unpacking is used to conveniently handle multiple return values from a function.
    Here, the os.path.split() function returns a tuple with the path and the last part of a
    filesystem path.
    """
    title = "Handling Multiple Return Values"
    print("\n" + title)

    _, filename = os.path.split('./example_folder/example_file.txt')
    print(f"{filename= }")


def grab_excess_items():
    """
    Demonstrates using * to grab excess items in unpacking.

    This example showcases how the * operator in unpacking allows for capturing arbitrary excess items,
    useful when dealing with functions or assignments that may receive more items than expected.
    It demonstrates various scenarios, including handling excess items after assigning specific variables
    and using * to capture excess items before or between specified variables.
    """
    title = "Using * to Grab Excess Items"
    print("\n" + title)

    # Example 1: Capture excess items after assigning 'a' and 'b' variables.
    a, b, *rest = range(5)
    print(f"1. {a=}, {b=}, {rest=}")

    # Example 2: Handle fewer items in the iterable, leaving 'rest' empty.
    a, b, *rest = range(3)
    print(f"2. {a=}, {b=}, {rest=}")

    # Example 3: No excess items, 'rest' remains empty.
    a, b, *rest = range(2)
    print(f"3. {a=}, {b=}, {rest=}")

    # Example 4: Capture excess items between 'a' and 'c' variables using '*body'.
    a, *body, c, d = range(5)
    print(f"4. {a=}, {body=}, {c=}, {d=}")

    # Example 5: Capture excess items before 'b' using '*head'.
    *head, b, c, d = range(5)
    print(f"5. {head=}, {b=}, {c=}, {d=}")


def main():
    parallel_assignment()
    swap_variables()
    unpacking_function_arguments()
    handle_multiple_return_values()
    grab_excess_items()


if __name__ == "__main__":
    main()
