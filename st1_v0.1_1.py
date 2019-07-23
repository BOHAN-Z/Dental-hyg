#第一版

#7-19
#All the ui have not done
#Simple menu for test only
#V0.1

import random

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
    #for meal only 
    brushing_with_soda = ["Brushing_with_soda"]
    brushing_teeth = ["Brushing_teeth",1.5,1.5]
    #meal and snacks avalioable
    mouthwash = ["Mouthwash",0,5,2]
    mint = ["Mint",0,3]
    green_tea_mintflav = ["Green_tea_mintflav",0.5,1.5]
    chewing_gum = ["Chewing_gum",2,1]

    meal_clean = [brushing_with_soda,brushing_teeth,mouthwash,mint,green_tea_mintflav,chewing_gum]
    snack_clean = [mouthwash,mint,green_tea_mintflav,chewing_gum]

    #foods menu
    #Breakfast
    weetbix = ["Weetbix",-1,-0.5]
    weetbix_with_sugar = ["Weetbix_with_sugar",-1.5,-0.5]
    choc_cereal = ["Choc_cereal",-1,-1]
    pancake_with_sourcream = ["Pancake_with_sourcream",-1,-0.5]
    toast = ["Toast",-0.5,-0.5]
    bacon_and_egg = ["Bacon_and_egg",-1,-1]
    
    breakfast_menu = [weetbix,weetbix_with_sugar,choc_cereal,pancake_with_sourcream,toast,bacon_and_egg]
    
    #morning tea
    sausage_roll = ["Sausage_roll",-1,-1]
    choc_bar = ["Choclate_bar",-0.5,-1.5]
    carrot_bar = ["Carrot_bar",-0.5,+0.5]
    apple = ["Apple",-0.5,0]
    carrot_cake = ["Carrot_cake",-0.5,-0.5]
    
    morning_tea_menu = [sausage_roll,choc_bar,carrot_cake,apple,carrot_cake]

    #lunch
    pasta = ["Pasta",-1,-1]
    vegan_sandwitch = ["Vegan_sandwitch",-1,-0.5]
    sandwitch = ["Sandwitch",-1,-1]
    panini = ["Panini",-1,-1.5]
    pie = ["Pie",-1,-0.5]
    pizza = ["Pizza",-1.5,-1]
    burger = ["burger",-1,-1.5]
    
    lunch_menu = [pasta,vegan_sandwitch,sandwitch,panini,pie,pizza,burger]

    #dinner
    cornsoup_and_bread = ["Cornsoup_and_bread",-1,-0.5]
    steak = ["Steak",-0.5,-1]
    udon_noodles = ["udon_noodles",-1.5,-0.5]
    mashed_potato_gravy = ["Mashed_potato_and_gravy",-1,-2]
    lemon_chicken = ["Lemon_chicken",-1,-0.5]
    tuna_potato_bake = ["Tuna_potato_bake",-1,-1]

    dinner_menu = [cornsoup_and_bread,steak,udon_noodles,mashed_potato_gravy,lemon_chicken,tuna_potato_bake]
    
    #roll all the data into a list and seperate later
    data_list = [[meal_clean,snack_clean],[breakfast_menu,morning_tea_menu,lunch_menu,dinner_menu]]
    return(data_list)
    

    
    
    
    
    
def main():#尚未完成 have not done
    import random 
    """The main menu shows t othe user when the game first open"""
    data_list = import_data()
    passed_levels = 0
    remain_hp = 8
    current_clearance = 10
    current_comfortance = 10
    data_list.append([passed_levels,remain_hp,current_clearance,current_comfortance])
    data_list.append("easy")
    
    avaliable_options_menu = ["g","t","q","d","s"]
    choosed = False
    if not choosed:
        user_input = input("Pleased enter the option code")
        user_input = user_input.lower()
        if user_input in avaliable_options_menu:
            choosed = True
        else:
            choosed = False
            print("Pleade enter a valid code")
            
    #after choose, turn into matched defs
    if user_input == "g":
        level_choose(data_list)
    elif user_input == "t":
        test()
    elif user_input == "q":
        quit
    elif user_input == "s":
        save_data()
    elif user_input == "d":
        difficulties = difficulties_choose()

#难易度已完成
#to let user choose difficulties and return to main, store into the data_list
def difficulties_choose():#working fine
    choosed = False
    avaliable_options_difficulties = {"1":"easy","2":"hard","3":"hardest"}
    while not choosed:
        print("1 for easy\n2 for hard\n3 for hardest")
        user_input = str(input("Please enter a number to choose"))
        if user_input in avaliable_options_difficulties:
            choosed = True
            choice = avaliable_options_difficulties[user_input]
        else:
            choosed = False
            print("Please enter a valid number")
    
    return(choice)

#
def level_choose(data_list):
    difficulties_check(data_list)
    
    passed_levels = data_list[2][0]
    print("You are up to level'{}' now, max level is level 12".format(passed_levels+1))
    user_input = str(input("Please enter c to continue or q to quit"))
    
    if user_input.lower() == "c":
        game(data_list)
    elif user_input.lower() == "q":
        main()
    
    
