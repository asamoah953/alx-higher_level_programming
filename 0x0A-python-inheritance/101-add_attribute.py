def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object cannot have new attributes.

    Returns:
        None
    """
    if hasattr(obj, '__dict__') or hasattr(type(obj), '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
