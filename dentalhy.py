#第一版

#7-19
#All the ui have not done
#Simple menu for test only
#V0.1

import time
import random

def segement():
    time.sleep(1)
    print("\n\n","*"*60,"\n\n")
#check the user choosed difficulties or not
def difficulties_check(data_list):
    try:
        difficulties = data_list[3]
    except:
        print("You have not choose the difficulties yet")
        main()

#properties of basically all setting things
def import_data():
    """Import the data at the start of game every time"""
    #name clean_rating comfort_rating
    #for meal only -----------------------------------------------------
    brushing_with_soda = ["Brushing_with_soda",2,0.5]
    brushing_teeth = ["Brushing_teeth",1.5,1.5]
    #meal and snacks available------------------------------------------
    mouthwash = ["Mouthwash",0.5,2]
    mint = ["Mint",0,3]
    green_tea_mintflav = ["Green_tea_mintflav",0.5,1.5]
    chewing_gum = ["Chewing_gum",2,1]

    meal_clean = [brushing_with_soda,brushing_teeth,mouthwash,mint,green_tea_mintflav,chewing_gum]
    snack_clean = [mouthwash,mint,green_tea_mintflav,chewing_gum]

    #foods menu
    #Breakfast----------------------------------------------------------
    weetbix = ["Weetbix",-1,-0.5]
    weetbix_with_sugar = ["Weetbix_with_sugar",-1.5,-0.5]
    choc_cereal = ["Choc_cereal",-1,-1]
    pancake_with_sourcream = ["Pancake_with_sourcream",-1,-0.5]
    toast = ["Toast",-0.5,-0.5]
    bacon_and_egg = ["Bacon_and_egg",-1,-1]
    
    breakfast_menu = [weetbix,weetbix_with_sugar,choc_cereal,pancake_with_sourcream,toast,bacon_and_egg]
    
    #morning tea--------------------------------------------------------
    sausage_roll = ["Sausage_roll",-1,-1]
    choc_bar = ["Choclate_bar",-0.5,-1.5]
    carrot_bar = ["Carrot_bar",-0.5,+0.5]
    apple = ["Apple",-0.5,0]
    carrot_cake = ["Carrot_cake",-0.5,-0.5]
    
    morning_tea_menu = [sausage_roll,choc_bar,carrot_cake,apple,carrot_cake]

    #lunch--------------------------------------------------------------
    pasta = ["Pasta",-1,-1]
    vegan_sandwitch = ["Vegan_sandwitch",-1,-0.5]
    sandwitch = ["Sandwitch",-1,-1]
    panini = ["Panini",-1,-1.5]
    pie = ["Pie",-1,-0.5]
    pizza = ["Pizza",-1.5,-1]
    burger = ["burger",-1,-1.5]
    
    lunch_menu = [pasta,vegan_sandwitch,sandwitch,panini,pie,pizza,burger]

    #dinner-------------------------------------------------------------
    cornsoup_and_bread = ["Cornsoup_and_bread",-1,-0.5]
    steak = ["Steak",-0.5,-1]
    udon_noodles = ["udon_noodles",-1.5,-0.5]
    mashed_potato_gravy = ["Mashed_potato_and_gravy",-1,-2]
    lemon_chicken = ["Lemon_chicken",-1,-0.5]
    tuna_potato_bake = ["Tuna_potato_bake",-1,-1]

    dinner_menu = [cornsoup_and_bread,steak,udon_noodles,mashed_potato_gravy,lemon_chicken,tuna_potato_bake]
    
    #roll all the data into a list and seperate later-------------------
    data_list = [[meal_clean,snack_clean],[breakfast_menu,morning_tea_menu,lunch_menu,dinner_menu]]
    return(data_list)
    

