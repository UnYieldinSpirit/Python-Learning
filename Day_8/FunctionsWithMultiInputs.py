def greet_with_name(name, location):
    print(f"Hello, {name}")
    print(f"How is it in, {location}?")

greet_with_name("Emilee", "bed") # positional arguments
greet_with_name(location = "Maryland", name = "Emilee") # keyword arguments