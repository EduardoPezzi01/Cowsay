userText = input("Digite uma frase para vaquinha!")
words = userText.split()

if len(words) > 8:
    firstLine = " ".join(words[:len(words)//2 + 1])
    secondLine = " ".join(words[len(words)//2 + 1:])
    line = (len(firstLine) + 4) * "-"
    padding = (len(firstLine) - len(secondLine)) * " "
    content = "| " + firstLine + "|\n|" + secondLine + padding + " |"
else:  
    line = (len(userText) + 4) * "-"  
    content = "| " + userText + " |"

container = [line, content, line]

for item in container:
    print(item)

cow = ("         \\ ^__^",
"         \\ (oo) \\________",
"           (__) \\        )\\/\\",
"                  ||----W |",
"                  ||     ||")

for item in cow:
    print(item)