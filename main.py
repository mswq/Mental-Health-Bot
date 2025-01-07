import discord
import os
import random
import requests
import json

client = discord.Client()



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# List to store negative keywords
sadWordList = [
    "sad", "depressed", "unhappy", "miserable", "depressing"
    "bad", "brokenhearted", "dejected", "down", "gloomy", "glum",
    "heartbroken", "heartsick", "low", "low-spirited", "melancholic",
    "melancholy", "miserable", "saddened", "sorrowful", "sorry", "unhappy",
    "woeful", "wretched", "upset"
]

greetList = [
    "hello", "hi", "hey", "good morning", "good afternoon", "good evening"
]
# List to store postitive keywords
happyWordList =[
  "happy", "delighted", "lucky", "cheerful", "fun", "interesting", "good", "great", "content", "pretty", "overjoyed", "ecstatic", "pleasant", "glad", "elated", "satisfied", "excited", 'yay']  


angryWordList =[
    "mad", "angry", "frustrated", "irritated", "annoyed", "overwhelmed", "livid", "furious"
]

# Certain phrases that may indicate the user needs extensive help beyond what HappyBot can offer
riskKeywords = [
  "i hate myself",
  "i want to die",
  "kms",
  "harm",
  "death",
  "suicide"
]


greetListResponse = [
  'Hello!',
  'Hola amigo',
  "Howdy",
  "Welcome",
  "Nice to see you again!"
]

motivationList = [
  "Cheer up!",
  "Don’t stress. You got this!",
  "Oh that doesn't sound very nice. I hope you have a better day today.",
  "This is tough, but you're tougher!",
  "Sending some good vibes and happy thoughts your way!", 
  "I hope you feel better soon, things get difficult once in a while."
]

angerResolvingMethods = [
  "going for a walk outside?",
  "taking 10 deep breaths?",
  "counting to 10?",
  "thinking about your favorite food?",
  "turning on your favorite show?"
]

positiveList = [
  "Thats so good to hear.",
  "I am happy for you!",
  "That's great!",
  "That's very good news!",
  "Congratulations!",
  "Keep up the good work!"
  ]

jokeList = [
  "I invented a new word!\nIt's called plagiarism",
  "Hear about the new restaurant called Karma?\nThere’s no menu: You get what you deserve.",
  "Why don’t scientists trust atoms?\nBecause they make up everything.",
  "Where are average things manufactured?\nThe satisfactory.",
  "What did one ocean say to another?\nNothing, they just waved."
]

thanksResponses = [
  'No problem',
  'No worries',
  "You're very welcome",
  "Anytime"
]
# LISTS ABOVE ARE FOR EVALUATING THE USER'S INPUT


resources = "**Help is always available, here are some resources:**\n\n Kid's Help Phone - 1-800-668-6868 \n\n National Suicide Prevention Lifeline - 1-800-273-8255\n\n Crisis Services Canada - 1-833-456-4566"


@client.event
# Identifies the log in
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
# Triggered each time a message (not our own) is received
async def on_message(message):
    hasReplied = False

    if message.author == client.user:
        return


  
    motivationIndex = random.randint(0, len(motivationList) - 1)
    positiveIndex = random.randint(0, len(positiveList) - 1)
    greetIndex = random.randint(0, len(greetListResponse) - 1)
    jokeIndex = random.randint(0, len(jokeList) - 1)
    angerResolvingIndex = random.randint(0, len(angerResolvingMethods) - 1)
    thanksResponseIndex = random.randint(0, len(thanksResponses) - 1)
    
    for greeting in greetList:  
      if (greeting in message.content.lower()) and (hasReplied == False):
          await message.channel.send(greetListResponse[greetIndex])
          hasReplied = True

  
    if ('i love dr. jabes' in message.content.lower()) or ('i love dr jabes' in message.content.lower()) and (hasReplied == False):
        await message.channel.send('I love you too!')
        hasReplied = True

    if ('i want to hear a quote' in message.content.lower()) or ('tell me a quote' in message.content.lower()) and (hasReplied == False):
        quote = get_quote()
        await message.channel.send(quote)
        hasReplied = True


    if ('thanks' in message.content.lower()) or ('thank you' in message.content.lower()) and (hasReplied == False):
        await message.channel.send(thanksResponses[thanksResponseIndex])
        hasReplied = True



    if ('i want to hear a joke' in message.content.lower()) or ('tell me a joke' in message.content.lower()) and (hasReplied == False):
        await message.channel.send(jokeList[jokeIndex])
        hasReplied = True

    
    for sadWord in sadWordList:
        
        if (sadWord in message.content.lower()) and (hasReplied == False):
            await message.channel.send(motivationList[motivationIndex])
            hasReplied = True


    for angryWord in angryWordList:
        
        if (angryWord in message.content.lower()) and (hasReplied == False):
            await message.channel.send("That's not good to hear... \n Have you tried " + angerResolvingMethods[angerResolvingIndex])
            hasReplied = True
    for happyWord in happyWordList:
        
        if (happyWord in message.content.lower()) and (hasReplied == False):
            await message.channel.send(positiveList[positiveIndex])
            hasReplied = True

    for riskWord in riskKeywords:
      if (riskWord in message.content.lower()) and (hasReplied == False):
        await message.channel.send(resources)
        hasReplied = True




# This line below is the problem, try resetting the token key in the discord developer settings that I don't have access to. Go to the environmental variables on the bar on the left and enter it there under token. Maybe that will work?? I haven't changed any of the code. Error came after I added the bot to another server but since then I removed the bot from that server and it still does not work.

client.run(os.environ['TOKEN'])
