# program that takes two names and calculates the love amount
# counts the total amount of letters in TRUE and LOVE found in each person's name and then concatenates those two digits together

# some of the logic can be put into another function to remove redundancy

def calculate_love_score(first, second):
    t_count = 0
    r_count = 0
    u_count = 0
    e_count_first = 0
    l_count = 0
    o_count = 0
    v_count = 0
    e_count_second = 0

    # logic responsible for counting the times the letters in the words TRUE and LOVE appear in the user's selected names.
    for char in first:
        if char.upper() in "TRUE"[0]:
            t_count += 1
        if char.upper() in "TRUE"[1]:
            r_count += 1
        if char.upper() in "TRUE"[2]:
            u_count += 1
        if char.upper() in "TRUE"[3]:
            e_count_first += 1
    
    for char in second:
        if char.upper() in "TRUE"[0]:
            t_count += 1
        if char.upper() in "TRUE"[1]:
            r_count += 1
        if char.upper() in "TRUE"[2]:
            u_count += 1
        if char.upper() in "TRUE"[3]:
            e_count_first += 1

    for char in first:
        if char.upper() in "LOVE"[0]:
            l_count += 1
        if char.upper() in "LOVE"[1]:
            o_count += 1
        if char.upper() in "LOVE"[2]:
            v_count += 1
        if char.upper() in "LOVE"[3]:
            e_count_second += 1
    
    for char in second:
        if char.upper() in "LOVE"[0]:
            l_count += 1
        if char.upper() in "LOVE"[1]:
            o_count += 1
        if char.upper() in "LOVE"[2]:
            v_count += 1
        if char.upper() in "LOVE"[3]:
            e_count_second += 1

    true_count = t_count + r_count + u_count + e_count_first # sum of the TRUE counts
    love_count = l_count + o_count + v_count + e_count_second # sum of the LOVE counts
    
    print(f"{true_count}{love_count}") # concatenates the two sums

first_name = input("What is the first name? ")
second_name = input("What is the second name? ")
calculate_love_score(first_name, second_name)

def calculate_love_score_alternate_function(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")