#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#collecting the name of the user
first_name = input("Please enter your preferred name: ")

#determining the mood of the user and giving them a mood prompt

feeling = input("How are you feeling? Please select from the following options: Happy, Excited, Calm, Sad, Angry, Nervous, Guilty, Fearful, or I do not know.: ")
if feeling == 'Happy':
    print("Hi", first_name,". Tell us what's making you happy? What about it makes you happy?:")
elif feeling == 'Excited':
    print("Hi", first_name, "What are you most excited about? What makes it exciting?")
elif feeling == 'I do not know':
         print("Hi", first_name, "It is okay not to know how you're feeling. Try to put it into a category of good or bad. Make a playlist or find images that reflect how you're feeling. Having something to represent your feelings can aid in determining your emotions.")
elif feeling == 'Calm':
    print("What gave you this sense of serenity? Can you recreate this feeling or is it unique to this moment?")
elif feeling == 'Sad':
    print("Saddness is completely normal. Take some deep breaths and think or write about what could be the source of your saddness. If you don't know, that's okay! Emotions are complicated and hardly ever straightforward. It's okay to sit in the sadness for a little bit, but don't dwell in it too long. Do something you enjoy or try something new when the time is right for you. ")
elif feeling == 'Angry':
    print("Anger can be a powerful emotion. What is the source of this anger? If you don't know, that's okay! Here are some healthy ways of coping: Scream into a pillow, go for a walk, throw some rocks, or sing a loud song.")
elif feeling == 'Nervous':
    print("Try taking deep breaths to regulate your nervous system.")
elif feeling == 'Guilty':
    print("Everyone does wrong things and as a byproduct, we feel wrong for it, but sometimes we blame ourselves for situations that aren't our fault. Why are you feeling guilty? Have you wronged someone and need to talk to them about it? Maybe you've done something wrong and should resolve it before it becomes a problem. It's always best to be honest with yourself and take steps to fix your mistakes.")
elif feeling == 'Fearful':
    print("Find somewhere that makes you feel safe. If you can't, do something that gives comfort. Such as listening to a familiar song, or watching your favorite TV show!")
    
#journal prompts

import random

prompt = ["What are you grateful for?", "Who is your favorite person?", "Do you believe in aleins?", "What kind of ruler do you think you would be?", "Write down a confession."]
question = input("Would you like a journal prompt? Yes or No: ")
journal_prompt = random.choice(prompt)
if question == 'Yes':
    print(journal_prompt)
elif question == 'No':
    print("Disregard the following prompt.")

