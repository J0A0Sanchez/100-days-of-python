#Using return  on functions with multiple returns

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "no inputs"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    

formated_string = format_name(input("First name:"), input("Last name:"))
print(formated_string)