def main():#尚未完成 have not done
    import random 
    """The main menu shows t othe user when the game first open"""
    data_list = import_data()
    passed_levels = 0
    current_hp = 8
    current_clearance = 10
    current_comfortance = 10
    data_list.append([passed_levels,current_hp,current_clearance,current_comfortance])
    data_list.append("easy")

   
    keep_going = True
    while keep_going:
        avaliable_options_menu = ["g","q","d","s","r","i"]
        print("             Menu","\n"+"_"*30,"\n\n| G/g to game                |\n| D/d to difficulty choose   |\n| S/s to save data           |\n| Q/q to quit                |","\n| I/i to load saved data     |""\n| R/r to Read the rules      |","\n"+"_"*30)
        choosed = False
        if not choosed:
            user_input = input("Pleased enter option code \n")
            user_input = user_input.lower()
            if user_input in avaliable_options_menu:
                choosed = True
            else:
                choosed = False
                print("Pleade enter a valid code")
                segement()

                
        #after choose, turn into matched defs
        if user_input == "g":
            segement()
            data_list = level_choose(data_list)
            segement()
          
        elif user_input == "q":
            print("Thanks for playing")
            keep_going = False
            segement()
            quit
        elif user_input == "s":
            save(data_list)
            
        elif user_input == "d":
            segement()
            data_list[3] = difficulties_choose()
        elif user_input == "r":
            rules()
        elif user_input == "i":
            returned = import_user()
            data_list[2] = returned[0]
            data_list[3] = returned[1]

#to let user choose difficulties and return to main, store into the data_list
def difficulties_choose():#working fine
    choosed = False
    avaliable_options_difficulties = {"1":"easy","2":"hard","3":"hardest"}
    while not choosed:
        if user_input in avaliable_options_difficulties:
            print("  Avaliable ")
            print(" Difficulties ")
            print("_"*15,"\n")
            print("|1 for easy   |\n|2 for hard   |\n|3 for hardest|")
            print("_"*15)
            user_input = str(input("Please enter a number to choose\n"))
            choosed = True
            choice = avaliable_options_difficulties[user_input]
            print("\n")
            print("-_"*15)
            print("\nYou have choosed '{}' mode".format(avaliable_options_difficulties[user_input]))
            print("_-"*15)
        else:
            choosed = False
            print("Please enter a valid number")
            segement()
    segement()
    return(choice)



def level_choose(data_list):
    keep_going = True
    difficulties_check(data_list)
    passed_levels = data_list[2][0]
    
    while keep_going:
        print("Difficulty: {} ".format(data_list[3]).title())
        print("Currently you are up to level'{}' now\nMax level is level 12".format(data_list[2][0]+1))
        print("\n\n        Options""\n"+"_"*30,"\n\n| C/c to continue            |","\n| Q/q to back to main        |","\n| R/r to Read the rules      |","\n"+"_"*30)
        print("Please enter option code")
        user_input = str(input(""))
        
        if user_input.lower() == "c":
            segement()
            data_list = game(data_list)
            segement()
        elif user_input.lower() == "q":
            keep_going = False
            return(data_list)
        elif user_input.lower() == "r":
            rules()
        else:
            print("Invalid code, please enter again")
    return(data_list)
    
#have not start
#will be done after game def
def save_data():
    pass

def rules():
    segement()
    print("_"*40)
    time.sleep(1.6)
    print("\n\nYou have\n")
    time.sleep(1.6)
    print("7/10/10(HP/Clean Rating/Comfort rating at easy\n")
    time.sleep(1.6)
    print("7/8/8 at hard\n")
    time.sleep(1.6)
    print("5/8/8 at hardest\n")
    time.sleep(1.6)
    print("If your comfort/clean rating is lower than 50%\n")
    time.sleep(1.6)
    print("Which is 5 for easy and 4 for both hard and hardest\n")
    time.sleep(1.6)
    print("Your HP will decrease 0.5 each round\n")
    time.sleep(1.6)
    print("Default difficulty is easy\n")
    time.sleep(1.6)
    print("_"*40)
    time.sleep(1.6)
    segement()
    
    


