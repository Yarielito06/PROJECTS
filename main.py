class Suspect: 
    def __init__(self, name,age, alibi, evidence):
        self.name = name 
        self.alibi = alibi
        self.age = age
        self.evidence = evidence

    def introduction(self):
        print('My name is ', self.name)
        print('My age is', self.age)
        print('My alibi:', self.alibi)
        print('evidence: ',self.evidence )
    def analyse_evidence(self):
        total_score = 0
        for score in self.evidence.values():
            total_score += score
        if total_score >= 10:
            return 'Strong evidence'
        else:
            return 'Not enough evidence'

alex = Suspect(
    "Alex", 32, "I was at home",
    {"camera": 5, "message": 2, "login": 4}
)

sam = Suspect(
    "Sam", 25, "I was at work",
    {"camera": 1, "message": 2, "login": 3}
)

taylor = Suspect(
    "Taylor", 27, "I was at the library",
    {"camera": 3, "message": 5, "login": 4}
)

suspects = [alex,sam,taylor]

playing = True 
case_story = """
A confidential document disappeared at 2:14 AM.
Three employees had access to the building.
Your task is to investigate what happened.
"""
culprit = 'Taylor'


while playing:
    print("\nCASEFILE — Main Menu")
    print("1. View suspects")
    print("2. Investigate a suspect")
    print("3. Read case information")
    print("4. Accuse a suspect")
    print("5. Exit game")

    choice = input("Choose an option: ")

    if choice == '1':
        for suspect in suspects:
            print(suspect.name)
    elif choice == '2':
        print('Starting Investigation')
        found = False
        player = input('Choose a suspect:').strip().title()
        for suspect in suspects:
            if player == suspect.name:
                found = True
                print(suspect.name, ':', suspect.analyse_evidence())
                break
        if not found:
            print('uknown player')

    elif choice == '3':
        print(case_story)
    elif choice == '4':
        accusation = input('Who do you accuse?:').strip().title()
        print(accusation)
        if accusation == culprit:
            print('Correct! Case solved!')
            playing = False
        else:
            print('Incorrect try again!!')
        
    elif choice == '5':
        print("Thanks for playing CASEFILE!")
        playing = False
    else:
        print('Invalid option')

