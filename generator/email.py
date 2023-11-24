from random import choice

def generator():
    domains = [
        'gmail.com', 'naver.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
        'icloud.com', 'aol.com', 'protonmail.com', 'yandex.com', 'zoho.com'
    ]
    usernames = [
        'user123', 'john_doe', 'jane_smith', 'cool_guy', 'webmaster',
        'coding_ninja', 'happy_user', 'best_buddy', 'email_user', 'newbie',
        'python_lover', 'programmer', 'tech_enthusiast', 'hello_world', 'gamer123',
        'coffee_addict', 'bookworm', 'nature_lover', 'music_fan', 'foodie',
        'traveler', 'fitness_guru', 'art_lover', 'movie_buff', 'adventurer',
        'dog_lover', 'cat_person', 'beach_comber', 'mountain_hiker', 'skiing_pro',
        'yoga_master', 'soccer_fan', 'basketball_junkie', 'tennis_player', 'golf_pro',
        'fashionista', 'shopaholic', 'frugal_shopper', 'vegan_life', 'tech_geek',
        'gadget_guru', 'science_buff', 'math_wiz', 'space_enthusiast', 'history_buff',
        'baker', 'chef_extraordinaire', 'food_critic', 'vlogger', 'podcaster',
        'hiking_guru', 'fitness_model', 'cycling_enthusiast', 'wine_connoisseur',
        'beer_lover', 'whiskey_aficionado', 'cocktail_expert', 'DIY_enthusiast',
        'gardener', 'interior_designer', 'artist', 'photographer', 'freelancer',
        'book_author', 'book_publisher', 'movie_director', 'actor_actress',
        'rock_climber', 'scuba_diver', 'surfer', 'sailor', 'pilot', 'teacher',
        'professor', 'student', 'lawyer', 'doctor', 'nurse', 'engineer', 'architect',
        'accountant', 'financial_analyst', 'marketing_guru', 'sales_pro',
        'entrepreneur', 'startup_founder', 'CEOspeaker', 'boss', 'manager', 'leader',
        'problem_solver', 'innovator', 'dreamer', 'thinker', 'explorer', 'adventurer',
        'world_traveler', 'wanderer', 'backpacker', 'nomad', 'remote_worker',
        'web_developer', 'app_developer', 'data_scientist', 'AI_enthusiast',
        'blockchain_expert', 'cyber_security', 'ethical_hacker', 'gaming_streamer',
    ]
    
    while True:
        yield f"{choice(usernames)}@{choice(domains)}"