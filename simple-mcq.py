from Question import Question

question_prompts = [
    "What colors are apples?\n (a)Red \n (b)Green \n (c)Yellow \n (d)Purple\n",
    "What colors are berries?\n (a)Red \n (b)Green \n (c)Yellow \n (d)Purple\n",
    "What colors are bananas?\n (a)Red \n (b)Green \n (c)Yellow \n (d)Purple\n",
    "What colors are pineapples?\n (a)Red \n (b)Green \n (c)Yellow \n (d)Purple\n"

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1 

    print(f"You got {score}/{len(questions)} correct")


run_test(questions)
