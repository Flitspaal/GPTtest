import openai

openai.api_key = input("give me your key or else > ") #put in your key

while True:
    print("Enter something (or 'exit' to quit): ")
    userInput = input("> ")

    # program options
    if userInput.lower() == "exit": # exit the program
        break #exit the loop
    if userInput.lower() == "reply": # uses last response to go deeper in on the awnser
        userInput = input("> ")
        userInput = userInput + lastReplie
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= userInput,
            max_tokens=200
        )
    else: # standard option
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt= userInput,
          max_tokens=200
        )

    # Print response
    print(response.choices[0].text.strip())
    lastReplie = response.choices[0].text.strip()

print("thanks for using GPTest")
