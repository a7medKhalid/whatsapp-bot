
# CP: i need to unclick the message to make it work again
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

# you can set the chromedriver path on the system path and remove this variable
CHROMEDRIVER_PATH = 'chromedriver.exe'


# start driver

options = Options()
options.add_argument('user-data-dir=./User_Data')  # saving user data so you don't have to scan the QR Code again
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
driver.get('https://web.whatsapp.com/')
input('Press enter after scanning QR code or after the page has fully loaded\n')


from datetime import datetime
# take current time without seconds
start_time = datetime.now()
start_time = start_time.replace(second=0, microsecond=0)
print(start_time)



messagesDB = []
counter = 0
while True:
    # scroll sidepane to top
    sidepane = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
    driver.execute_script("arguments[0].scrollTop = 0", sidepane)

    # check if there are unread messages
    unreads = driver.find_elements(By.XPATH , "//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")

    unreadsCount = len(unreads)

    if unreadsCount == 0 :
        counter += 1
        
        if counter == 5:
            sleep(5)
            counter = 0
            print('no new messages')

        
        continue

    # get unread conversations
    conversations = []
    for unread in unreads:

        unread.click()

        out_messages_xpath = '//div[@class="message-in focusable-list-item _7GVCb _2SnTA _1-FMR"]//div[@class="_1-lf9 _3mSPV _18q-J"]//div[@class="ItfyB _3nbHh"]//div[@class="_27K43"]//div[@class="copyable-text"]'
        messages = driver.find_elements(By.XPATH, out_messages_xpath + '//div[@class="_21Ahp"]' )
        times = driver.find_elements(By.XPATH, out_messages_xpath )

        for message in messages:
            message_text = message.text
            time_stamp = times[messages.index(message)].get_attribute('data-pre-plain-text')
            message = message.text + ',' + str(time_stamp)

            # compare time
            text = time_stamp

            time  = text.split(']')[0].replace('[', '')

            date = time.split('،')[1].strip()
            time = time.split('،')[0].strip()
            # change arabic numbers to english
            time = time.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤', '4').replace('٥', '5').replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9').replace('م', 'PM').replace('ص', 'AM')
            date = date.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤', '4').replace('٥', '5').replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')


            message_time = time  + ',' + date
            # conver to datetime
            message_time = datetime.strptime(message_time, "%I:%M %p,%Y/%m/%d")
            
            # compare two times if meeage time is older print yes
            time_compare =  message_time >= start_time
            print(start_time,message_time)
            print(time_compare,message)
            


            msg_box = driver.find_elements(By.CSS_SELECTOR, '.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt')
            msg_box = msg_box[1]
            # check if message is not read send resopnse
            if message not in messagesDB and time_compare:

                # get user input 
                if message_text == 'مرحبا':
                    msg_box.send_keys('مرحبا بك' + '\n')
                elif message_text == 'حكمة':
                    # get random quote from api
                    import requests
                    import json
                    import random

                    url = "https://type.fit/api/quotes"
                    response = requests.get(url)
                    quotes = json.loads(response.text)
                    quote = random.choice(quotes)
                    msg_box.send_keys(quote['text'] + '\n' + quote['author'])
                else:
                    msg_box.send_keys('أرسل حكمة لتصلك حكمة')


                msg_box.send_keys(u'\ue007')
                messagesDB.append(message)
                    
                   
                

            
        # unclick conversation by clicking esc
        try:
            msg_box.send_keys(u'\ue00c')
        except:
            msg_box = driver.find_elements(By.CSS_SELECTOR, '.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt')
            msg_box = msg_box[1]
            msg_box.send_keys(u'\ue00c')
            
        
            
        # return side pane to top to not miss selinum cordinations
        sidepane = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
        driver.execute_script("arguments[0].scrollTop = 0", sidepane)
        




