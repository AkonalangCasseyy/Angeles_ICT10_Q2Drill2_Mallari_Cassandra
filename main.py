from pyscript import document, display

club_members = ["Cassandra Mallari", "Denie Manuntag", "Madeline Narciso", "Jiuliano Rivera"]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = ""
    for item in club_members:
        display(item, target="output")

def check_member(e):
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()
    full_name = f"{f_name} {l_name}"
    
    has_text = bool(f_name) and bool(l_name)
    is_member = full_name in club_members
    

    index = int(has_text) * (1 + int(is_member))
    
    messages = [
        "<span class='text-warning'>Please enter both first and last name.</span>",
        f"<span class='text-danger'>Sorry {full_name}, your application has been denied.</span>",
        f"<span class='text-success'>Congratulations {full_name}! You are now part of the Communication Arts Club.</span>"
    ]
    
    document.getElementById("message").innerHTML = messages[index]
    
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""

show_list()