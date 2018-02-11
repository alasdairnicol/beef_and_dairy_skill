"""
Beef and Dairy Network Unofficial Skill
"""
import os
import random

from echokit import EchoKit

skill_id = os.getenv("SKILL_ID")

app = EchoKit(skill_id)
handler = app.handler


@app.launch
def launch(request, session):
    welcome_text = """\
    Hello and welcome to the Beef and Dairy Network Alexa Skill,
    the number one skill for those involved, or just interested,
    in the production of beef animals and dairy herds."
    """
    response = app.response(welcome_text)
    response.reprompt("You can ask me a question like 'how many meats are there', or, 'where is Sid Onion'")
    response.end_session = False
    return response


@app.session_ended
def session_ended(request, session):
    text = "Thanks for using the Beef and Dairy Network Alexa Skill. Beef Out!"
    return app.response(text)


@app.intent('AMAZON.CancelIntent')
def handle_cancel_intent(request, session):
    text = "Thanks for using the Beef and Dairy Network Alexa Skill. Beef Out!"
    return app.response(text)


@app.intent('AMAZON.HelpIntent')
def handle_help_intent(request, session):
    text = "You can ask me, 'what is your favourite beef dish', or, 'How many meats are there'"
    return app.response(text)


@app.intent('AMAZON.StopIntent')
def handle_stop_intent(request, session):
    text = "Thanks for using the Beef and Dairy Network Alexa Skill. Beef Out!"
    return app.response(text)


@app.intent('FifthMeatIntent')
def handle_favourite_meat_intent(request, session):
    answers = [
        "There is no fifth meat",
        "Please stop this dangerous talk about a fifth meat",
        "Never ask me that again",
        "What is wrong with you? There are four meats.",
    ]
    text = random.choice(answers)
    return app.response(text)


@app.intent('SidOnionIntent')
def handle_sid_onion(request, session):
    text = "Sid Onion is still in jail in Turkey. Beeves without borders are working tirelessly to get him out of there."
    return app.response(text)


@app.intent('FavouriteBeefIntent')
def handle_favourite_beef_intent(request, session):
    text = "Hmm, good question. I'd have to say: a plate of rich beef sausages"
    return app.response(text)


@app.intent('HowManyMeatsIntent')
def handle_how_many_meats_intent(request, session):
    text = "There are four types of meat: Beef, pork, chicken, and lamb"
    return app.response(text)


@app.intent('BeefPluralIntent')
def handle_beef_plural_intent(request, session):
    text = "The plural of beef, is beeves"
    return app.response(text)


@app.intent('WhichMeatIntent')
@app.slot('meat')
def handle_which_meat_intent(request, session, meat):
    meats = {
        'beef': 'Beef is one of the four meats',
        'lamb': 'lamb is one of the four meats',
        'pork': 'pork is one of the four meats',
        'chicken': 'chicken is one of the four meats',
        'turkey': 'turkey is simply a large christmas chicken',
        'venison': 'venison is forest beef',
        'tuna': 'tuna is aquatic chicken',
        'goat': 'goat is mountain lamb',
    }
    text = meats.get(meat)
    if not text:
        text = f"Hmm, I'm not sure which one of the four meats {meat} is."
    return app.response(text)
