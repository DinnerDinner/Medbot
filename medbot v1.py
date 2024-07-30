import audioop
import calendar
import datetime
import re
from tabnanny import verbose
import webbrowser
from setuptools import Command
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import playsound
import os
import random
import time
import pyjokes
import wikipedia
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import subprocess
import json

def medbot_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
#Fetching the microphone, setting up the recognizer as well as possible recognizing errors
def recordAudio(ask = False):


    with sr.Microphone() as source:
        if ask:
            medbot_speak(ask)
        audio = r.listen(source, 7, 7)

        data = ''
        try:
            data = r.recognize_google(audio)
        except sr.UnknownValueError:
            medbot_speak("Sorry, I couldn't understand that, would you mind repeating")
        except sr.RequestError:
            medbot_speak("Sorry but my speech service is malfunctionning")
        print(">>"+ data.lower())
        print("Done Listening")
        return data



#Action of creating a new audio file and deleting instnatly while speaking to the user
def medbot_speak(audio_speak):
    audio_speak = str(audio_speak)
    file = gTTS(text = audio_speak, lang = 'en', slow=False)
    r = random.randint(1, 100000000)
    audio_file = "audio" + str(r) + ".mp3"
    file.save(audio_file)
    # os.system("start realbot.mp3")
    playsound.playsound(audio_file)
    print(audio_speak)
    os.remove(audio_file)

def there_is(terms):
    for terms in terms:
        if terms in data:
            return True





#All variables and dictionaries linked to diseases



anxiety = {

}

stress = {
    "explanation" : "Stress is your body's psychological or physical reaction to daily challenges, and is coping method that can be pushed to a certain extent, although, if this limit is crossed, stress could lead to high and irregular heart rate as well as raise in blood pressure also called hypertension. ",
    "meds" : "take tranquilizers as medication for anxiety and stress, such drugs include xanax and ativan and show effect within an hour. Although, avoid taking an medications whatsoever due to side effects and prefer taking a break, a day off or an appointment for the doctor.",
    "emergency" : " Please note: If your stress is followed by breathing problems, chest pain, extreme fever, or intrusive thoughts, seek medical attention and if you pass out then call 911"
}

cold = {
    "explanation" : "A cold is just an infection in your nose and throat, and isn't much to be concerned about.",
    "reasons"  : " It could be caused due to a virus. It could also be a nasal inflammation, because of allergies such as pollen or dust, as well as caused by nonallergic reasons for exemple air conditionning or smoking.",
    "meds" : "You could blow your nose, take a quick, warm shower, or a cozy nap. If these don't help then you may use nasal sprays, Saline drops, or breathe steam, but don't forget plenty of fluids in any case. ",
    "symptoms" : "A common cold could involve mild fatigue as well as a low fever and a nauseos feeling. ",
    "emergency" : "Please note: In case you have chronic health conditions or if the symptoms worsen, or if a high fever lasts for more then three days, you have difficulty breathing or you experience ear pain and headaches, seek medical attention. On the other hand, if you are ill for over a week or two, talk to your doctor. "
}

flu = {
    "explanation" : "A flu is a virus infection which affects the average person about once a year if they aren't vaccinated, and is deemed more concerning then a cold",
    "meds" : "Try drinking a lot of fluids, and increase your rest for recovery, you may also use pain relievers such as acetiminophen ",
    "symptoms" : "Runny nose, High fever, Achy muscles, Severe fatigue and headaches. Although cold may have similar symptoms but at  mild level instead."
}


