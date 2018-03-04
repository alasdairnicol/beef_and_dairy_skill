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
    response = app.response(text)
    response.end_session = False
    return response


@app.intent('AMAZON.StopIntent')
def handle_stop_intent(request, session):
    text = "Thanks for using the Beef and Dairy Network Alexa Skill. Beef Out!"
    return app.response(text)


@app.intent('FifthMeatIntent')
def handle_favourite_meat_intent(request, session):
    answers = [
        "There is no fifth meat",
        "I don't understand the question. There are only four meats.",
        "Please stop this dangerous talk about a fifth meat",
        """<speak>Never ask me <phoneme alphabet="ipa" ph="ðat">that</phoneme> again</speak>""",
        "What is wrong with you? There are four meats.",
    ]
    text = random.choice(answers)
    speech_type = 'SSML' if text.startswith('<speak>') else 'PlainText'
    return app.response(text, speech_type=speech_type)


@app.intent('SidOnionIntent')
def handle_sid_onion(request, session):
    text = "Sid Onion is still in jail in Turkey. Beeves without borders are working tirelessly to get him out of there."
    return app.response(text)


@app.intent('FavouriteBeefIntent')
def handle_favourite_beef_intent(request, session):
    answers = [
        "Hmm, good question. I'd have to say: a plate of rich beef sausages",
        "Rich beef sausages",
    ]
    text = random.choice(answers)
    return app.response(text)


@app.intent('CheeseAndOnionIntent')
def handle_cheese_and_onion_intent(request, session):
    text = """Cheese and Onion are Britain's foremost comedy double act, best known for their hit song, "She'd never had cheese and onion before"."""
    return app.response(text)


@app.intent('LambIntent')
def handle_lamb_intent(request, session):
    text = "Eat lamb today and I promise you, by the end of the month you'll be found dead in a pool of mint sauce"
    return app.response(text)


def get_person_key(request):
    """
    Get the normalised key from the slot. For example, this method will
    return "michael" if the user asks about "Michael Banyan" or "Michael"
    """
    try:
        person = request['intent']['slots']['person']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
    except KeyError:
        person = "notfound"
    return person


people = {
    'boffo': "Boffo is the owner of Boffo's cow circus, which is best known for the Bollywave, a part of the show where a cow is fired out of a cannon into a bath containing bolognese. The bolognese soaks the audience, who absolutely love it.",
    'eli': """<speak>Eli Roberts is a former slaughterhouse owner, theme park entrepreneur, and now religious cult leader. <amazon:effect name="whispered">He doesn't like me talking about him so I'm going to be quiet now.</amazon:effect></speak>""",
    'les': """<speak><phoneme alphabet="ipa" ph="les">Les</phoneme> Cheese was a member of Britain's foremost comedy double act Cheese and Onion</speak>""",
    'malcolm': "Malcolm is a bull who is worshipped by the members of the Church of Eli.",
    'michael': "Michael Banyan is the former bovine poet laureate who mysteriously disappeared. His best known work is his collection of poetry 'Crab Of The Land'.",
    'phillip': "Phillip Mushroom is one of Britain's best loved television actors. He is best known for his roles in 'Beef Justice', 'Bankside', and 'Bankside: The Movie'. He is famous for acting with his back to the camera.",
    'roy': "Roy Gluck Junior is the CEO of fast food restaurant, Burgers Barrel.",
    'david': """<speak>Dr David Pin is a researcher from the European Space Agency. He claims to have discovered <say-as interpret-as="expletive">evidence</say-as> of the so-called <say-as interpret-as="expletive">fifth</say-as> <say-as interpret-as="expletive">meat</say-as>, but he hasn't been seen since.</speak>""",
}


@app.intent('PersonIntent')
@app.slot('person')
def handle_person_intent(request, session, person):
    try:
        person_key = get_person_key(request)
        text = people[person_key]
    except KeyError:
        text = f"I'm sorry, I don't know about {person}"

    speech_type = 'SSML' if text.startswith('<speak>') else 'PlainText'
    return app.response(text, speech_type=speech_type)


@app.intent('WhereIsMichaelIntent')
def handle_where_is_michael_intent(request, session):
    text = "Michael Banyan is in a secret location. If his whereabouts was revealed, he would be in grave danger from the Bovine Farmers' Union who have already sewn a cow's face onto his face."
    return app.response(text)


@app.intent('HowManyMeatsIntent')
def handle_how_many_meats_intent(request, session):
    text = "There are four types of meat: Beef, pork, chicken, and lamb"
    return app.response(text)


@app.intent('BeefPluralIntent')
def handle_beef_plural_intent(request, session):
    text = "The plural of beef, is beeves"
    return app.response(text)


meats = {
    'beef': 'Beef is one of the four meats',
    'lamb': 'lamb is one of the four meats',
    'pork': 'pork is one of the four meats',
    'chicken': 'chicken is one of the four meats',
    'turkey': 'turkey is simply a robust chicken',
    'venison': 'venison is forest beef',
    'tuna': 'tuna is a type of fish, although some scientists believe that it can be categorized as a beef',
    'goat': 'goat is mountain lamb',
    'horse': 'horse is ride-on beef',
    'weasel': 'weasel is small long porkmeat',
    'sparrow': 'sparrow is mini chicken',
    'giraffe': 'giraffe is long necked savannah beef',
    'lizard': 'lizard is scaled pork',
    'peregrine falcon': 'all falcons are sleek speed chicken',
    'spider': 'eight legged micro beef',
    'snow leopard': 'snow leopard is himalayan fanged pork',
    'kangaroo': 'kangaroo is a type of antipodean pork meat',
    'fish': 'fish is fish',
    'rabbit': 'rabbit is hedgerow pork',
    'pheasant': 'pheasant is posh chicken',
    'quail': 'quail is weird chicken',
    'salmon': 'salmon is a type of fish, although some scientists believe that it can be categorized as chicken',
    'prawns': 'prawns are a type of fish, although some scientists believe that it can be categorized as a beef',
    'veal': 'veal is young male beef',
    'partridge': "partridge is God's chicken",
    'pigeon': 'pigeon is urban chicken',
    'duck': 'duck is floating chicken',
    'insects': 'insects are small gross porkmeats',
    'snails': 'snails are a type of beef',
    'seafood': 'seafood is fish',
    'reindeer': 'reindeer is tundra forest beef',
    'hedgehog': 'hedgehog is a type of hedgerow porkmeat and is a lovely tender meat',
    # FIXME missing meats
    # 'crab': 'crab is a type of ',
    # 'goose': 'goose is a type of ',
    # 'buffalo': 'buffalo is a type of ',
    # 'seal': 'seal is a type of ',
    # 'whale': 'whale is a type of ',
}


@app.intent('WhichMeatIntent')
@app.slot('meat')
def handle_which_meat_intent(request, session, meat):
    text = meats.get(meat)
    if not text:
        text = f"Hmm, I'm not sure which one of the four meats {meat} is."
    return app.response(text)


@app.intent('BanyanPoemIntent')
def handle_banyan_poem_intent(request, session):
    text = """
           Soft as a mother, smooth as a latte,
           a beefy oblong with the eyes of an angel,
           black as night and white as snow,
           you're like an edible domino,
           or a coat hanger whose burden isn't shirts but meat.
           Stand up.
           Raise a glass and give yourself a hand.
           You are, the crab of the land.
           """
    return app.response(text)
