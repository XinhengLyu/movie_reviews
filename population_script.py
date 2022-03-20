
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_reviews.settings')
import django
django.setup()

from rango.models import UserProfile, Movie, Movie_review, User

def populate():

    movies = [

    {'movie_name': 'sundown',
     'movie_information': 'Neil and Alice Bennett (Tim Roth, Charlotte Gainsbourg) are the core of a wealthy family on vacation in Mexico with younger members Colin and Alexa (Samuel Bottomley, Albertine Kotting McMillan) until a distant emergency cuts their trip short. When one relative disrupts the family\'s tight-knit order, simmering tensions rise to the fore in this suspenseful jolt from writer/director Michel Franco.',
     'release_date': '2021-09-05',
     'movie_image': 'Movie_images/movie_image1.png',
     'trailer_link': 'https://www.youtube.com/watch?v=dte6YUfWwHw', },

    {'movie_name': 'Dog',
     'movie_information': 'DOG is a buddy comedy that follows the misadventures of two former Army Rangers paired against their will on the road trip of a lifetime. Army Ranger Briggs (Channing Tatum) and Lulu (a Belgian Malinois dog) buckle into a 1984 Ford Bronco and race down the Pacific Coast in hopes of making it to a fellow soldier\'s funeral on time. Along the way, they\'ll drive each other completely crazy, break a small handful of laws, narrowly evade death, and learn to let down their guards in order to have a fighting chance of finding happiness.',
     'release_date': '2022-02-18',
     'movie_image': 'Movie_images/movie_image2.png',
     'trailer_link': 'https://www.youtube.com/watch?v=V4tAtp-TyzQ', },

    {'movie_name': 'SCREAM',
     'movie_information': 'Twenty-five years after a streak of brutal murders shocked the quiet town of Woodsboro, Calif., a new killer dons the Ghostface mask and begins targeting a group of teenagers to resurrect secrets from the town\'s deadly past.',
     'release_date': '2022-01-14',
     'movie_image': 'Movie_images/movie_image3.png',
     'trailer_link': 'https://www.youtube.com/watch?v=beToTslH17s', },

    {'movie_name': 'MINAMATA',
        'movie_information': 'Inspired by a true story, Minamata stars Johnny Depp playing celebrated photojournalist Eugene Smith. The film takes place in 1971 when we find Smith as a recluse and disconnected from the world he once shot. After receiving one final assignment from Life Magazine editor Robert Hayes (Bill Nighy), Eugene must travel to the Japanese coastal city of Minamata, which has been ravaged by mercury poisoning. Ushered by an impassioned Japanese translator, Aileen (Minami) and encouraged by local villagers (Hiroyuki Sanada), Eugene\'s powerful images expose decades of gross negligence by the country\'s Chisso Corporation.',
        'release_date': '2021-04-22',
        'movie_image': 'Movie_images/movie_image4.png',
        'trailer_link': 'https://www.youtube.com/watch?v=WP3pKTssw_E', },

    {'movie_name': 'FRESH',
     'movie_information': 'FRESH follows Noa (Daisy Edgar-Jones), who meets the alluring Steve (Sebastian Stan) at a grocery store and -- given her frustration with dating apps -- takes a chance and gives him her number. After their first date, Noa is smitten and accepts Steve\'s invitation to a romantic weekend getaway. Only to find that her new paramour has been hiding some unusual appetites.',
     'release_date': '2022-01-20',
     'movie_image': 'Movie_images/movie_image5.png',
     'trailer_link': 'https://www.youtube.com/watch?v=wKk5VAK1GZQ', },

    {'movie_name': 'CYRANO',
     'movie_information': 'Award-winning director Joe Wright envelops moviegoers in a symphony of emotions with music, romance, and beauty in Cyrano, re-imagining the timeless tale of a heartbreaking love triangle. A man ahead of his time, Cyrano de Bergerac (played by Peter Dinklage) dazzles whether with ferocious wordplay at a verbal joust or with brilliant swordplay in a duel. But, convinced that his appearance renders him unworthy of the love of a devoted friend, the luminous Roxanne (Haley Bennett), Cyrano has yet to declare his feelings for her -- and Roxanne has fallen in love, at first sight, with Christian (Kelvin Harrison, Jr.).',
     'release_date': '2021-09-02',
     'movie_image': 'Movie_images/movie_image6.png',
     'trailer_link': 'https://www.youtube.com/watch?v=fOInHcgmKus', },

    {'movie_name': 'THE BATMAN',
     'movie_information': 'Batman ventures into Gotham City\'s underworld when a sadistic killer leaves behind a trail of cryptic clues. As the evidence begins to lead closer to home and the scale of the perpetrator\'s plans become clear, he must forge new relationships, unmask the culprit and bring justice to the abuse of power and corruption that has long plagued the metropolis.',
     'release_date': '2022-03-18',
     'movie_image': 'Movie_images/movie_image7.png',
     'trailer_link': 'https://www.youtube.com/watch?v=mqqft2x_Aa4', },

    {'movie_name': 'HERE BEFORE',
     'movie_information': 'When a new family moves in next door to Laura and her family, their young daughter, Megan, quickly captivates her, stirring up painful memories of her own daughter, Josie, who died several years previously.',
     'release_date': '2021-03-17',
     'movie_image': 'Movie_images/movie_image8.png',
     'trailer_link': 'https://www.youtube.com/watch?v=6bqtZcvfuws', },

    {'movie_name': 'I WANT YOU BACK',
     'movie_information': 'Peter (Charlie Day) and Emma (Jenny Slate) are total strangers, but when they meet, one thing instantly bonds them: they were both unexpectedly dumped by their respective partners, Anne (Gina Rodriguez) and Noah (Scott Eastwood), on the same weekend. As the saying goes, "misery loves company," but their commiseration turns into a mission when they see on social media that their exes have happily moved on to new romances, Anne with Logan (Manny Jacinto) and Noah with Ginny (Clark Backo). Terrified that, in their 30s, they have lost their shot at happily ever after and horrified at the prospect of having to start over, Peter and Emma hatch a desperate plot to win the loves of their lives back. Each will do whatever it takes to put an end to their exes\' new relationships and send them running back to their arms.',
     'release_date': '2022-02-11',
     'movie_image': 'Movie_images/movie_image9.png',
     'trailer_link': 'https://www.youtube.com/watch?v=AJ_Zry9KLb8', },

    {'movie_name': 'BELLE',
     'movie_information': 'Suzu is a shy, everyday high school student living in a rural village. For years, she has only been a shadow of herself. But when she enters "U", a massive virtual world, she escapes into her online persona as Belle, a gorgeous and globally-beloved singer. One day, her concert is interrupted by a monstrous creature chased by vigilantes. As their hunt escalates, Suzu embarks on an emotional and epic quest to uncover the identity of this mysterious "beast" and to discover her true self in a world where you can be anyone.',
     'release_date': '2021-07-15',
     'movie_image': 'Movie_images/movie_image10.png',
     'trailer_link': 'https://www.youtube.com/watch?v=izIycj3j4Ow', },
     
    {'movie_name': 'BLACKWIDOW',
     'movie_information': 'Natasha Romanoff, aka Black Widow, confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises. Pursued by a force that will stop at nothing to bring her down, Natasha must deal with her history as a spy, and the broken relationships left in her wake long before she became an Avenger.',
     'release_date': '2021-07-07',
     'movie_image': 'Movie_images/movie_image11.png',
     'trailer_link': 'https://www.youtube.com/watch?v=ybji16u608U', },

    {'movie_name': 'TURNING RED',
     'movie_information': 'In "Turning Red", Mei Lee is a confident, dorky thirteen-year-old torn between staying her mother\'s dutiful daughter and the chaos of adolescence. And as if changes to her interests, relationships, and body weren\'t enough, whenever she gets too excited (which for a teenager is practically ALWAYS), she "poofs" into a giant red panda!',
     'release_date': '2022-03-11',
     'movie_image': 'Movie_images/movie_image12.png',
     'trailer_link': 'https://www.youtube.com/watch?v=XdKzUbAiswE', },

    {'movie_name': 'LINGUI, THE SACRED BONDS',
     'movie_information': 'On the outskirts of N\'Djamena in Chad, Amina lives alone with her only 15-year-old daughter Maria. Her already fragile world collapses the day she discovers that her daughter is pregnant. The teenager does not want this pregnancy. In a country where abortion is not only condemned by religion, but also by law, Amina finds herself facing a battle that seems lost in advance...',
     'release_date': '2021-07-08',
     'movie_image': 'Movie_images/movie_image13.png',
     'trailer_link': 'https://www.youtube.com/watch?v=2DFew16WifY', },
     
    {'movie_name': 'COME FROM AWAY',
     'movie_information': '"Come From Away" is the filmed version of the award-winning Broadway musical which tells the story of 7,000 people stranded in the small town of Gander, Newfoundland after all flights into the US are grounded on September 11, 2001. As the people of Newfoundland graciously welcome the "come from aways" into their community in the aftermath, the passengers and locals alike process what\'s happened while finding love, laughter and new hope in the unlikely and lasting bonds that they forge.',
     'release_date': '2022-03-11',
     'movie_image': 'Movie_images/movie_image14.png',
     'trailer_link': 'https://www.youtube.com/watch?v=Af77C4zUkjs', },

    {'movie_name': 'WHO WE ARE: A CHRONICLE OF RACISM IN AMERICA',
     'movie_information': 'Interweaving lecture, personal anecdotes, interviews, and shocking revelations, in WHO WE ARE: A Chronicle of Racism in America, criminal defense/civil rights lawyer Jeffery Robinson draws a stark timeline of anti-Black racism in the United States, from slavery to the modern myth of a post-racial America.',
     'release_date': '2022-01-14',
     'movie_image': 'Movie_images/movie_image15.png',
     'trailer_link': 'https://www.youtube.com/watch?v=IGsGRSgZbXY', },

    {'movie_name': 'POLY STYRENE: I AM A CLICHÉ',
     'movie_information': 'Poly Styrene was the first woman of color in the UK to front a successful rock band. She introduced the world to a new sound of rebellion, using her unconventional voice to sing about identity, consumerism, postmodernism, and everything she saw unfolding in late 1970s Britain, with a rare prescience. As the frontwoman of X-Ray Spex, the Anglo-Somali punk musician was also a key inspiration for the riot grrrl and Afropunk movements. But the late punk maverick didn\'t just leave behind an immense cultural footprint. She was survived by a daughter, Celeste Bell, who became the unwitting guardian of her mother\'s legacy and her mother\'s demons. Misogyny, racism, and mental illness plagued Poly\'s life, while their lasting trauma scarred Celeste\'s childhood and the pair\'s relationship. Featuring unseen archive material and rare diary entries narrated by Oscar-nominee Ruth Negga, this documentary follows Celeste as she examines her mother\'s unopened artistic archive and traverses three continents to better understand Poly the icon and Poly the mother.',
     'release_date': '2021-02-27',
     'movie_image': 'Movie_images/movie_image16.png',
     'trailer_link': 'https://www.youtube.com/watch?v=stXSFuUOdeU', },

    {'movie_name': 'WRITING WITH FIRE',
     'movie_information': 'In a cluttered news landscape dominated by men emerges India\'s only newspaper run by Dalit women. Chief reporter Meera and her journalists break traditions, redefining what it means to be powerful.',
     'release_date': '2021-01-30',
     'movie_image': 'Movie_images/movie_image17.png',
     'trailer_link': 'https://www.youtube.com/watch?v=nzyWNOkKnJg', },

    {'movie_name': 'DUNE',
     'movie_information': 'Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet\'s exclusive supply of the most precious resource in existence, only those who can conquer their own fear will survive.',
     'release_date': '2021-10-22',
     'movie_image': 'Movie_images/movie_image18.png',
     'trailer_link': 'https://www.youtube.com/watch?v=8g18jFHCLXk', },

    {'movie_name': 'DEMON SLAYER -KIMETSU NO YAIBA- THE MOVIE: MUGEN TRAIN',
     'movie_information': 'Falling forever into an endless dream... Tanjiro and the group have completed their rehabilitation training at the Butterfly Mansion, and they arrive to their next mission on the Mugen Train, where over 40 people have disappeared in a very short period of time. Tanjiro and Nezuko, along with Zenitsu and Inosuke, join one of the most powerful swordsmen within the Demon Slayer Corps, Flame Hashira Kyojuro Rengoku, to face the demon aboard the Mugen Train on track to despair.',
     'release_date': '2020-10-16',
     'movie_image': 'Movie_images/movie_image19.png',
     'trailer_link': 'https://www.youtube.com/watch?v=ATJYac_dORw', },

    {'movie_name': 'NOMADLAND',
     'movie_information': 'A woman embarks on a journey through the American West after losing everything during the recession.',
     'release_date': '2020-09-11',
     'movie_image': 'Movie_images/movie_image20.png',
     'trailer_link': 'https://www.youtube.com/watch?v=6sxCFZ8_d84', },
    ]


    # --------------------------------------sundown----------------------------------------
    movie1_review = [
        {    
            'review_content':'I Want You Back is sweeter and more sensitive than you might expect from this kind of broad mainstream romp.',
            'grade':3,
        },
        {    
            'review_content':'Jenny Slate and Charlie Day deserve better than I Want You Back, a leaden rom-com that gives them a shot at being funny, charming, and sweet, only to squander it scene by scene.',  
            'grade':6,
        },
        {    
            'review_content':'Slate and Day are better known for more heightened comedic roles and for their distinctively husky but sometimes squeaky voices. But here they are wonderfully warm and endearing as two good people who are very sad and a little lost.',
            'grade':7,
        },
    ]
    # --------------------------------------Dog----------------------------------------
    movie2_review = [   
        {    
            'review_content':'The screenplay finds it hard to straddle the line between being a light-hearted animal flick that kids can equally enjoy, and a darker tale of war, PTSD and suicide.',
            'grade':5,
        },
        {    
            'review_content':'A typically congenial, occasionally touching, if far-from-exceptional tale of the bond between two damaged souls, both wounded by the same war...Its no great shakes but Dog thankfully turns out to be a film that does not live up to its name.',
            'grade':7,
        },
        {    
            'review_content':'In Dog -- Tatum’s first onscreen role since 2017 -- the actor displays his trademark charm to the hilt. It turns the film, a man-pup buddy dramedy, into an easy crowd-pleaser.',
            'grade':8,
        },
    ]
    # --------------------------------------SCREAM----------------------------------------
    movie3_review = [
    {    
            'review_content':'Scream works well as its own horror with tense musical beats, suspense, and creative kills, as well as working perfectly as a meta representation of toxic fandom, modern horror, and the generational differences between characters.',
            'grade':9,
            
        },
        {    
            'review_content':'The Scream films are always commenting on themselves and movies and also how media is absorbed by the audience. What this one ends up being about is very clever.',  
            'grade':7,
        },
        {    
            'review_content':'It’s easy to like a movie that likes movies, especially if you like movies. But that’s too easy. If you really like movies, maybe you shouldn’t like Scream, and should yearn for something fresh and exciting.',
            'grade':9,
        },
    ]
    # --------------------------------------MINAMATA----------------------------------------
    movie4_review = [   
        {    
            'review_content':'As a chronicle of real-life events, Minamata plays things quite too safe to get the sort of impact it is hoping for. However, an experienced star like Depp ensures that we can comprehend the pain of a life capturing humanity at its worst.',
            'grade':9,
        },
        {    
            'review_content':'Sequences that should be thrilling or moving play out with very little energy. But Eugene\'s compelling photographs are recreated in ways that bristle with yearning compassion, reminding us of the power of a clear, honest image.',
            'grade':6,
        },
        {    
            'review_content':'Andrew Levitas has crafted a delicate yet passionate human-rights biopic, one where anger and grace balance the scale of a story incredibly powerful in its themes of redemption and injustice.',  
            'grade':1,
        },
    ]
    # --------------------------------------FRESH----------------------------------------
    movie5_review = [   
        {    
            'review_content':'A fantastic first act loses some energy as the film overstays its welcome with a draggy climax, but credit Sebastian Stan for his go-for-broke performance and Daisy Edgar-Jones for anchoring the whole enterprise. This one is plenty of fun',
            'grade':8,
        },
        {    
            'review_content':'It’s a movie that deserves to spark conversation for quite some time. The dance scenes, the charisma, it’s all meant to seduce but, hopefully, to get us to think about an unavoidably complex subject.',
            'grade':3,
        },
        {    
            'review_content':'If you want to be terrified of meeting someone to date in real life as well as being terrified of online dating, Fresh is definitely the movie for you.',  
            'grade':7,
        },
    ]
    # --------------------------------------CYRANO----------------------------------------
    movie6_review = [   
        {    
            'review_content':'While it lapses into sentimental repetition after the first hour - there is only so much pining for the beautiful Roxanne that the audience can take before it gets tiresome - Wright\'s eye for the perfect setpiece never leaves him.',
            'grade':6,
        },
        {    
            'review_content':'A lush, moving and emotionally rich story of longing, love and acceptance featuring a standout performance from Peter Dinklage who -- as he did in “The Station Agent” way back in 2003 -- proves that he is leading-man material.',  
            'grade':5,
        },
        {    
            'review_content':'Director Joe Wright has a nice romantic visual flair, especially in designing the musical numbers, but there is just too little of the play and the character that I grew up loving that make it into the film.',
            'grade':6,
        },
    ]
    # --------------------------------------THE BATMAN----------------------------------------
    movie7_review = [   
        {    
            'review_content':'This Batman is as dark, depressed and angry as many of those living in these dark, stressful times. Batman wants revenge, while the villain wants to expose government corruption. Thus, the normal superhero story formula is upended.',
            'grade':6,
        },
        {    
            'review_content':'An engaging crime thriller that stars an excellent Robert Pattinson as a brooding, vengeful Dark Knight who dives into the corrupt heart of Gotham City and emerges as a symbol of justice.',
            'grade':6,
        },
        {    
            'review_content':'With a super tight first half and a second one that tries too hard to work too many plot lines, The Batman goes back to the character\'s detective-like roots and makes Gotham dark and grim again. Se7en and Saw blending into a low key superhero movie.',  
            'grade':7,
        },
    ]
    # --------------------------------------HERE BEFORE----------------------------------------
    movie8_review = [   
    {    
            'review_content':'Here Before can’t decide if it wants to be an ambiguous drama about grief or a rug-pulling horror freak-out. Unfortunately, in trying to be both, Stacey Gregg’s debut satisfies neither impulse.',
            'grade':9,
        },
        {   
            'review_content':'Gregg is a storyteller still finding her feet. But what a pleasure it is to make her acquaintance. She’s here today, going places tomorrow.',
            'grade':2,
        },
        {    
            'review_content':'While the characters themselves are experiencing an uncanny dj vu, so are the audience, who may find that they cant quite shake the feeling theyve seen all this before.',  
            'grade':8,
        },
    ]
    # --------------------------------------I WANT YOU BACK----------------------------------------
    movie9_review = [   
        {    
            'review_content':'Here Before can’t decide if it wants to be an ambiguous drama about grief or a rug-pulling horror freak-out. Unfortunately, in trying to be both, Stacey Gregg’s debut satisfies neither impulse.',
            'grade':6,
        },
        {    
            'review_content':'Gregg is a storyteller still finding her feet. But what a pleasure it is to make her acquaintance. She’s here today, going places tomorrow.',
            'grade':1,
        },
        {   
            'review_content':'While the characters themselves are experiencing an uncanny dj vu, so are the audience, who may find that they cant quite shake the feeling theyve seen all this before.',  
            'grade':8,
        },
    ]
    # --------------------------------------BELLE----------------------------------------
    movie10_review = [   
        {    
            'review_content':'Belle proves that anime has been the single most imaginative, original, and visually innovative format of storytelling for literally decades. Heres hoping that Belle reminds naysayers in the West of that.',
            'grade':9,
        },
        {    
            'review_content':'The film’s message is a beautiful one: to integrate our real-life vulnerabilities with the persona we project is to become all the more powerful.',  
            'grade':6,
        },
        {    
            'review_content':'Belle delivers the perfect blend of drama, humour and heart. It’s a feast for both the eyes and ears, and it tells a story of love, loss, finding your inner strength and accepting who you are.',  
            'grade':8,
        },
    ]
    # --------------------------------------BLACKWIDOW----------------------------------------
    movie11_review = [   
        {    
            'review_content':'While far from being one of the best installments of the MCU, Black Widow is still a fairly decent outing, propelled by spirited performances by Scarlett Johansson and Florence Pughs characters.',
            'grade':9,
        },
        {    
            'review_content':'A Marvel film that is happy to be its own self-contained adventure. If this came in the build-up to Infinity War, it might have got lost in the shuffle. However, after two years away from the big screen, Johansson brings the universe back with style.',
            'grade':9,
        },
        {    
            'review_content':'That said, if any film had to reinvigorate the box office for audiences, Im glad its this one, which proves once again to the risk-averse Disney that having a female protagonist can actually succeed.',  
            'grade':8,
        },
    ]
    # --------------------------------------TURNING RED----------------------------------------
    movie12_review = [   
    {    
            'review_content':'I suspect tweens and teens are not the real targets anyway. The film often seems squarely, deliberately, aimed at their parents instead, offering them a gentle (if busy) reminder that they were young once too.',
            'grade':9,
        },
        {    
            'review_content':'Turning Red stands apart from the Pixar pack for being unafraid to show puberty in all its uncomfortable glory, while being funny, charming and pleasantly poignant at the same time.',

            'grade':9,  
        },
        {    
            'review_content':'A nuanced and compassionate exploration of how to reconcile differences, embrace change no matter how painful, and learn the value of seeing family members as human beings rather than extensions of yourself.',
            'grade':8,
        },
    ]
    # --------------------------------------LINGUI, THE SACRED BONDS----------------------------------------
    movie13_review = [
        {    
            'review_content':'As sad and bleak as this story starts off, Lingui (which is Chadian for bond or connection) is a film that, as it goes along, blossoms with hope and inspiration.',
            'grade':9,  
        },
        {    
            'review_content':'The economical script builds reasonable tension, and the film moves assuredly from incident to incident with a simplicity in the storytelling that makes it seem old-fashioned, but winsomely so.',
            'grade':9,  
        },
        {    
            'review_content':'The film is a social commentary that features little to no actual penetrative analysis beyond blanket statements about communal sisterhood in the face of patriarchal oppression.',
            'grade':7,  
        },
    ]
    # --------------------------------------COME FROM AWAY----------------------------------------
    movie14_review = [
        {    
            'review_content':'Not only is Come From Away relevant in a political sense, but its heart and comforting emotion expressing that no matter how bad things get we will get through it feels perfect for the modern moment.',
            'grade':3,
        },
        {    
            'review_content':'Briskly paced, it\'s also an important depiction of how disparate people can connect meaningfully, peppering scenes with observations that burst with multifaceted thoughts and feelings.',
            'grade':5,
        },
        {    
            'review_content':'As the 20th year is upon us, forget "never forget" anger and remember stories like this, where strangers rescued the stranded and the human spirit uplifts souls and emotions.',
            'grade':6,
        },
    ]

    # --------------------------------------WHO WE ARE: A CHRONICLE OF RACISM IN AMERICA----------------------------------------
    movie15_review = [
        {    
            'review_content':'Robinson\'s tone throughout is calm and reasoned, even when speaking with a white Southerner holding a Confederate flag and insisting the Civil War had nothing to do with slavery.',
            'grade':5,  
        },
        {    
            'review_content':'This mix of the personal and the historic is what drives Who We Are: A Chronicle of Racism in America, a fascinating and powerful new documentary from filmmaking sisters Emily and Sarah Kunstler.',
            'grade':3,  
        },
        {    
            'review_content':'Robinson presents a thoughtful, detailed and honest assessment of Americas denied problem and maps out the history of slavery in America. He does this quite elegantly with his lectures and interviews with people on both sides.',
            'grade':8,    
        },
    ]
    # --------------------------------------POLY STYRENE: I AM A CLICHÉ----------------------------------------
    movie16_review = [
        {    
            'review_content':'If you know squat about punk music, if you\'ve never heard of Poly Styrene, this biography holds little appeal beyond idle curiosity. If, however, the singer spoke loudly to your life as her fan, the film satisfies idol curiosity.',
            'grade':9,  
        },
        {    
            'review_content':'Its important to keep her legacy alive, while at the same time recognizing that behind the iconic music and photos she was a real, flawed woman. Poly Styrene: I Am A Cliche does exactly that.',
            'grade':9,  
        },
        {    
            'review_content':'The best footage is of the performer up on stage at some grotty club, wailing into a microphone with her band thrashing behind her, and her fans flailing in front. She looks the way punk rockers are never supposed to look. She looks happy.',
            'grade':8,
        },
    ]
    # --------------------------------------WRITING WITH FIRE----------------------------------------
    movie17_review = [
        {    
            'review_content':'Writing With Fire is not just an empathetic look at women who are breaking the barriers...It is also a masterclass for aspiring young journalists, a refresher course for the seniors and a much-needed shot of inspiration for the weary and cynical brigade.',
            'grade':9,  
        },
        {    
            'review_content':'The documentary presents a complete picture, professional and personal, of an admirable and courageous group of women who have been able to insert themselves into a field dominated not only by men but also by high castes. Full review in Spanish',
            'grade':1,  
        },
        {    
            'review_content':'This is a story of women taking their destiny into their own hands, and literally changing the world at the same time told in an entertaining and educating way to its audience.',
            'grade':8,
        },
    ]
    # --------------------------------------JUJUTSU KAISEN 0: THE MOVIE----------------------------------------
    movie18_review = [
        {    
            'review_content':'Denis Villeneuve’s windswept epic is engrossing enough to maintain an audience with an intermission and a running time twice its length.',
            'grade':4,  
        },
        {    
            'review_content':'Nowhere near as enjoyable as Villeneuve\'s inspired Blade Runner 2049, Dune is an achievement for sure, but watching it is rather like having huge marble monoliths dropped on you for two and a half hours.',
            'grade':5,  
        },
        {    
            'review_content':'If nothing else, Dune wins its place as a masterpiece of adaptation, truncating roughly half the novel into its runtime to expand the books monomaniacal focus on Paul into a more ensemble narrative.',
            'grade':6,
        },
    ]
    # --------------------------------------DEMON SLAYER -KIMETSU NO YAIBA- THE MOVIE: MUGEN TRAIN----------------------------------------
    movie19_review = [
        {    
            'review_content':'This is a movie that should be seen on the big screen if given the chance. Seeing the characters and animation of Demon Slayer on the big screen proves to be absolutely breathtaking.',
            'grade':6,
        },
        {    
            'review_content':'The animation is first rate. The classic anime character design comes alive though compelling CGI effects and a story that keeps the human emotions intact.',
            'grade':5,
        },
        {    
            'review_content':'Mugen Train is an average movie tossed into the middle of a sensationally beautiful and thoughtful anime. While Mugen Train is a highly entertaining movie with plenty of heart and action, I wouldn\'t go so far as to call it a great film.',  
            'grade':8,
        },
    ]
    # --------------------------------------NOMADLAND----------------------------------------
    movie20_review = [
        {    
            'review_content':'What is presented as a fulfilling alternative lifestyle embraced by people living on the fringes of society becomes a portrait of a broken person using the road to escape her past and shield herself from emotional ties.',
            'grade':5,
        },
        {    
            'review_content':'Featuring one of McDormand\'s best performances - a role she occupies deeply - and emotionally dissecting the economic terrors of backwater America, \'Nomadland\' is one of the best of the year.',
            'grade':4,
        },
        {    
            'review_content':'A highly recommended road-movie where the melodrama is supported with steel nails, avoiding any kind of easy solution and proudly raising the gaze of those who lost everything.',  
            'grade':8,
        },
    ]
    reviews=[movie1_review,movie2_review,movie3_review,movie4_review,movie5_review,
    movie6_review,movie7_review,movie8_review,movie9_review,movie10_review,
    movie11_review,movie12_review,movie13_review,movie14_review,movie15_review,
    movie16_review,movie17_review,movie18_review,movie19_review,movie20_review]

    users = {
        "DWIGHT":
            {
                "password": "123456",
                "user_profile": {
                    "email": "DWIGHT@gmail.com",
                    "picture": "profile_images/user1.jpg",
                    "information":'A Tropical Fish Yearns for Snow',
                }
            },
        "JOHN":
            {
                "password": "123456",
                "user_profile": {
                    "email": "JOHN@gmail.com",
                    "picture": "profile_images/user2.jpg",
                    "information":'100% minimalist and handmade.',
                }
            },
        "PETER":
            {
                "password": "123456",
                "user_profile": {
                    "email": "PETER@gmail.com",
                    "picture": "profile_images/user3.jpg",
                    "information":'soldier! You have vowed to be loyal to the Crusaders',
                }
            },
        "EDDIE":
            {
                "password": "123456",
                "user_profile": {
                    "email": "EDDIE@gmail.com",
                    "picture": "profile_images/user4.jpg",
                    "information":'Let\'s do our best today!!!!',
                }
            },
            "TASHA":
            {
                "password": "123456",
                "user_profile": {
                    "email": "TASHA@gmail.com",
                    "picture": "profile_images/user5.jpg",
                    "information":'Only they know, who is to win and lose',
                }
            },
    }
    
    for username, user in users.items():
        print(username)
        print(user)
        u = add_user(username, user["password"],user["user_profile"]['email'])
        add_user_profile(u, user["user_profile"]["picture"], user["user_profile"]["information"])

    for movie in movies:
        print(movie["movie_name"])
        add_movie(movie["movie_name"], movie["movie_information"], movie["release_date"], movie["movie_image"], movie["trailer_link"])

    for i in range(len(reviews)):
        movie = Movie.objects.all()[i]
        for movie_review in reviews[i]:
            userIndex = random.randint(0,4)
            user = User.objects.all()[userIndex]
            add_movie_review(movie, user, movie_review["review_content"], movie_review["grade"])
            
def add_movie(movie_name, movie_information, release_date, movie_image, trailer_link):
   movie = Movie.objects.get_or_create(movie_name=movie_name,
   movie_information = movie_information,
   release_date = release_date,
   movie_image = movie_image,
   trailer_link = trailer_link)[0]
   movie.save()
   return movie


def add_movie_review(movie, user, review_content, grade):
    movie_review = Movie_review.objects.get_or_create(
        movie=movie,user=user,review_content=review_content)[0]
    
    movie_review.grade = grade
    movie_review.save()
    return movie_review


def add_user(username, password,email):
    user = User.objects.create_user(
        username=username, password=password, email=email)
    user.save()
    return user


def add_user_profile(user, picture, information):
    user_perfile = UserProfile.objects.get_or_create(user=user)[0]
    user_perfile.picture = picture
    user_perfile.information = information
    user_perfile.save()
    return user_perfile


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