headaches = {
    "headaches_type" : "There exists 3 major types of headaches: foremost, tension is caused by stress and muscle tensions, secondly are cluster headaches which cause intense pain around an eye or a side of your head, and finally, the most concerning are migraine headaches, because it generally affect an entire side of the head and would be followed by vomitting, feeling sick, severe diarrhea, extreme sentsitvity to light, and sound.",
    "meds" : "Take ibuprofen which can be found in meds such as Advil, Mortrin IB or Nurofen, or take acetaminophen containing meds such as Tylenol(preferred for kids) or Nyquil.",
    "self-care" : "For an occasional tension headahce, use hot or cold packs, take a warm shower, and rest until you feel better, but if the pain persists for over 2 days then, or if you sense a cluster headache, call your doctor.",
    "please_note" : "If you feel a migraine attack upcoming then avoid any activity and go into a dark room immediately, advised to drink cola or coffee, or taking some aspirin for adults.",
    "emergency" : "Please note: If it's a recurring headache, or if the headache is due to a head injury or even if it's a sudden and sever headache, seek medical attention right away"
}

menieres_disease = {
    "explanation" : "It is a chronic, long-term hearing disorder, described as a buzzing sensation, which usually affects one ear and produces dizziness, vertigo and potentially hearing loss, yet the cause of this disease remains unknown but are linked to viral ear infections.",
    "emergency" : "Please note: There aren't medications nor recovery techniques, it is advised that if your ears are affected by tinnitus, hearing loss, and/or recurring dizziness, and i fit lasts more then a couple of days without a resolution, that you seek medical attention to get an accurate diagnosis."
}

insomnia = {
    "meds" : "Meds such as antidepressants like Desyrel or benzodiazepines like Xanax, although over usage of such meds might have worse side effects such as depression and suicidal thoughts ",
    "self-care" : "avoid drinking caffeine, alchohol, over-stressing or using stimulants such as nicotine. Also take a shower about an hour or two right before sleep and try sleeping around the same time, in a dark and quiet room every night",
    "emergency" : "Please note: If you struggle to sleep 3 or more nights a week for a straight month or two, seek medical attention and do some urine or blood tests."
}

diuretics = {
    "explanation" : "blood pressure lowering drugs such as antihypertensives, more commonly known as diuretics, might cause dizziness",
    "meds" : "This is a rare side effect, so you should rather reduce your alcohol consumption, if you responsibly drink or don't drink at all, then give a visit to your doctor for a more accurate diagnosis."
}

dehydration_or_starving = {
    "explanation" : "dehydration because you haven't been drinking enough fluids or been over working physically without proper nutrition.",
    "self_care" : "A simple way to deal with this is by taking a break, staying inside, avoid working the eyes, and drinking fluids or eating a proper, well-rounded meal",
    "emergency" : "Seek medical attention if despite drinking a proper amount of water , 2-4 Litres for men and 1-3 Litres for women, daily, and yet feeling dehydrated and dry"
}

hypothermia = {
    "signs" : "The common signs of hypothermia might include red skin, confusion, clumisness, weak pulse and drowsiness other then shivering itself. It could have been caused by  inproper dressing according to the weather, or due to staying out in the cold for too long. ",
    "self_care" : "Stay inside and change your clothes into something dry and warmer, drink a warm beverage such as coffee or tea, call 911 if you suspect that the person or you might have hypothermia, and while waiting for medical help to arrive, keep the pulse in check."
}

frostbite = {
    "causes" : "It is usually associated to a red, white, bluish, grayish or brown skin color at the part of the skin affected, it may also be followed by numbness and unusual chills on that part of the skin",
    "self_care" : "You can gently warm the area but don't use any direct heat such as a heat pad or heater, because it may lead to paralysis, instead avoid drinking or smoking, remove any wet clothes, and especially don't walk if you're forstbitten on the feet.",
    "emergency" : "It will eventually feel better, although it may get worse if not treated, PLEASE NOTE: seek medical attention if you can't stop shivering or feeling very drowsy. On top of that, seek a doctor if the area affected by the frostbite has turned completely white but doesn't cause any pain, or if the part of the skin affected feels warm instead of cold, as they are symptoms of 2nd and 3rd degree frostbites."
}


pulse = ("You can check your pulse by putting your two fingers, your index and middle one either right under your chin on the right side ")





