# message = input(">")
# words = message.split(' ')

# print(words)
# emoji= {
#     ":)": "😄",
#     "(:": "😧"
# }
# output = ""
# for word in words:
#     output += emoji.get(word,word)+" "

# print(output)

def emoji_Converter(message):
    words =message.split(' ')
    emoji= {
    ":)": "😄",
    "(:": "😧"
}
    output = ''
    for x in words:
        output = output + emoji.get(x,x)+" ";
    return output;

x = emoji_Converter("Yogesh shaha :)")
print(x)
    