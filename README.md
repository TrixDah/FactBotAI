# FactBotAI
Welcome to FactBotAI. We are a small project, trying to make a wikipedia of sorts, but with a AI chatbot-esque style. We aren't actually using AI, but we want to make it feel like an AI. Instead of feeling official, we want the feel of the responses to be conversational and casual. Currently, topics like science and maths have jokes instead of facts, feel free to actually do that!

To set a new fact, just do this:
    if "keyword" in answer:
        print("Answer")
        response_status = 0
In the keyword, the code looks for a certain string of letters in the answer, and then prints the answer. Then, we set the response_status to 0, so that we can restart the process of getting a prompt. 

However, if you want to add a fact to check if the word math and geometry are in the same prompt, check for this code:
    if "math" in answer:
        (Rest of Code)
So, that way we don't check for math twice in the loop. Then, just put an if when it is the first answer in that section, or an elif if it isn't. Here's an example:
    if math in answer:
        if "geometry" in anwer:
            print("Answer")
            response_status = 0
And that's the guide for the code, for now :D    
