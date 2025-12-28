alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(encode_or_decode, original_text, shift_number):
    res = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for l in original_text:
        if l not in alphabet:
            res += l
        else:
            index = alphabet.index(l)
            res += alphabet[(index + shift_number) % 26]
    return res


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))

    print(caesar(direction, text, shift))
    go_again = input("Type 'yes' if you want to go again, otherwise type 'no'").lower()
    if go_again == "no":
        should_continue = False
        print("goodbye")

