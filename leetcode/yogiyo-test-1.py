def check_duplicate(Email_name, Email):
    i = 1
    if Email_name in Email:
        Email_name = Email_name+str(i+1)
        if Email_name+str(2) in Email_name:
            i = 2
            Email_name = Email_name+str(i+1)
    return Email_name


def solution(S, C):
    # write your code in Python 3.6
    Names = S.split(", ")
    Email = ""
    Email_names = ""
    i = 1
    for name in Names:
        First_name = name.split(" ")[0].lower()
        Last_name = name.split(" ")[-1].lower()
        Last_name = Last_name.replace("-", "")
        Email_name = First_name + "." + Last_name
        Email_List.append(Email_name)

    return Email


C = "Example"
S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"

print(solution(S, C))
