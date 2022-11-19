print("This is my interesting program about choosing a series")

# Being indecisive is hard. Since, I love watching series but still, having a hard time choosing what to watch.
# I'm lucky to got passed by in one of "Tina Huang" youtube video. So, I have some idea on how to do a program
# in choosing a random series.
# Here's the link on her video, (https://youtu.be/_xf1TMs0ysk)

from random import choice

while True:
    # Letting the user choose what he wants to watch, be it anime, series, movie.
    print("Options:\n"
          "1.Anime\n"
          "2.Series\n"
          "3.Movie")
    option = input("What do you want to watch? ")
    # create a list for anime
    anime = ['Your Name', 'Haikyuu', 'Black Clover', 'One Piece', 'Kimi Ni Todoke', 'Jujutsu Kaisen',
             'Seven Deadly Sins']
    # create a list for series option
    series = ['Gilmore Girls', 'Greys Anatomy', 'Stranger Things', 'Sex Education', 'The Umbrella Academy',
              'Bridgerton', 'Queens Gambit', 'Euphoria', 'Money Heist', 'Emily in Paris']
    # create a list for movie option
    hw_movie = ['10 things I hate about you', 'Enola Homes', 'Wonder', 'Mean Girls', 'The Devil Wears Prada',
                'Breakfast Club', 'Flipped', 'Narnia', 'Bridge to Terabithia', 'Poltergeist', 'Insidious', 'The Notebook',
                ]
    filo_movie = ['Barcelona: A love untold', 'The Hows of Us', 'My Ex and Whys', 'Im Drunk, I love you',
                  'Kita Kita', 'Doll House', 'Goyo: Ang Batang Heneral', 'Heneral Luna', 'Four Sisters and A Wedding',
                  'Seven Sundays']
    k_movie = ['On your Wedding Day', '20th Century Girl', 'Sweet and Sour', 'Seoul Vibe', 'Peninsula', 'Parasite',
               'Train to Busan', 'Alive', 'The Call']
    if option == '1':
        print(choice(anime))
    elif option  == '2':
        print(choice(series))
    elif option =='3':
        for_movie = input("What kind of movie do you want to watch?\n"
                          "1. Hollywood Movies\n"
                          "2. Filipino Movies\n"
                          "3. Korean Movies\n"
                          "4. Others\n"
                          "Answer: ")
        if for_movie == '1':
            print(choice(hw_movie))
        elif for_movie == '2':
            print(choice(filo_movie))
        elif for_movie == '3':
            print(choice(k_movie))
    else:
        print("Try again. Please input a valid code. ")

    ask = input("Do you want to try again? (Y/N) ")
    if ask == 'Y':
        continue
    else:
        print("Thank you for using this program.")
        break


