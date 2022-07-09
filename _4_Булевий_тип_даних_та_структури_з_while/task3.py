"""
The math quiz program.
Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong, and then responds with a message accordingly.
"""

math_example = '16/4*(3-1) = '
right_answer = 8.0
msg_for_question = 'Your answer choice: '
limit_of_attempts = 3
attempt = 0

print(f'Math example is:\n\t\t\t{math_example}')

print('Enter "q" to quit')
while attempt < limit_of_attempts:          # check limit of attempts
    get_answer = input(msg_for_question)
    attempt += 1
    if get_answer.lower() == "q":           # check wish to quit
        break
    elif float(get_answer) == right_answer:
        print(f'Well done! {get_answer} is right answer.')
        break
    else:
        if True:
            print(f'It isn\'t correct. However you have {limit_of_attempts - attempt} attempts more.\
                Try one more time.')
else:
    print('Sorry. You can try next time.')
