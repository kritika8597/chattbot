from chatterbot import ChatBot # method to import the chatbot
from chatterbot.trainers import ListTrainer # method to import the chatbot
#from tkinter import *
#o = Tk()

bot = ChatBot('Ron Obvious',
input_adapter="chatterbot.input.VariableInputTypeAdapter",
output_adapter="chatterbot.output.OutputAdapter",
output_format="text",
              
input_adapter1="chatterbot.input.TerminalAdapter",
output_adapter1="chatterbot.output.TerminalAdapter",

input_adapter2="chatterbot.input.Gitter",
output_adapter2="chatterbot.output.Gitter",
gitter_api_token="my-gitter-api-token",
gitter_room="my-room-name",
gitter_only_respond_to_mentions=True,)
conversation = open("chat.txt",'r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conversation)
while True:
    l1 =(input('you:'))
    l2 = bot.get_response(l1)
    print('Bot:',l2)
    
#response = bot.get_response("what is ur name")
#print(response)
