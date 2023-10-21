import openai

openai.api_key = input("give me your key or else > ") # input for your key

while True:
    print("Enter something (or 'exit' to quit): ")
    userInput = input("> ")
    if userInput.lower() == "exit":
        break #exit the loop
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt= userInput,
      max_tokens=200
    )

    print(response.choices[0].text.strip())
