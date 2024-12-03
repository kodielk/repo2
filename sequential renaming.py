def rename_selections(selections, naming_scheme):
    """
    renames the provided selections based on the specified naming scheme.
    
    """
    # Validate the naming scheme
    if '#' not in naming_scheme:
        raise ValueError("naming scheme must contain at least one '#' character for numbering.")
    
    # Split the naming scheme to find the padding
    prefix, sep, suffix = naming_scheme.partition('#' * naming_scheme.count('#'))
    padding_length = len(sep)  # Number of '#' determines padding length
    
    new_names = []
    
    for i, obj in enumerate(selections, start=1):
        # Format the number with zero padding
        number = str(i).zfill(padding_length)
        new_name = f"{prefix}{number}{suffix}"
        new_names.append(new_name)
    
    return new_names


# Example usage:
# Selections can be a list of objects, e.g., ["obj1", "obj2", "obj3"]
selections = ["obj1", "obj2", "obj3"]
naming_scheme = "Leg_##_Jnt"

# Rename the selections
try:
    renamed_objects = rename_selections(selections, naming_scheme)
    print("Renamed objects:", renamed_objects)
except ValueError as e:
    print("Error:", e)
