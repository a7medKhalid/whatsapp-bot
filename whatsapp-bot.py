
# CP: time compare is not working will and i need to unclick the message to make it work again
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

# # you can set the chromedriver path on the system path and remove this variable
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

while True:
    # scroll sidepane to top
    sidepane = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
    driver.execute_script("arguments[0].scrollTop = 0", sidepane)

    # check if there are unread messages
    unreads = driver.find_elements(By.XPATH , "//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")

    unreadsCount = len(unreads)

    if unreadsCount == 0 :
        print('no new messages')
        # sleep(5)
        continue

    # get unread conversations
    conversations = []
    for unread in unreads:

        unread.click()

        out_messages_xpath = '//div[@class="message-in focusable-list-item _7GVCb _2SnTA _1-FMR"]//div[@class="_1-lf9 _3mSPV _18q-J"]//div[@class="ItfyB _3nbHh"]//div[@class="_27K43"]//div[@class="copyable-text"]'
        messages = driver.find_elements(By.XPATH, out_messages_xpath + '//div[@class="_21Ahp"]' )
        times = driver.find_elements(By.XPATH, out_messages_xpath )

        for message in messages:

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
            



            # check if message is not read send resopnse
            if message not in messagesDB and time_compare:
                
                msg_box = driver.find_element(By.CSS_SELECTOR, '.fd365im1.to2l77zo.bbv8nyr4.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt')
                print('sending response')
                msg_box.send_keys('hi i am a b-o-t')
                msg_box.send_keys(u'\ue007')
                messagesDB.append(message)
            
            # unclick conversation
            

        # return side pane to top to not miss selinum cordinations
        sidepane = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
        driver.execute_script("arguments[0].scrollTop = 0", sidepane)
        





# fetch unread conversations count

# get all conversations

# create decrease counter by unread conversations count

# loop through conversations

    # check if user last message is unread by checking database with messsage time stamp, text and sender
        # resond to user
        # decrease counter by 1
    # else
        # continue

    # check if counter is 0 break

# def sendResponse(driver,message):
#     name = input('Enter the name of a user')
#     msg = input('Enter your message')

#     # saving the defined contact name from your WhatsApp chat in user variable
#     user = driver.find_element('xpath', '//span[@title = "{}"]'.format(name))
#     user.click()

#     # name of span class of contatct
#     msg_box = driver.find_element('class', '/uMse')
#     msg_box.send_keys(msg)
#     sleep(5)
 
#  todos
# after counter is 2 the driver does not read messages 

# try to fetch conversation from unread indicator after recording all conversatins messages

# prssist messages DB


# new scenario 
# get messages with unread indicator and send response
# know if message is read or not by checking the time stamp to time stamp of starting the program ifbefore read if after check messages DB if not in DB send response and add to DB


# register time stamp of starting the program with date
# messagesDB = []   
# counter = 0
# while True:
#     # scroll sidepane to top
#     sidepane = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 _3fGK2']")
#     driver.execute_script("arguments[0].scrollTop = 0", sidepane)

#     unreads = driver.find_elements(By.XPATH , "//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")

#     unreadsCount = len(unreads)

#     if unreadsCount == 0 and counter > 0:
#         print('no new messages')
#         # sleep(5)
#         continue

   
#     # get all conversations
#     conversations = driver.find_elements(By.XPATH, "//span[@class='_7T_0D']//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr']")

#     for conversation in conversations:
#         conversationtext = conversation.text

#         # try:
#         conversation.click()
#         # except:
#         #     conversation = conversation.find_element(By.XPATH, "//span[@title='" + conversation.text + "']")
#         #     conversation.click()
        
#         out_messages_xpath = '//div[@class="message-in focusable-list-item _7GVCb _2SnTA _1-FMR"]//div[@class="_1-lf9 _3mSPV _18q-J"]//div[@class="ItfyB _3nbHh"]//div[@class="_27K43"]//div[@class="copyable-text"]'
#         messages = driver.find_elements(By.XPATH, out_messages_xpath + '//div[@class="_21Ahp"]' )
#         times = driver.find_elements(By.XPATH, out_messages_xpath )

#         for message in messages:

#             time = times[messages.index(message)].get_attribute('data-pre-plain-text')
#             message = message.text + ',' + str(time)

#             if message not in messagesDB:
#                 # here you can add your response
#                 messagesDB.append(message)
#                 print(message)
#                 print('----------------')
#                 # unreadsCount -= 1
#                 if counter > 0:
#                     # send response
#                     msg_box = driver.find_element(By.CSS_SELECTOR, '.fd365im1.to2l77zo.bbv8nyr4.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt')
#                     print('sending response')
#                     # msg_box.send_keys('hi i am a b-o-t')
#                     # msg_box.send_keys(u'\ue007')

                

#             else:
#                 break
#         # this code is to save iterations
#         # if unreadsCount == 0 and counter > 1:
#         #     break
#     counter += 1




































# # work conversatio by conversation

# # get all conversations
# conversations = driver.find_elements(By.CSS_SELECTOR, '._8nE1Y')


# for conversation in conversations:
#     # take daata from text
#     conversation = conversation.text.splitlines()
    
#     try :
#         unreadCount = conversation[]





# # loop through conversations
# for conversation in conversations:

#     allchildelemnts = conversation.find_elements(By.CSS_SELECTOR, "*")
#     try:
#         upper = allchildelemnts[0]
#         lower = allchildelemnts[1]

#         lower = lower.find_elements(By.CSS_SELECTOR, "*")
#         lower = lower[1]

#         lower = lower.find_elements(By.CSS_SELECTOR, "*")
#         lower = lower[0]
#     except:
#         continue

#     # if lower has unread message indicator take name from upper

