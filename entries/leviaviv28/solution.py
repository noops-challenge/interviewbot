# Interactive python client for fizzbot

import json
import urllib.request
import urllib.error
import roman
from sympy.ntheory import factorint

domain = 'https://api.noopschallenge.com'

def print_sep(): print('----------------------------------------------------------------------')

# print server response
def print_response(dict):
    print('')
    print('message:')
    print(dict.get('message'))
    print('')
    for key in dict:
        if key != 'message':
            print('%s: %s' % (key, json.dumps(dict.get(key))))
    print('')

# try an answer and see what fizzbot thinks of it
def try_answer(question_url, answer, respType):
    print_sep()
    body = json.dumps({ respType: answer })
    print('*** POST %s %s' % (question_url, body))
    try:
        req = urllib.request.Request(domain + question_url, data=body.encode('utf8'), headers={'Content-Type': 'application/json'})
        res = urllib.request.urlopen(req)
        response = json.load(res)
        print_response(response)
        print_sep()
        return response

    except urllib.error.HTTPError as e:
        response = json.load(e)
        print_response(response)
        return response

# keep trying answers until a correct one is given
def get_correct_answer(question_url, question_data):
    while True:
        answer = ""
        respType = 'answer'
        if 'exampleResponse' in question_data and 'login' in question_data['exampleResponse']:
            answer = 'leviaviv28'
            respType = 'login'
        else:
            if 'prime' in question_data['message']:
                answer = [*factorint(int(question_data['question']))]
            elif 'convert' in question_data['message']:
                answer = roman.fromRoman(question_data['question'])
            elif 'compute' in question_data['message']:
                answer = string_equation(question_data['question'])

        response = try_answer(question_url, answer, respType)

        return response.get('nextQuestion')

# do the next question
def do_question(domain, question_url):
    print_sep()
    print('*** GET %s' % question_url)

    request = urllib.request.urlopen( ('%s%s' % (domain, question_url)) )
    question_data = json.load(request)
    print_response(question_data)
    print_sep()

    next_question = question_data.get('nextQuestion')

    if next_question: return next_question
    return get_correct_answer(question_url, question_data)

def string_equation(equation):
    num_dict = {
        "zero":'0', "one":'1', "two":'2', "three":'3',"four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8',
        "nine":'9', "ten":'10', "eleven":'11', "twelve":'12', "thirteen":'13', "fourteen":'14', "fifteen":'15',
        "sixteen":'16', "seventeen":'17', "eighteen":'18', "nineteen":'19', "twenty":'20', "thirty":'30', "forty":'40',
        "fifty":'50', "sixty":'60', "seventy":'70', "eighty":'80', "ninety":'90', 'minus':'-', 'plus':'+', 'times':'*', 'divided': '/'}
    digit_str = ""
    equation = equation.replace(' by', '')
    for word in equation.split(' '):
        if '-' in word and len(word) > 1:
            for subword in word.split('-'):
                digit_str += num_dict[subword].replace('0', '')
        else:
            digit_str += num_dict[word]
        digit_str += " "
    return eval(digit_str)


def main():
    question_url = '/interviewbot/start'
    while question_url:
        question_url = do_question(domain, question_url)

if __name__ == '__main__': main()
