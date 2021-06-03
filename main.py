from collections import defaultdict

# user, question, answer
user_answers = {
    1: [
        (1, 1),
        (2, 1),
        (3, 1),
    ],

    2: [
        (1, 2),
        (2, 2),
        (3, 2),
    ],

    3: [
        (1, 1),
        (2, 2),
        (3, 1),
    ],
}

expected_outcome = {
    1: {
        1: 0,  # always 0 as same person
        2: 0,  # no matching answers
        3: 2,  # 2 matching answers
    },

    2: {
        1: 0,
        2: 0,  # always 0 as same person
        3: 1,  # 1 matching answer
    },

    3: {
        1: 2,
        2: 1,
        3: 0,  # always 0 as same person
    },
}

def get_scores():
    scores = defaultdict(dict)
    for user1, answers1 in user_answers.items():
        for user2, answers2 in user_answers.items():
            score = 0
            if user1 != user2:
                for answer1, val1 in answers1:
                    for answer2, val2 in answers2:
                        if answer1 == answer2 and val1 == val2:
                            score += 1
            scores[user1][user2] = score
    return scores


scores = get_scores()
assert scores == expected_outcome