def game(data_list):
    difficulties_check(data_list)
    """Converting data-----------------------------------"""
    #seperate the datalist into small single lists
    meal_clean = data_list[0][0]
    snack_clean = data_list[0][1]

    #import menus
    breakfast_menu = data_list[1][0]
    morning_tea_menu = data_list[1][1]
    lunch_menu = data_list[1][2]
    dinner_menu = data_list[1][3]

    #MAX hp,cleaniness,comfort_rating, depending on difficulties
    difficulty = data_list[3]
    avaliable_options_difficulties = {"easy":0,"hard":1,"hardest":2}
    matched_values = [[7,10,10],[7,8,8],[5,8,8]]
    max_hp = matched_values[avaliable_options_difficulties[difficulty]][0]
    max_clean_rating = matched_values[avaliable_options_difficulties[difficulty]][1]
    max_comfort_rating = matched_values[avaliable_options_difficulties[difficulty]][2]
    
    #check the data unit is empty or not, if yes, make a new start.
    try:
        passed_levels = data_list[2][0]
        current_hp = data_list[2][1]
        current_clean_rating = data_list[2][2]
        current_comfort_rating = data_list[2][3]
    except:
        passed_levels = 0
        current_hp = max_hp
        current_clean_rating = max_cleaniness
        current_comfort_rating = max_comfort_rating
    """--------------------------------------------------"""

    user_data = []
    max_list = [max_hp,max_clean_rating,max_comfort_rating,passed_levels]
    current_list = [current_hp,current_clean_rating,current_comfort_rating]
    clean_list = [meal_clean,snack_clean]
    menu_list = [breakfast_menu,morning_tea_menu,lunch_menu,dinner_menu]
    user_data = [menu_list,clean_list,max_list,current_list,""]
    keep_going = True

    
    while keep_going:
        #breakfast
        user_data[4] = "breakfast"
        segement()
        user_data = meal_process(user_data)
        #morning tea
        user_data[4] = "morning_tea"
        segement()
        user_data = meal_process(user_data)
        #lunch
        user_data[4] = "lunch"
        segement()
        user_data = meal_process(user_data)
        #dinner
        user_data[4] = "dinner"
        segement()
        user_data = meal_process(user_data)
        
        passed_levels += 1
        user_data[2][3] = passed_levels
        print("_ "*15)
        print("Another day finished, you are up to day {} now".format(user_data[2][3]+1))
        user_option = str(input("Enter 'stop' to back to level choosing menu\nOr enter anykey to continue\n"))
        print("_ "*15)
        if user_option.lower() == "stop":
            keep_going = False
            user_data[3].insert(0,passed_levels)
            data_list[2] = user_data[3]
            return(data_list)
        else:
            keep_going = True
        
        
            
   

def death_trigger(current_hp):
    """
    check user's hp every time, if <= 0 will trigger the death event
    """
    if current_hp == 0 or current_hp < 0:
        print("You died\nGame over")
        main()

def clean_tool_choose_meal(meal_clean):
    """
    allow user to choose a single tool to clean their teeth
    tool name/roder must in the avaliable list
    if no ask user to choose again
    main meal tools
    """

    name_list = []
    for i in range(len(meal_clean)):
        name_list.append(meal_clean[i][0])
    print("_"*30)
    print("_"*9,"Tool Menu","_"*10)
    print("_"*30)
    for i in range(len(name_list)):
        print("|Code:{}\n|name:{} ".format(i,name_list[i]))
        print("|Clean rating +{}\n|Comfort rating +{}".format(meal_clean[i][1],meal_clean[i][2]))
        if i == len(name_list)-1:
            print("_"*30)
        else:
            print(" -"*15)

    choosed = False
    while not choosed:
        order_list = []
        for i in range(len(name_list)):
            order_list.append(str(i))
            
        user_input = str(input("Please enter name or code to choose\n"))
        if user_input in name_list:
            tool_order = name_list.index(user_input)
            choosed = True
        elif user_input in order_list:
            tool_order = int(user_input)
            choosed = True
        else:
            choosed = False
            print("Invalid name")
    return(meal_clean[tool_order])
    
def clean_tool_choose_snack(snack_clean):
    """
    allow user to choose a single tool to clean their teeth
    tool name/roder must in the avaliable list
    if no ask user to choose again
    snack tools
    """
    
    name_list = []
    for i in range(len(snack_clean)):
        name_list.append(snack_clean[i][0])
    print("_"*30)
    print("_"*9,"Tool Menu","_"*10)
    print("_"*30)
    for i in range(len(name_list)):
        print("|Code:{}\n|Name:{} ".format(i,name_list[i]))
        print("|Clean rating +{}\n|Comfort rating +{}".format(meal_clean[i][1],meal_clean[i][2]))
        if i == len(name_list)-1:
            print("_"*30)
        else:
            print(" -"*15)

    choosed = False
    
    while not choosed:
        order_list = []
        for i in range(len(name_list)):
            order_list.append(str(i))
            
        user_input = str(input("Please enter name to choose"))
        if user_input in name_list:
            tool_order = name_list.index(user_input)
            choosed = True
        elif user_input in order_list:
            tool_order = int(user_input)
            choosed = True
        else:
            choosed = False
            print("Invalid name")
    return(snack_clean[tool_order])


