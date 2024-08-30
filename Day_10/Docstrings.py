def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    # Docustrings are strings used to document a Python module, class, function or method
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("Michael", "Jackson")

length = len(formatted_name)