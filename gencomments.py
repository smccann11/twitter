import random

def generate_comment_0():
    adjs = ['good', 'great', 'amazing', 'impactful', 'better']
    adj = random.choice(adjs)
    experts = ['scientists', 'experts', 'social workers', 'smart people', 'people like Fauci']
    expert = random.choice(experts)
    factss = ['facts', 'the truth', 'information', 'real science']
    facts = random.choice(factss)
    aspects = ['certain aspects of life', 'science', 'the unkown', 'some phenomena']
    aspect = random.choice(aspects)

    text = "Joe Biden will be a " + adj + " president becasue he will listen to " + expert + " and implement policy based on " + facts + " not feeling. " + expert + " know best, as they have devoted their lives to advancing knowledge of " + aspect + "."
    return text


def generate_comment_1():
    advs = ['fight', 'advocate', 'push', 'champion']
    adv = random.choice(advs)
    adjs = ['kind', 'good', 'sympathetic', 'smart', 'knowledgable']
    adj = random.choice(adjs)
    rights = ['fighting racism', 'income equality', 'the right to an abortion', 'healthcare']
    right = random.choice(rights)
    goods = ['good', 'betterment', 'best', 'future']
    good = random.choice(goods)
    peoples = ['americans', 'the people', 'citizens', 'us']
    people = random.choice(peoples)

    text = "Biden and Harris will " + adv + " for the natural human rights of all people. Any " + adj + " candidate would. An example of a natural human right would be " + right + ". Voting for Biden would be voting for the " + good + " of " + people + "."
    return text


def generate_comment_2():
    works = ['work', 'policy', 'ideas', 'achievements']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    fights = ['fought', 'advocated', 'helped', 'improved lives']
    fight = random.choice(fights)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    others = ['americans', 'the people', 'citizens', 'everyone']
    other = random.choice(others)

    text = "Joe Biden's " + work + " under the Obama administration " + show + " his passion for the American people. Biden was a major part in revamping the auto industry, and " + fight + " for people. " + person + " vote for Biden is a vote for " + other + "."
    return text


def generate_comment_3():
    works = ['work', 'policy', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    fights = ['fought', 'advocated', 'helped', 'improved lives']
    fight = random.choice(fights)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    others = ['profanity', 'hate', 'racism', 'ignorance']
    other = random.choice(others)

    text = "Donald Trump's " + work + " under his administration " + show + " his ignorance for the American people. Trump ignored the severity of COVID-19, and never " + fight + " for american people. " + person + " vote for Trump is a vote for " + other + "."
    return text


def generate_comment_4():
    works = ['work', 'policy', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    eves = ['evident', 'seen in fact', 'there', 'all throught his actions and words']
    eve = random.choice(eves)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    values = ['values', 'ideas', 'thoughts', 'actions']
    value = random.choice(values)

    text = "If you believe the " + work + " of Doanald Trump under his administration " + show + " the best of the American people, re-examine your thoughts. His ignorance for the American people, although maybe not obvious is" + eve + ". Trump ignored the severity of COVID-19. " + person + " vote should align with your best" + value + "."
    return text


def generate_comment_5():
    works = ['words', 'tweets', 'ideas', 'actions']
    work = random.choice(works)
    shows = ['shows', 'exemplifies', 'points to', 'brings light to']
    show = random.choice(shows)
    eves = ['evident', 'seen', 'obvious', 'shown all throught his actions and words']
    eve = random.choice(eves)
    persons = ['Your', 'Everyones', 'His or her', 'Our']
    person = random.choice(persons)
    values = ['health', 'safety', 'equality', 'hope']
    value = random.choice(values)

    text = "Trump's " + work + " " + show + " the person he is. An ignorant, selfish, and stobborn man without sufficient knowledge or skills to be a president. It is " + eve + " that Trump does not care about the average person, but rather himself and his reputaiton. " + person + " vote could end this era, and begin one full of " + value + "."
    return text

def generate_comment():
    for i in range(20):
        options = [0, 1, 2, 3, 4, 5]
        choice = random.choice(options)
        if choice == 0:
            return generate_comment_0()
        elif choice == 1:
            return generate_comment_1()
        elif choice == 2:
            return generate_comment_2()
        elif choice == 3:
            return generate_comment_3()
        elif choice == 4:
            return generate_comment_4()
        elif choice == 5:
            return generate_comment_5()

print(generate_comment())