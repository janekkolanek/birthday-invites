with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    invite_path = f"./Output/ReadyToSend/letter_for_{name}.txt"

    with open(invite_path, "w") as invite_file:
        with open("./Input/Letters/starting_letter.txt", "r") as starting_letter_file:
            invite_content = starting_letter_file.read()
            invite_content = invite_content.replace("[name]", name)
            invite_file.write(invite_content)