#All variables linked to Symptoms 


symptoms = {
    "fatigue" : "feeling oddly tired also called Fatigued?",
    "pale_skin" : "having an unusual faintness of skin color compared to one's natural skin tone?",
    "weakness" : "having difficulty in moving certain body parts while feeling stressed or exhausted?",
    "chest_pain" : "experiencing an unusual pain around the chest or the shoulders and neck?",
    "cold_hands_or_feet" : "feeling cold on your fingers or toes?",
    "headaches" : "going through pain in any part of your head?",
    "sweating"  : "sweating or perspiring despite no pyhicical activity right now?",
    "tachycardia" : "feeling your heart pound faster then usual?",
    "trembling" : "shaking involuntarily?",
    "dark_yellow_and_strong_smelling_pee" : "or have you been urinating a dark yellow and smelly pee?",
    "body_temperature" : "98.6 Fahrenheit or exactly 37 Celsius",
    "atrial_fibrillations" : "sensing an unusual heart beat?",
    "swollen_legs" : "seeing any parts of your body such as your ankles, legs or feet?",
    "tinnitus" : " hearing a ringing, buzzing, whistling or hissing sound constantly in your ear?",
    "constipation_or_diarrhea" : "having feces discharge, either it being in liquid form and frequently also called diarrhea or feces are hard and painful to pass also called constipation?",
    "insomnia" : "having a sleep disorder, which troubles the sleeping cycle, and doesn't allow one to get quality sleep, or any sleep at all",
}

# pale_skin = recordAudio("Are you " + symptoms["pale_skin"])
# # headaches = recordAudio("Are you " + symptoms["headaches"])
# atrial_fibrillation_and_tachycardia = recordAudio("Are you " + symptoms["atrial_fibrillations"] + " Or are you " + symptoms["tachycardia"])


#All variables linked to Medications

basic_self_care = {
    "fluids" : "It is advised to drink plenty of fluids to avoid dehydration during a fever",
    "rest" : "rest is primordal for recovery and avoid any unnecessary activity",
    "warm_water" : "soak in lukewarm water for 5 to 10 minutes or give a shower to younger ones"
}

basic_meds = {
    "ibuprofen" : "take ibuprofen which can be found in meds such as Advil, Mortrin IB or Nurofen",
    "acetaminophen" : "take acetaminophen containing meds such as Tylenol(preferred for kids) or Nyquil"

}


#All yes possibilities
 
yesz = ("yes" or "yeah" or "yep" or " i think so" or "most likely" or "pretty sure" or "si" or "shit" or "indeed" or "i believe so" or "sort of")


