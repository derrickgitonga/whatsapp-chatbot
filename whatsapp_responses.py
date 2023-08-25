import re
import long_responses as long
import random_gift as ran

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calculates percentage of recognised words
    percentage = float(message_certainty) / float(len(recognised_words))

    for words in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # response-------------------------------------------------------------------------
    response('hello', ['hello', 'hi', 'hey', 'sup', 'heyy'], single_response=True)
    response('I can not answer religious questions', ['believe', 'in', 'god', 'church', 'allah'],required_words=['believe', 'allah'])
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('okay nice talking to you', ['good night', 'bye', 'shutdown'],
             required_words=['good night', 'bye', 'shutdown'])
    response('Thank you', ['i', 'love', 'code', 'Palace', 'you'], required_words=['code', 'palace', 'love'])
    response('nice to meet you', ['am', 'name', 'can lled', 'i'], required_words=['am', 'i'])
    response('if i were you, I would look that on the internet', ['weather', 'what', 'play', 'who'],
             required_words=['weather', 'play'])
    response('I was created on 10/07/2022, by Moses', ['who', 'created', 'you', 'made'], required_words=['made'])
    response('I am resily_bot', ['who', 'are', 'you'], required_words=['are'])
    response('I am a robot, and am not sentient. maybe one day i will be',
             ['are', 'you', 'feelings', 'have', 'feel', 'sentient'], required_words=['feelings', 'feel', 'you'])
    response('hi mom', ['i', 'miriam'], required_words=['miriam'])
    response('i can answer the questions you have, example ask me what is the weather', ['what', 'can', 'you', 'do'],
             required_words=['do', 'what'])
    response('hello welcome to res_betting. choose a random number from one to five. start with g/. example g/four',
             ['bet'], required_words=['can'])
    response(ran.gifter(), ['g/four', 'g/one', 'g/two', 'g/three', 'g/five'], required_words=['g/four', 'g/one', 'g/two', 'g/three', 'g/five'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 0.5 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
