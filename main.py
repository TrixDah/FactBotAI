# This is the code for the FactBot
# Have a look at the README for more info

response_status = 0
begin_status = 0

while True:
    if response_status == 0:
        if begin_status == 0:
            beg_answer = input("Welcome to FactBot, an experimental AI built around printing facts. Let's begin: ")
            answer = beg_answer.lower()
            response_status = 1
            begin_status = 1
        else:
            beg_answer = input("Prompt: ")
            answer = beg_answer.lower()
            response_status = 1
    if response_status == 1:
        if "random" in answer:
            print("Watching a graduation ceremony is like sitting through a movie that's entirely end credits")
            response_status = 0
        elif "france" in answer:
            if "capital" in answer:
                print("The capital of France is Paris, but I think it should be Disneyland")
                response_status = 0
            else:
                print("The capital of France is F")
                response_status = 0
        elif "math" in answer:
            print("Idk maths, sorry D:")
            response_status = 0

        else:
            print("We don't have a suitable answer for that yet, we should soon! ")
            response_status = 0