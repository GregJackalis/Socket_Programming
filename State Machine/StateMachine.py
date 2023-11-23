import hashlib

user_list = [
    ("Chris", "Password", "SALT12345"), ("Patrick", "Password", "SALT23456"), ("Admin", "Password", "SALT12345")
]
state_list = ["START_STATE", "NEGOTIATION", "LOGIN", "STATE1", "REPEATING_STATE", "OTHER_STATE", "TERMINATE"]
current_state = "START_STATE"
next_state = "NONE"
prev_state = "NONE"

user_input = ""
message = ""

while current_state != "TERMINATE":
    if current_state == "START_STATE":
        for state in state_list:
            i = state_list.index(state)
            print(f"{i}: {state}")
        user_input = int(input("What would you like to do: "))
        next_state = state_list[user_input]
    elif current_state == "NEGOTIATION":
        options = ["C", "V", "O"]
        user_input = input("Choose an option: (C)aesar, (V)ignere, (O)ther")
        next_state = current_state

        for option in options:
            if user_input == option:
                next_state = "LOGIN"

    elif current_state == "LOGIN":

        username = input("Enter a username: ")
        password = input("Enter your password")
        found = False

        for user in user_list:
            # Split the user tuple into its component parts
            user_name, pass_word, salt = user

            # Create the MD5 Hash of the entered password postpended with the salt value
            combined_string = password + salt
            md5Hash = hashlib.md5()
            md5Hash.update(combined_string.encode())
            entered_salted = md5Hash.digest()
            print(f"Password: {password}, Salt: {salt}")
            print(f"The hash of the entered password is: {entered_salted}")

            # Create the MD5 Hash of the stored password postpended with the salt value
            combined_string = pass_word + salt
            md5Hash = hashlib.md5()
            md5Hash.update(combined_string.encode())
            current_salted = md5Hash.digest()
            print(f"Password: {password}, Salt: {salt}")
            print(f"The hash of the stored password is: {current_salted}")
            # Perform comparisons, ensure that found cannot be set False within the loop
            if username == user_name and entered_salted == current_salted:
                print("The username and password matched")
                found = True
                break

        if found:
            next_state = "STATE1"
        else:
            next_state = current_state

    elif current_state == "STATE1":
        print("Look at me, I'm a state!")
        next_state = "REPEATING_STATE"
    elif current_state == "REPEATING_STATE":
        user_input = input("Enter (Stay) to stay in this state, (Go) to change state")
        if user_input == "Stay":
            next_state = current_state
        elif user_input == "Go":
            next_state = "OTHER_STATE"
        else:
            print("Hey you cheated, I should have validated the input... watch me crash")
    elif current_state == "OTHER_STATE":

        user_input = input("Enter a string containing wakkawakka to terminate")
        if "wakkawakka" in user_input:
            next_state = "TERMINATE"
        else:
            message = message + user_input
            print(message)
            next_state = current_state
    elif current_state == "TERMINATE":
        print("You can never reach this due to the way this state machine is constructed")
        print("If you need the user to reach a termination state inserting an additional state like STATE1")
        print("will let you send output and then auto-transition out")

    # Change the state of the machine, record the previous state so we have memory if needed
    prev_state = current_state
    current_state = next_state
    next_state = "NONE"