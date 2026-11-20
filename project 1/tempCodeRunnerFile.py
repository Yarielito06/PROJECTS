
suspects = {
    "Alex": {"camera": 5, "message": 2, "login": 4},
    "Sam": {"camera": 1, "message": 2, "login": 3},
    "Jordan": {"camera": 4, "message": 4, "login": 3},
    "Taylor":{"camera": 3, "message": 5, "login": 4}
}

def analyse_evidence(evidence):
    total_score = 0

    for score in evidence.values():
        total_score += score

    if total_score >= 10:
        return "strong evidence"
    else:
        return "Not enough evidence"


#for name, evidence in suspects.items():
#    result = analyse_evidence(evidence)
#    print(name, ":", result)
# more readable verison , result = analyse_evidence(suspects[chosen_name])



keep_investigating = True

while keep_investigating:

    chosen_name = input("Choose a suspect: ").strip().title()

    if chosen_name in suspects:
        print('suspects found')
        print(chosen_name + ': ' + analyse_evidence(suspects[chosen_name]))
    else:
        print('Unknown suspect')

    answer = input("Keep playing? Yes/No: ").strip().lower()

    if answer == "no":
        keep_investigating = False

print("Game over!")
