def get_ai_response(user_query):
    """
    Simulates a call to an AI API (like Google's Gemini API or OpenAI).
    For the assignment, this function returns a generic AI-like response.
    """
    if "iron lady" in user_query or "about" in user_query:
        return "I am a helpful assistant for Iron Lady. What would you like to know?"
    elif "leadership" in user_query:
        return "Our leadership programs are designed to empower aspiring leaders with practical skills and mentorship."
    elif "career" in user_query or "job" in user_query:
        return "Our programs are tailored to help you advance your career and achieve your professional goals."
    else:
        return "I can try to answer general questions, but my primary knowledge is about Iron Lady's leadership programs."
def chatbot():
    print("Hello! I am the Iron Lady chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        if "programs" in user_input:
            print("Chatbot: We offer a variety of leadership programs, including the 'Empowerment Leadership Program' and 'Tech-Innovation Program'.")
        elif "duration" in user_input:
            print("Chatbot: The duration for most programs is 12 weeks, but this can vary depending on the program.")
        elif "online or offline" in user_input or "mode" in user_input:
            print("Chatbot: All of our programs are currently conducted online.")
        elif "certificates" in user_input:
            print("Chatbot: Yes, participants who successfully complete the program receive a certificate of completion.")
        elif "mentors" in user_input or "coaches" in user_input:
            print("Chatbot: Our mentors are industry experts and seasoned professionals with extensive experience in their respective fields.")
        elif user_input in ["exit", "bye", "quit"]:
            print("Chatbot: Goodbye! Feel free to reach out if you have more questions.")
            break
        else:
            # Instead of a default message, pass the unknown question to an AI function
            ai_response = get_ai_response(user_input)
            print(f"Chatbot: {ai_response}")
if __name__=="__main__":
    chatbot()