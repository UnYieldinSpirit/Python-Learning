def format_name(f_name, l_name):
    formatted_f_name = f_name.title() # title makes the string like so: Example. Capital first letter and lowercase remainder
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("gLoRIa","HENDRICKS"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)