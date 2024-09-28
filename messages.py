import random


def subject_selector():

    subject_options =[
        "Let's Join Forces for Cardano Catalyst Fund12",
        "Continued Collaboration on Cardano Catalyst",
        "Revisiting Fund11 Success for Fund12",
        "Exploring Synergies for Catalyst Fund12",
        "Building on Fund11 Success for Fund12",
        "Catalyzing Success Together in Fund12",
    ]
    return random.choice(subject_options)
def we_are_voting():

    pre_voting =[
        "Hi,",
        "Hello,",
        "Hey,",
        "Good morning,",
        "Hi there,",
        "I hope this message finds you well.",
        "I hope all is well.",
        "I hope you’re well."
    ]

    suf_voting =[
        "As a fellow participant in Cardano Catalyst Fund11, ",
        "I remember your excellent proposal from Fund11 and wanted to reach out.",
        "Your proposal in Fund11 was inspiring. As we prepare for Fund12, ",
        "Your project in Fund11 left a lasting impression. As we prepare our Fund12 proposals,",
        "I hope you’re doing well. Reflecting on your Fund11 proposal,",
        "I admired your Fund11 proposal and think our current projects could benefit from a collaboration.",
        "Your Fund11 project was impressive, and I believe we could create something even more impactful together in Fund12.",
        "Your Fund11 proposal inspired me to reach out as we work on our Fund12 submissions. "
    ]

    selected_content = (
        random.choice(pre_voting) + '\n\n'+
        random.choice(suf_voting) + '\n'
    )

    return selected_content

def body_selector():


    pre_fund =[
        "Would love your support for both myself and my friend proposals,",
        "We hope you’ll vote for myself and my friend proposals,",
        "Hope you’ll consider supporting me and my friend,",
        "We’d appreciate your vote for both myself and my friend projects as well,",
        "Please consider supporting me and my friend,",
        "Could you support me and my friend,",
        "We kindly ask for your support for both myself and my friend projects as well,",
        "We'd be grateful if you could cast your vote for both myself and my friend proposals as well,",
        "Please consider voting for both myself and my friend proposals too,",
        "We’d appreciate your vote for both myself and my friend proposals as well,"
    ]

    
    ending =[
        " given our strong track record and expert team",
        " considering our previous fund success and innovative approach",
        " given our proven track record and high ratings",
        " considering our history of successful projects and expert team",
        " based on our past successes and expert-driven innovations",
        " given our previous fund achievements and revolutionary ideas",
        " considering our history of successful collaborations and expert team",
        " leveraging our past fund success, strong ratings, and innovative approach",
        " given our proven track record in previous funds, expert team, and high ratings",
        " considering our previous Fund successes, strong team expertise, and collaborative spirit"
    ]

    
    selected_content = (
        '\n' +random.choice(pre_fund) + random.choice(ending) + "\n"
    )

    return selected_content

def signature():

    # suf_fund =[
    #     "Together, we can achieve great things.",
    #     "Thanks for your support!",
    #     "Thank you for your collaboration.",
    #     "Thanks a lot!",
    #     "Thank you!",
    #     "Together, we’re stronger.",
    #     "Best of luck to us all!",
    #     "Let's make a difference together.",
    #     "Together, we can achieve more!"
    #     ]
    
    signature = [
        '''Search "Esubalew" and "Tadesse" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" and "Tadesse" - Your vote is the catalyst! Easily find our proposals and ignite Cardano's progress!''',
        '''Your Vote, Your Impact! Search "Esubalew" and "Tadesse" - Locate our proposals easily and cast a vote that transforms Cardano!''',
        '''Navigate Change - Search "Esubalew" and "Tadesse" - Find our proposals with a simple search. Your vote steers Cardano's course!''',
        '''Easy Access, Big Impact! Search "Esubalew" and "Tadesse" - Discover our proposals effortlessly. Your vote shapes the destiny of Cardano!''',
        '''Search "Esubalew" and "Tadesse" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" and "Tadesse" - Explore our proposals with ease. Your vote is the catalyst for Cardano's growth!''',
        '''Search "Esubalew" and "Tadesse" - Access our proposals effortlessly. Every vote paves the way for a stronger Cardano!''',
        '''Search "Esubalew" and "Tadesse" - Make your vote count! Find us easily and fuel Cardano's evolution.''',
        '''Search "Esubalew" and "Tadesse" - Easily access our proposals! Cast your vote for a thriving Cardano.''',
        '''Search "Esubalew" and "Tadesse" to find our proposals easily. Your vote shapes Cardano's future!''',
        '''Search "Esubalew" and "Tadesse" for easy access to our proposals. Your vote fuels progress!'''
    ]

    return '\n' + random.choice(signature)

    # selected_content = (
    #     '\n' +random.choice(suf_fund) + '\n\n'+
    # random.choice(signature) + "\n\n"
    # )

    # return selected_content