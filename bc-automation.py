# >>imported our modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


# >>Accessing our website
PATH = "C:/chromedriver_win32(113.0.5)/chromedriver.exe"
Driver = webdriver.Chrome(PATH)

Driver.get('https://bc.game')  

for i in range(3):
    print('We are in !')

time.sleep(30) # my login time
print('wait 1')
time.sleep(30)
print('Wait 2')
time.sleep(10)
print('Wait 3')

# >>accessing all buttons similar to our target
button_list = Driver.find_elements(By.CLASS_NAME, "button-inner")
print(f'the number of buttons on limbo page {len(button_list)}')  # >>ensuring we're on the right page, our page has 97 similar buttons 

# >>accepting the cookies to clear up the page
cookie_element = button_list[0]
cookie_element.click()

# >>accessing last result
# recent_list = Driver.find_element(By.CLASS_NAME, "recent-list")
# print(recent_list.text)
# list_of_8results = recent_list.find_elements(By.CLASS_NAME, "recent-item")
# for recent_item in list_of_8results:
#     last_result = recent_item.find_element(By.TAG_NAME, "div")
#     print(f'last result is {last_result.text}')
# last_result = list_of_8results[7].find_element(By.TAG_NAME, "div")
# prelast_result = list_of_8results[6].find_element(By.TAG_NAME, "div")

# >>accessing input fields
limbo_page_inputs = Driver.find_elements(By.TAG_NAME, "input")  # >>accessing all input fields
print(f'the length of input field list is {len(limbo_page_inputs)}') # >>should be 2 values
bet_amount_field = limbo_page_inputs[0]  # >>accessing BET_AMOUNT input field
# print(bet_amount_field.get_attribute('value'))
# bet_amount_field.click()
# bet_amount_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
# bet_amount_field.send_keys("2000")

time.sleep(1)

payout  = limbo_page_inputs[1]  # >>accessing PAYOUT input field
payout.send_keys(Keys.SHIFT + Keys.HOME, Keys.BACKSPACE)  # >>clearing the input field and replacing values
payout.send_keys("2")

# >> bet action button
bet_action = button_list[2]
# bet_action.click()
# print('done!')

time.sleep(1)

#>>>>>>>>>>>>>>>>>>>>>START<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

starting_balance = 4
balance_goal = 7.8
initial_bet = 0.0039
current_bet_amount = 0
min_bet = 0.0
loss_counter = 1
current_balance = starting_balance
playgame_counter = 0
oscillation_counter = 0
down_steper = 1

time.sleep(1)

while (balance_goal) > current_balance >= (current_bet_amount * 2):
    
    recent_list = Driver.find_element(By.CLASS_NAME, "recent-list")
    list_of_8results = recent_list.find_elements(By.CLASS_NAME, "recent-item")
    last_result = list_of_8results[7].find_element(By.TAG_NAME, "div")
    prelast_result = list_of_8results[6].find_element(By.TAG_NAME, "div")

    pre_bet_result = last_result.get_attribute('class')
    pre_pre_bet_result = prelast_result.get_attribute('class')
    # print(f'pre_bet_result {pre_bet_result}')
    # print(f'pre_pre_bet_result is {pre_pre_bet_result}')
    
    if 'item-wrap is-win' in pre_bet_result:
        
        current_bet_amount = (initial_bet * loss_counter * down_steper)
       
        bet_amount_field.click()
        bet_amount_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        bet_amount_field.send_keys(f'{current_bet_amount}')
       
        time.sleep(1)

        bet_action.click()

        playgame_counter += 1

        

    else:
        current_bet_amount = min_bet
        
        bet_amount_field.click()
        bet_amount_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        bet_amount_field.send_keys(f'{current_bet_amount}')
       
        time.sleep(1)

        bet_action.click()
        
        playgame_counter += 1

    time.sleep(3)
    
    new_recents = Driver.find_element(By.CLASS_NAME, "recent-list")
    new_recent_list = recent_list.find_elements(By.CLASS_NAME, "recent-item")
    new_last_result = new_recent_list[7].find_element(By.TAG_NAME, "div")
   
    post_bet_result = new_last_result.get_attribute('class')
    # print(f'post_bet_result is {post_bet_result}')
    
    print(f'we just bet ${current_bet_amount}')
    # time.sleep(1)


    if  'item-wrap is-win' in post_bet_result:
        current_balance += current_bet_amount
    else:
        current_balance -= current_bet_amount
    print (f'current_balance is {current_balance}')

# >> advancment on martingale
    if  'item-wrap is-win' in pre_bet_result and  'item-wrap is-lose' in post_bet_result:
        loss_counter *= 2
    elif 'item-wrap is-win' in pre_bet_result and  'item-wrap is-win' in post_bet_result: # resetting bet amount
        loss_counter = 1
        oscillation_counter += 1
        down_steper = 1
    
    if  'item-wrap is-win' in  pre_pre_bet_result and  'item-wrap is-win' in pre_bet_result and  'item-wrap is-lose' in post_bet_result:
        down_steper = 0.5
    
    pre_bet_result = post_bet_result
    # time.sleep(1)


starting_balance = current_balance


total_games_played = playgame_counter
total_oscillations = oscillation_counter
print(f'In this session, we betted {total_games_played} times')
print(f'And we oscillated {total_oscillations} times')

print(f'our final balance is {current_balance}')
print('Next round/End of round')


# >>list of buttons

# # cookie_element = button_list[0]
# # sign_up = button_list[1](text- Sign up)
# # sign_up1 = button_list[2](text- Sign Up Now)(home page
# # element[3] = not accessible(home page
# # bet_action = button_list[2](on limbo page