#Response commands, all commands possible resumed into one place
def response(data):
    searches = ["what was", "what were", "what are", "search", "when was", "where was", "where were", "when were", "when is", "when are", "how to", "how can", "why is", "why are", "why were", "why was"]

    if there_is(["what is your name", "what are you called", "your name"]):
        medname = "My name is medbot"
        medbot_speak(medname)  

    if "why were you made"in data:
        med_use = "I was made to keep your health in check but also work as a supportive virtual assistant to enhance your browsing experience"
        medbot_speak(med_use)

    if there_is(["search", "what was", "what were", "what are", "search", "when was", "where was", "where were", "when were", "when is", "when are", "how to", "how can", "why is", "why are", "why were", "why was"]) and (["search on YouTube"]) not in data:
        med_search = recordAudio("What would you like to search")
        url = "https://google.com/search?q=" + med_search
        webbrowser.get().open(url)
        medbot_speak("Here are the results for " + med_search + "on google")

    if "time" in data:
        time_now = (datetime.datetime.now().strftime("It is %I:%M:%p"))
        medbot_speak(time_now + " right now")

    if "find location" in data:
        med_maps = recordAudio("What location are you looking for:")
        url = "https://google.nl/maps/place/" + med_maps
        webbrowser.get().open(url)
        medbot_speak("Here are the results for " + med_maps + "on google maps")

    if there_is(["search on Youtube", "find on YouTube", "YouTube"]):
        med_searchyt = recordAudio("What video are you searching for?")
        url = "https://www.youtube.com/results?search_query=" + med_searchyt
        webbrowser.get().open(url)
        medbot_speak("Here are the results for " + med_searchyt + " on YouTube")

    if "joke" in data:
        medbot_speak(pyjokes.get_joke())
        #THIS API IS NOT WORKING RIGHT NOW BUT WHENEVER IT DOES, TURN IT ON:::
        # url = "http://official-joke-api.appspot.com/random_joke"
        # r = request.urlopen(url)
        # print(r.getcode())
        # med_joke = r.read()
        # jsonData = json.loads(data)
        # print(jsonData)
        # for j in jsonData:
        #     setup = setup["setup"]
        #     punchline = punchline["punchline"]
        #     medbot_speak(j)
    if "even" in data:
        try:
            numbers = int(recordAudio("Please pick a number"))
            r = numbers % 2
            if r == 0:
                medbot_speak("{0} was an even number".format(numbers))
            else:
                medbot_speak("{0} was an odd number".format(numbers))
        except ValueError:
            medbot_speak("Please strictly pick a valid whole number")

    if there_is(["open a new tab", "open tab", "new tab", "google tab", "start browser", "launch browser", "launch google"]):
        url = "https://google.com/"
        webbrowser.get().open(url)
        medbot_speak("Here is a new tab")

    if there_is(["find my exact location", "my exact location", "my location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?"
        webbrowser.get().open(url)
        medbot_speak("Here are the whereabouts of your location")

    if there_is(["weather in"]):
        weather = recordAudio("What city's weathers are you looking for?")
        url = "https://www.google.com/search?q=weather+" + weather + "&rlz=1C1CHZN_enCA970CA970&oq=wether+ddo&aqs=chrome..69i57j0i10j0i512j0i10i512l2j0i10j0i10i512l4.1155j1j7&sourceid=chrome&ie=UTF-8"
        webbrowser.get().open(url)
        med_weather = url.read()
        jsonData = json.loads(data)
        print(jsonData)
        medbot_speak("Here is what I found for on google at " + weather)

    if there_is(["weather"]) and "weather in" not in data:
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        medbot_speak("This is the weather outside")

    if there_is(["what is the news", "current news", "current affairs", "news"]):
        url = "https://www.bloomberg.com/"

        webbrowser.get().open(url)
        medbot_speak("This is Bloomberg.com, an international news channel, enjoy reading...")

    if there_is(["who is"]):
        person = recordAudio("who are you asking for:")
        wiki = wikipedia.summary(person, sentences = 2)
        medbot_speak(wiki)
    
    if there_is(["flip", "coin"]):
        flip = random.randint(0, 1)
        if flip == 0:
            medbot_speak("It was tails!")
        elif flip == 1:
            medbot_speak("It was heads!")

    if there_is(["rock paper scissors", "play rps", "rock", "paper"]):
        rps = ["rock", "paper", "scissors"]
        computer = random.choice(rps)
        player = recordAudio("Pick rock, paper or scissors")
        try:
            if "rock" in player and computer == "rock":
                medbot_speak("You has a tie")
                medbot_speak("The computer also chose:")
                medbot_speak(computer)

                
            elif "rock" in player and computer == "scissors":
                medbot_speak("The computer chose:")
                medbot_speak(computer)

                medbot_speak("YOU WIN!")

            elif "rock" in player and computer == "paper":
                medbot_speak("The computer chose:")
                medbot_speak(computer)
                medbot_speak("You lose")


            elif "paper" in player and computer == "paper":
                medbot_speak("You has a tie")
                medbot_speak("The computer also chose:")
                medbot_speak(computer)

                
            elif "paper" in player and computer == "rock":
                medbot_speak("The computer chose:")
                medbot_speak(computer)

                medbot_speak("YOU WIN!")

            elif "paper" in player and computer == "scissors":
                medbot_speak("The computer chose:")
                medbot_speak(computer)

                medbot_speak("You lose")

            elif "scissors" in player and computer == "scissors":
                medbot_speak("You has a tie")
                medbot_speak("The computer also chose:")
                medbot_speak(computer)

                
            elif "scissors" in player and computer == "paper":
                medbot_speak("The computer chose:")
                medbot_speak(computer)

                medbot_speak("YOU WIN!")
            elif "scissors" in player and computer == "paper":
                medbot_speak("The computer chose:")
                medbot_speak(computer)

                medbot_speak("You lose")
        except ValueError:
            medbot_speak("Pick rock paper or scissors next time...")
    
    if there_is(["play guess", "guessing game", "play guessing", "play number"]):
        computers = random.randint(1,10)
        computer = str(computers)
        try:
            for i in range(0,7):
                guess = str(recordAudio("Guess a number between 1 and 100: \n"))
                if str(guess) == str(computer):
                    medbot_speak("You got it, PERFECT, play again some time")               
                    break
                elif str(guess) > str(computer) and str(computer) % 2 == 0:
                    medbot_speak("TRY LOWER WITH AN EVEN NUMBER")
                elif str(guess) > str(computer) and str(computer) % 2 != 0:
                    medbot_speak("TRY LOWER WITH AN ODD NUMBER")
                elif str(guess) < str(computer) and str(computer) % 2 != 0:
                    medbot_speak("TRY HIGHER WITH AN ODD NUMBER")
                elif str(guess) < str(computer) and str(computer) % 2 == 0:
                    medbot_speak("TRY HIGHER WITH AN EVEN NUMBER")
                else:
                    medbot_speak("Are you retarded, just pick a damn number between 1 and 100.")

            else:
                medbot_speak ("Well too bad, I guess you ran out of tries, press /guess to play again...")
                medbot_speak("The number was:")
                medbot_speak(str(computer))
        except ValueError:
            medbot_speak("Next time input a number between 1 and 100...")

#8ball game;


    
    if there_is(["date today", "what is the date"]):
        date = datetime.datetime.now()
        monthNum = date.month
        dayNum = date.day
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "Septmeber", "October", "November", "December"]
        ordinalNumbers = ['1st','2nd','3rd','4th','5th', '6th', "7th", "8th", "9th", "10th", "11th", "12th", "13th",
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th',
                    '25th', '26th', '27th', '28th', '29th', '30th', '31st']
        medbot_speak('Today is '+months[monthNum-1]+' '+ordinalNumbers [dayNum-1]+'')

    if there_is(["what day is it", "day what", "what day"]):
        date = datetime.datetime.today()
        weekday = calendar.day_name[date.weekday()]
        medbot_speak("Today is "+weekday+"")

#Part regarding all of the diseases and medications: Main stuff===

    #Fevers
    if there_is(["fever", "head is hot"]):
        fever_sure = recordAudio("Are you sure you have a fever after checking the temperature with a thermometer")
        if "yes" or "yeah" or "i think so" or "i am pretty sure" in fever_sure:
            medbot_speak("Fever is just a sign of your body fighting against some infection, like a bacteria such as salmonella, or a virus like covid-19.  " + "You might most likely experience a pain such as a sore throat, an unusual pain around the eyes, a cough, a light chest congestion or a fever due to heat exhaustion")

            fev_question = recordAudio("Is the person you're treating or are you under the age of 18?")
            if "yes" or "yeah" or "yep" in fev_question:
                medbot_speak("In that case, regarding the medication, never give aspirin(acetylsalicylic acid) unless advised specifically by a doctor. Because rarely yet possibly, aspirin can cause serious or fatal diseases." + "Instead " + basic_self_care["fluids"] + ". On top of that " + basic_self_care["rest"] + ". You may also " + basic_self_care["warm_water"] + "If the pain persists or is awful, it is advised to " + basic_meds["ibuprofen"] + ". Or try to " +  basic_meds["acetaminophen"] + ". But long term usage may cause liver or kidney damage so if they don't succeed then call the doctor. On top of that please Note: If you have a severe headache, difficulty breathing, unreasonable irritability, persistent vomiting or severe diarrhea, call 911, or if temperatures of more then 102F or 38.9C for over 48 hours, or a recurring fever, call your doctor.")
            else:
                medbot_speak("In that case," + basic_self_care["fluids"] + ". On top of that " + basic_self_care["rest"] + ". You may also " + basic_self_care["warm_water"])

     
        else:
            medbot_speak("In that case, even though a certain variation in body temperature could be considered healthy, we should still check to be on the safe side. Thus, one way to check is by orally using a thermometer. Clean the tip, turn it on and set it under your tongue in the back of the mouth. If the temperature displayed after the beep hopefully is around" + symptoms["body_temperature"] + " although if it exceeds 100 Farhenheit or 38 Celsius, then it certainly is a fever.")
            body_temp_check = recordAudio("Does your body temperature exceed 100.4 farhenheit or 38 celsius")
            if "yes" or "yeah" or "i think so" or "i am pretty sure" in body_temp_check:
                medbot_speak("Fever is just a sign of your body fighting against some infection like a bacteria, such as salmonella, or a virus like covid-19.  " + "You might most likely experience a pain such as a sore throat, an unusual pain around the eyes, a cough, a light chest congestion or a fever due to heat exhaustion")
                medbot_speak()
                fev_question = recordAudio("Is the person you're treating or are you under the age of 18?")
                if "yes" or "yeah" or "yep" in fev_question:
                    medbot_speak("In that case, regarding the medication, never give aspirin(acetylsalicylic acid) unless advised specifically by a doctor. Because rarely yet possibly, aspirin can cause serious or fatal diseases." + "Instead " + basic_self_care["fluids"] + ". On top of that " + basic_self_care["rest"] + ". You may also " + basic_self_care["warm_water"] + "If the pain persists or is awful, it is advised to " + basic_meds["ibuprofen"] + ". Or try to " +  basic_meds["acetaminophen"] + ". But long term usage may cause liver or kidney damage so if they don't succeed then call the doctor. On top of that please Note: If you have a severe headache, difficulty breathing, unreasonable irritability, persistent vomiting or severe diarrhea, call 911, or if temperatures of more then 102F or 38.9C for over 48 hours, or a recurring fever, call your doctor.")
                else:
                    medbot_speak("In that case," + basic_self_care["fluids"] + ". On top of that " + basic_self_care["rest"] + ". You may also " + basic_self_care["warm_water"])

            else:
                medbot_speak("If you don't believe you have a fever, then try asking me about symptoms you or the patient seem to be affected by currently." + "If the pain persists or is awful, it is advised to " + basic_meds["ibuprofen"] + ". Or try to " +  basic_meds["acetaminophen"] + ". But long term usage may cause liver or kidney damage so if they don't succeed then call the doctor. On top of that please Note: If you have a severe headache, difficulty breathing, unreasonable irritability, persistent vomiting or severe diarrhea, call 911, or if temperatures of more then 102F or 38.9C for over 48 hours, or a recurring fever, call your doctor.") 

    #Heat exhaustion
    if there_is(['heat exhaustion', "heat cramps", "i feel very hot"]):
        medbot_speak("Being exposed to the heat or high temperatures can excessively increase the body temperature")
        heat_exhaustion = recordAudio("Foremost, heat exhaustion may include painful muscle spasms, weakness, dizziness, disorientation and sudden chills. Are you or is the patient subject to these?")
        if ("yes" or "yeah" or "pretty much" or "most likely" or "I think so") in heat_exhaustion:
            medbot_speak("This isn't much to be concerned about, advised to get out of the heat immediately though, as well as quickly grab a drink to avoid dehydration")
        else:
            medbot_speak("Well in that case, ask me about heat strokes or heat cramps instead, but stay inside until you feel better")
        medbot_speak("It is still advised by doctors to avoid being outside during hot days or the afternoons. On top of that wear light colored and cotton clothes during summer. Also prior to going somewhere, ask a doctor once about the effects of heat if you take any medications such as diuretics(for high blood pressure individuals), or antihistamines(for individuals suffering from allergies such as insect bites or stings) ")
    
    #Heat stroke
    if there_is(["heat stroke" or "heatstroke" or "hot outside"]):
        heat_stroke = recordAudio("A heatstroke can be life-threatening and sudden. It could be a heat stroke if the person would stop persipiring suddenly, an increase in heartbeat and the body becoming immessurably hot and dry reaching upto temps of 104 or higher quickly. Are you or is the patient subject to these?")
        if ("yes" or "yeah" or "pretty much" or "most likely" or "I think so") in heat_stroke:
            medbot_speak("Immediately get out of the heat and grab a drink, if you heavily suspect a heat stroke or if the person is unconsious then call 911.")
        else:
            medbot_speak("Nonetheless, take a cold water bathe if you suspect of a heat-related illness, remain indoors and avoid going outside from noon to 4 p.m." + "It is still advised by doctors to avoid being outside during hot days or the afternoons, on top of that wear light colored and cotton clothes during summer and prior to going somewhere ask a doctor once about the effects of heat on you if you take any medications such as diuretics(for high blood pressure individuals) or antihistamines(for individuals suffering from allergies such as insect bites or stings) ")

    
    #Dizzy symptom
    if there_is(["dizzy"]):
        medbot_speak("Dizziness is a symptom linked to multiple diseases, and describes a variety of sensations such as weakness, unsteadiness, or disorientation")
        dizzy_y_or_n = recordAudio("Do you feel like you're swaying, being pulled in a certain direction and unable to stand straight?")
        if yesz in dizzy_y_or_n:
            vertigo = recordAudio("Are you feeling tired, uneasy, nauseous, or is the world around moving or spinning unexplainably, despite eating and drinking well?")
            if yesz in vertigo:
                tinnitus = recordAudio("Are you" + symptoms["tinnitus"])
                if yesz in tinnitus:
                    insomnia_check = recordAudio("Have you been diagnosed with insomnia or been having trouble recently while sleeping?")
                    if yesz in insomnia_check:
                        medbot_speak("In that case, your dizziness and ringing sounds also called tinnitus could be explained due to " + symptoms["insomnia"])
                        medbot_speak("You should also take" + insomnia["meds"] + ". Other then that" + insomnia["self-care"] + ". Finally" + insomnia["emergency"])
                        medbot_speak("Although talking to an ear specialist could be vital about ear infections, labyrinthitis or meniere's disease possibility.")
                    else:
                        medbot_speak("If not, it could be possibly be linked to meniere's disease, " + menieres_disease["explanation"] + ". Other then that; " + menieres_disease["emergency"])

                else:
                    diuretics_y_or_n = recordAudio("Are you diagnosed with a high blood pressure and subject to any meds to reduce blood pressuse?")
                    if yesz in diuretics_y_or_n:
                            medbot_speak("In some cases, dizziness could be linked to " + diuretics["explanation"])
                            medbot_speak(diuretics["meds"])
                    else:   
                        constipation_or_diarrhea = recordAudio("Are you" + symptoms["constipation_or_diarrhea"])               
                        if yesz in constipation_or_diarrhea:
                            head_hurt = recordAudio("Is your head aching on top of the dizziness?")
                            if yesz in head_hurt:
                                medbot_speak(headaches["headaches_type"])
                                medbot_speak("Concerning the meds" + headaches["meds"] + ". Other then that, " + headaches["please_note"] + ". Although, " + headaches["self-care"])
                            else: 
                                medbot_speak("It could also be a case of stress. " + stress["explanation"] + " You can " + stress["meds"] + stress["emergency"])
                        else:
                            head_hurt = recordAudio("Is your head aching on top of the dizziness?")
                            if yesz in head_hurt:
                                medbot_speak(headaches["headaches_type"])
                                medbot_speak("Concerning the meds" + headaches["meds"] + ". Other then that, " + headaches["please_note"] + ". Although, " + headaches["self-care"])
                            else: 
                                medbot_speak("It could also be a case of stress. " + stress["explanation"] + " You can " + stress["meds"] + stress["emergency"])
            else: #dehydration
                medbot_speak("If dizziness occurs without an odd spinning or moving, then it could be a case of " + dehydration_or_starving["explanation"] +  " So " + dehydration_or_starving["self_care"]  + ". Finally " + dehydration_or_starving["emergency"])
        else: #dehydration
            medbot_speak("If dizziness occurs without an odd spinning or moving, then it could be a case of " + dehydration_or_starving["explanation"] +  " So " + dehydration_or_starving["self_care"]  + ". Finally " + dehydration_or_starving["emergency"])            
        medbot_speak("Finally no matter the cause, seek medical attention if there is loss of concsiousness, trouble breathing, pain in chest, memory loss, blood loss whatsoever, vomiting, or a seizure. Also dizziness could be linked to chronic diseases such as labyrinthitis or heart problems but it could also be a minor headache symptom thus, take an over the counter antihistamine such as Dramamine or Ativert to deal with sleeping problems, dizziness or vertigo, ask BBPV for more info about vertigo and stop caffeine, alcohol and illegal drugs intake. If the dizziness persist, take a full blood test and talk to your doctor about your blood sugar, blood pressure and iron level.")

#COLD
    if there_is(["stuffy nose", "blocked nose", "full nose", "runny nose", "have a cold"]):
        medbot_speak("A stuffy nose is usually linked to a cold. In general, " + cold["explanation"] + cold["reasons"] + ". Normally " + cold["symptoms"] + " To deal with it, " + cold["meds"])
        more_cold = recordAudio("Would you like information about linked illnesses such as flu?")
        if yesz in more_cold:
            medbot_speak(flu["explanation"] + ". Symptoms may include a " + flu["symptoms"] + " . And to deal with them, " + flu["meds"])

        else:
            medbot_speak("Take extra care, and you can ask me about something else instead <3")

        medbot_speak(" Finally " + cold["emergency"])

#HYPOTHERMIA
    if there_is(["hypothermeia", "my feet are cold", "my body is cold", "feeling cold", "frostbite", "freezing"]):
        medbot_speak("Frost bite is the freezing of parts of your skin and tissues within. It is caused by being outside in a cold weather without properly dressing up to withstand the weather")
        medbot_speak(frostbite["causes"] +  ". " + frostbite["self_care"] + " " + frostbite["emergency"])
        hypothermia_y_or_n = recordAudio("Hypothermia is associated to frostbite in many instances, would you like to know more")
        if yesz in hypothermia_y_or_n:
            medbot_speak("Shivering will most likely be your body's initial reaction to a drop in body temperature, in order to heat up your body, this is called hypothermia")
            medbot_speak(hypothermia["signs"] + " SO try to" + hypothermia["self_care"] + ". Unlike frostbite, hypothermia may also occur in hot temperatures due to being in a sweaty, or wet place, or trapped in cold water.")
        





    if  ("stop" or "thank you") in data: 
        medbot_speak("Alright then, have a great day")
        exit()

    # if :
    #     medbot_speak("I apologize alothugh that is not a valid command")








#Actual action of speaking the audio as well as listening, should be kept last in all codes...
time.sleep(1)
medbot_speak("Hi it's medbot")
engine = pyttsx3.init()


while 1:
    data = recordAudio()
    response(data)