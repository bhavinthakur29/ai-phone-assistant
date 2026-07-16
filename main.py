from assistant.parser import Parser
from assistant.dispatcher import Dispatcher


dispatcher = Dispatcher()

print("AI Phone Assistant")
print("------------------")

while True:

    command = input("> ")

    if command.lower() == "exit":
        break

    try:

        action = Parser.parse(command)

        print(action)

        dispatcher.execute(action)

    except Exception as e:
        print(e)