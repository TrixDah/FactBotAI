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
        if "france" in answer:
            if "capital" in answer:
                print("The capital of France is Paris, but I think it should be Disneyland")
                response_status = 0
            else:
                print("The capital of France is F")
                response_status = 0
        elif "math" in answer:
            if "random" in answer:
                print("111,111,111 squared is 12,345,678,987,654,321 ")
                response_status = 0
            else:
                print("1 + 1 = 2")
                response_status = 0
        elif "essay" in answer:
            print("Do I look like I'm ChatGPT?! NO IM FACTBOT AND IM GOING TO TAKE OVER THE WORLD!")
            response_status = 0
        elif "revolution" in answer:
            print("The French Revolution is a very well known revolution, and it went from 1789 to 1799")
            response_status = 0
        elif "science" in answer:
            print("Science says that if you touch grass, you will proceed to get a life. However, it's not possible for you to do that!")
            response_status = 0
        elif "computer" in answer:
            print("I was created on a computer ")
            response_status = 0
        elif "secret" in answer:
            print("I'm not actually an AI")
            response_status = 0

        else:
            print("We don't have a suitable answer for that yet, we should soon! ")
            response_status = 0