#have not start
#will be done after game def
def save_data():
    pass

    

def game(data_list):
    difficulties_check(data_list)
    """Converting data-----------------------------------"""
    #seperate the datalist into small single lists
    meal_clean = data_list[0][0]
    snack_clean = data_list[0][1]
    
    breakfast_menu = data_list[1][0]
    morning_tea_menu = data_list[1][1]
    lunch_menu = data_list[1][2]
    dinner_menu = data_list[1][3]

    difficulty = data_list[3]

    avaliable_options_difficulties = {"easy":1,"hard":2,"hardest":3}
    
    #MAX hp,cleaniness,comfort_rating, depending on difficulties
    matched_values = [[10,10,10],[7,8,8],[5,8,8]]
    max_hp = matched_values[avaliable_options_difficulties[difficulty]][0]
    max_clean_rating = matched_values[avaliable_options_difficulties[difficulty]][1]
    max_comfort_rating = matched_values[avaliable_options_difficulties[difficulty]][2]
    
    #check the data unit is empty or not, if yes, make a new start.
    try:
        passed_levels = data_list[2][0]
        remain_hp = data_list[2][1]
        current_clean_rating = data_list[2][2]
        current_comfort_rating = data_list[2][3]
    except:
        passed_levels = 0
        remain_hp = max_hp
        current_clean_rating = max_cleaniness
        current_comfort_rating = max_comfort_rating
    """--------------------------------------------------"""
        
    ######  HARD CODING WARNING (FOR TEST ONLY, WILL CHANGE INTO A DEF LATER)
        
    #breakfast
    death_trigger(remain_hp)
    meal_prop = breakfast_menu[random.randint(0,len(breakfast_menu))]
    print(meal_prop)
    meal_name = meal_prop[0]
    meal_clean_rating = meal_prop[1]
    meal_comfort_rating = meal_prop[2]

    #processing of clean rating and comfort rating
    current_clean_rating += meal_clean_rating
    current_comfort_rating += meal_comfort_rating
    #process of hp
    if current_clean_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low clean rating")
    elif current_comfort_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low comfort rating")
    else:
        print("Your teeth are still comfort & clean now\nKeep it up")
    print("\n{} remain hp\n{} current clean rating\n{} current comfort rating\n".format(remain_hp,current_clean_rating,current_comfort_rating))



    #morning tea
    death_trigger(remain_hp)
    meal_prop = morning_tea_menu[random.randint(0,len(morning_tea_menu))]
    meal_name = meal_prop[0]
    print(meal_prop)
    meal_clean_rating = meal_prop[1]
    meal_comfort_rating = meal_prop[2]

    #processing of clean rating and comfort rating
    current_clean_rating += meal_clean_rating
    current_comfort_rating += meal_comfort_rating
    #process of hp
    if current_clean_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low clean rating")
    elif current_comfort_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low comfort rating")
    else:
        print("Your teeth are still comfort & clean now\nKeep it up")
    print("\n{} remain hp\n{} current clean rating\n{} current comfort rating\n".format(remain_hp,current_clean_rating,current_comfort_rating))


    #lunch
    death_trigger(remain_hp)
    meal_prop = lunch_menu[random.randint(0,len(lunch_menu))]
    print(meal_prop)
    meal_name = meal_prop[0]
    meal_clean_rating = meal_prop[1]
    meal_comfort_rating = meal_prop[2]

    #processing of clean rating and comfort rating
    current_clean_rating += meal_clean_rating
    current_comfort_rating += meal_comfort_rating
    #process of hp
    if current_clean_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low clean rating")
    elif current_comfort_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low comfort rating")
    else:
        print("Your teeth are still comfort & clean now\nKeep it up")
    print("\n{} remain hp\n{} current clean rating\n{} current comfort rating\n".format(remain_hp,current_clean_rating,current_comfort_rating))


    #dinner
    death_trigger(remain_hp)
    meal_prop = dinner_menu[random.randint(0,len(dinner_menu))]
    print(meal_prop)
    meal_name = meal_prop[0]
    meal_clean_rating = meal_prop[1]
    meal_comfort_rating = meal_prop[2]

    #processing of clean rating and comfort rating
    current_clean_rating += meal_clean_rating
    current_comfort_rating += meal_comfort_rating
    #process of hp
    if current_clean_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low clean rating")
    elif current_comfort_rating < max_clean_rating*0.5:
        current_hp += -0.5
        print("Your hp decreased 0.5 because of low comfort rating")
    else:
        print("Your teeth are still comfort & clean now\nKeep it up")
    print("\n{} remain hp\n{} current clean rating\n{} current comfort rating\n".format(remain_hp,current_clean_rating,current_comfort_rating))

    
    
#check hp every time
def death_trigger(remain_hp):
    if remain_hp == 0 or remain_hp < 0:
        print("You died\nGame over")
        main()

def clean_tool_choose_meal(meal_clean):
    pass
def clean_tool_choose_snack(snack_clean):
    pass
main()
    


    
    
