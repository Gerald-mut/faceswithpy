# Create a a funcion
def convert(text):

    # Convert :) to 🙂
    text = text.replace(":)", "🙂")

    # Convert :( to 🙁
    text = text.replace (":(,", "🙁")

    # Return the modified text
    return text

# Implement a function called main
def main():

        # Prompt user for input
    user_input = input("Enter text: ")

    # Call convert and store the result
    converted_text = convert(user_input)

    # Print the convrted text
    print(converted_text)

    # Call main
if  __name__ == "__main__":
    main()