#     if lower.find_element(By.CSS_SELECTOR, '._1pJ9J'):
#         print(upper.text)
#         print(lower.text)
#         print('----------------')

   








# latestDate = ''

# while True:

#     # get all conversations
#     conversations = driver.find_elements(By.CSS_SELECTOR, '.le5p0ye3.l7jjieqr._11JPr')
#     dates = driver.find_elements(By.CSS_SELECTOR, '.aprpv14t')

#     # merge conversations and dates
#     conversations = zip(conversations, dates)

#     # sort by date
#     conversations = sorted(conversations, key=lambda x: x[1].text, reverse=True)


#     for conversation in conversations:

#         if conversation[1].text > latestDate:
#             print('new message')
#             print(conversation[0].text)
#             print(conversation[1].text)
#             print('----------------')
#         else:
#             latestDate = conversation[1].text
#             print('no new messages')
#             sleep(5)
#             break

    


#     else:
#         print('no new messages')
#         sleep(5)
#         continue


#     # loop through conversations
#     for conversation in conversations:
#         date = conversation.find_element(By.CSS_SELECTOR, './EFt_').text

#         # assign latest date if date is later

#         if date > latestDate:
#             latestDate = date

        













# unreads = driver.find_elements(By.XPATH , "//span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")

# # get people with unread messages and add to list by parent
# unreadConversations = []
# for unread in unreads:
#     a = unread.find_element(By.XPATH , '..')
#     print
#     print(a.text)

#     # b = unread.parent
#     # print(b.text)

# # infinte loop to detect new messages
# while True:
#     conversations = driver.find_elements(By.CSS_SELECTOR, '.le5p0ye3.l7jjieqr._11JPr')

#     unreadConversation = []
#     for conversation in conversations:
#         # if conversation has unread span add to unread list

#         try:
#             conversationName = conversation.find_element(By.CSS_SELECTOR , "span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']")
#             unreadConversation.append(conversation)
#         except:
#             print('no')
        

#     print(conversations)
#     # read the messages

#     # send response






# # # test sending a message
# # def send_a_message(driver):
# #     name = input('Enter the name of a user')
# #     msg = input('Enter your message')

# #     # saving the defined contact name from your WhatsApp chat in user variable
# #     user = driver.find_element('xpath', '//span[@title = "{}"]'.format(name))
# #     user.click()

# #     # name of span class of contatct
# #     msg_box = driver.find_element('class', '/uMse')
# #     msg_box.send_keys(msg)
# #     sleep(5)


# # def pane_scroll(dr):
# #     global SCROLL_TO, SCROLL_SIZE

# #     print('>>> scrolling side pane')
# #     side_pane = dr.find_element('id','pane-side')
# #     dr.execute_script('arguments[0].scrollTop = '+str(SCROLL_TO), side_pane)
# #     sleep(3)
# #     SCROLL_TO += SCROLL_SIZE


# # def get_messages(driver, contact_list):
# #     global SCROLL_SIZE
# #     print('>>> getting messages')
# #     conversations = []
# #     for contact in contact_list:

# #         sleep(2)
# #         user = driver.find_element('xpath', '//span[contains(@title, "{}")]'.format(contact))
# #         user.click()
# #         sleep(3)
# #         conversation_pane = driver.find_element('xpath',"//div[@class='_2-aNW']")

# #         messages = set()
# #         length = 0
# #         scroll = SCROLL_SIZE
# #         while True:
# #             elements = driver.find_elements('xpath', "//div[@class='copyable-text']")
# #             for e in elements:
# #                 messages.add(e.get_attribute('data-pre-plain-text') + e.text)
# #             if length == len(messages):
# #                 break
# #             else:
# #                 length = len(messages)
# #             driver.execute_script('arguments[0].scrollTop = -' + str(scroll), conversation_pane)
# #             sleep(2)
# #             scroll += SCROLL_SIZE
# #         conversations.append(messages)
# #         filename = 'collected_data/conversations/{}.json'.format(contact)
# #         os.makedirs(os.path.dirname(filename), exist_ok=True)
# #         with open(filename, 'wb') as fp:
# #             pickle.dump(messages, fp)
# #     return conversations


# # def main():
# #     global SCROLL_TO, SCROLL_SIZE
# #     SCROLL_SIZE = 600
# #     SCROLL_TO = 600
# #     conversations = []

# #     options = Options()
# #     options.add_argument('user-data-dir=./User_Data')  # saving user data so you don't have to scan the QR Code again
# #     driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
# #     driver.get('https://web.whatsapp.com/')
# #     input('Press enter after scanning QR code or after the page has fully loaded\n')

# #     try:
# #         # retrieving the contacts
# #         print('>>> getting contact list')
# #         contacts = set()
# #         length = 0
# #         while True:
# #             # nothing found in the class name, so I used the xpath
# #             contacts_sel = driver.find_elements('xpath', '//*[@id="pane-side"]/div/div/div/div[17]/div/div/div/div[2]/div[1]/div[1]/span/span')
# #             contacts_sel = set([j.text for j in contacts_sel])
            
# #             conversations.extend(get_messages(driver, list(contacts_sel-contacts)))
# #             contacts.update(contacts_sel)
# #             if length == len(contacts) and length != 0:
# #                 break
# #             else:
# #                 length = len(contacts)
# #             pane_scroll(driver)
# #         print(len(contacts), "contacts retrieved")
# #         print(len(conversations), "conversations retrieved")
# #         filename = 'collected_data/all.json'
# #         os.makedirs(os.path.dirname(filename), exist_ok=True)
# #         with open(filename, 'wb') as fp:
# #             pickle.dump(conversations, fp)
# #     except Exception as e:
# #         print(e)
# #         driver.quit()


# # if __name__ == "__main__":
# #     main()







