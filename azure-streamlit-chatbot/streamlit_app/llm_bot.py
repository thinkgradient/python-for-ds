from az_openai import ChatBotClient

# Description: This file contains the logic for the LLM bot
def dummy_bot(msg):
    return "Dummy bot: I'm a dummy bot"

def echo_bot(msg):
    return 'Echo: {}'.format(msg)

def simple_llm(msg):
    bot = ChatBotClient()
    msgs = [
        {"role": "system", "content": "You are an AI chatbot built by Vodafone. You can answer any question about Vodafone offers."},
        {"role": "user", "content": msg}
    ]
    response = bot.get_chat_response(msgs)
    return  response