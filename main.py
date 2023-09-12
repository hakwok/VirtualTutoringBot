import re
import long_responses as long


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
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

    # Response-----------------------------------------------
    # You can add more responses here, make sure to add keywords and required words if necessary
    response('Hello! ', ['hello', 'hi', 'hey'], single_response=True)
    response('You can find the student sign up page by clicking the students tab on the top right. The sign up form '
             'is at the bottom of the page. I hope this helps!', ['help', 'student', 'sign up', 'singup', 'form'])
    response('You can find the tutor sign up page by clicking the tutor tab on the top right. The sign up form '
             'is at the bottom of the page. I hope this helps!', ['help', 'tutor', 'sign up', 'singup', 'form'],
             required_words=['tutor'])
    response('You can contact us at virtualtutoringsf@gmail.com. I hope this helps!',
             ['contact', 'admin', 'administration', 'help', 'email'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


print('Hi! I am the VirtualTutoringSF bot. Would you like help with signing up as a student, tutor, or contacting '
      'administration?')
while True:
    print('Bot: ' + get_response(input('You: ')))