def meal_process(user_data):
    """seperate the data list into small list for use later
    identify the meal, find the matched menu and clean menu
    check user's current hp, if = 0 then die
    ask to choose clean tool and return properties
    properties calculating
    return the data list
    """
    #seperate
    menu_list = user_data[0]
    meal_clean = user_data[1][0]
    snack_clean = user_data[1][1]


    max_hp = user_data[2][0]
    max_clean_rating = user_data[2][1]
    max_comfort_rating = user_data[2][2]
    current_hp = user_data[3][0]
    current_clean_rating = user_data[3][1]
    current_comfort_rating = user_data[3][2]


    meal_list = ["breakfast","morning_tea","lunch","dinner"]
    meal_order = meal_list.index(user_data[4])
    meal_menu = menu_list[meal_order]

    
    death_trigger(current_hp)
    
    meal_prop = meal_menu[random.randint(0,len(meal_menu)-1)]

    print("- - - - - -")
    print("[Day{} {}]".format(user_data[2][3]+1,user_data[4]))
    print("- - - - - -\n\n\n")
    print("Food: {}\ncomfort rating  {}\nclean rating  {}".format(meal_prop[0],meal_prop[1],meal_prop[2]))

    meal_name = meal_prop[0]
    meal_clean_rating = meal_prop[1]
    meal_comfort_rating = meal_prop[2]

    if meal_order == 1 or meal_order == 2:
        choosed_tool_prop = clean_tool_choose_meal(snack_clean)
        choosed_tool_name = choosed_tool_prop[0]
        choosed_tool_clean_rating = choosed_tool_prop[1]
        choosed_tool_comfort_rating = choosed_tool_prop[2]
    else:
        choosed_tool_prop = clean_tool_choose_meal(meal_clean)
        choosed_tool_name = choosed_tool_prop[0]
        choosed_tool_clean_rating = choosed_tool_prop[1]
        choosed_tool_comfort_rating = choosed_tool_prop[2]

    #processing of clean rating and comfort rating
    current_clean_rating += meal_clean_rating
    current_clean_rating += choosed_tool_clean_rating
    current_comfort_rating += meal_comfort_rating
    current_comfort_rating += choosed_tool_comfort_rating

    #limit the max ratings
    if current_hp > max_hp:
        current_hp = max_hp
    if current_clean_rating > max_clean_rating:
        current_clean_rating = max_clean_rating
    if current_comfort_rating > max_comfort_rating:
        current_comfort_rating = max_comfort_rating
    
    #process of hp
    if current_clean_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low clean rating")
    elif current_comfort_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low comfort rating")
    else:
        print("Your teeth are still comfort & clean now")
    print("\n{} current hp\n{} current clean rating\n{} current comfort rating\n".format(current_hp,current_clean_rating,current_comfort_rating))
    current_list = [current_hp,current_clean_rating,current_comfort_rating]
    user_data[3] = current_list
    return(user_data)


def save(data_list):
    segement()
    
    file = open("user_data.txt","w")
    for i in range(4):
        file.write(str(data_list[2][i]))
        file.write(":")
        
    file.write(str(data_list[3]))
    file.close()
    print("Level: {}\nMode: {}\nSAVED".format(data_list[2][0]+1,data_list[3].title()))
    segement()

def import_user():
    segement()
    file = open("user_data.txt")
    initial_data = file.readline()
    data = initial_data.split(":")
    
    current_list = []
    for i in range(4):
        if i == 0:
            current_list.append(int(data[i]))
        else:
            current_list.append(float(data[i]))
    print("Level: {}\nMode: {}\nLOADED".format(current_list[0]+1,data[4].title()))
    segement()
    return([current_list,data[4]])
        
    
main()
    

        
    
    
