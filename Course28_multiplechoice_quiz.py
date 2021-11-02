# modul ile python aynı klasördeyse otomatik kendisi geliyor
from question import Question

# soruları bir diziye yazdık
question_promts = [
    "What color are appless? \n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color are bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow \n\n",
    "What color are strawberries? \n(a) Yellow \n(b) Red \n(c) Blue \n\n"
]

# quesiton py dosyası yarattık (soru nesnesi için)
# içinde cevaplar ve sorular var


#cevaplarımızın ve sorularımın olduğu bir class dizisi yarattık
questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]


def run_test(questions):
    score = 0  #bildiği sorular için puan
    for question in questions: # objeler içindeki ker soru için
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")        


run_test(questions)