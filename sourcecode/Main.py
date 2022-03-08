''' Raphael S. Vispo
Project- PYsbook
December 12, 2021'''

from keysEncrption import *
from os.path import exists
import random

#These are the paths needed to run the program CMSC12project/
userDatabasePath="databases/users-database.txt"
userAccountDatabasePath="databases/users-accountdatabase.txt"
userFriendDatabasePath="databases/user-friendsdatabase.txt"
userMessageDatabasePath="databases/user-messagedatabase.txt"
userFriendRequestDatabasePath="databases/user-friendrequestdatabase.txt"
numberOfUsers="databases/numberofuser.txt"

userDatabase={}
userAccountDatabase={}
userFriendDatabase={}
userMessagesDatabase={}
userFriendRequestDatabase=[]
usersentFriendRequestDatabase=[]

residualuserMessagesDatabase=[]
residualuserFriendRequestDatabase=[]

user=""
email=""

#THe formatter of the string that inputs the line and the type of split
def lineformatter(line, split):
    if line[-1]=='\n':
        return decryption(line[:-1]).split(split)
    else:
        return decryption(line).split(split)

#Adding random friends if they don have friends yet


def randomfriends():
    print("People you may know")
    friendrequest=random.choices(list(userAccountDatabase.keys()), k=5)
    
    counter=1
    for friendr in friendrequest:
        print(f"[{counter}] {userAccountDatabase[friendr]['Name']}")
        counter+=1
    
    choice=ch(1,5)-1

    print(f"Succesfully sent a friend request to {userAccountDatabase[friendrequest[choice]]['Name']}")

    userid=friendrequest.pop(choice)
    residualuserFriendRequestDatabase.append("{},{}".format(userid, user))

#The function for entering a number
def ch(min, max):
    while True:
        chs=input("Enter a number: ")
        print()

        for letter in chs:

            if 48<= ord(letter)<=57:
                choice=int(chs)
                if min<=choice<=max:
                    return choice
                else:
                    if min == max:
                        print(f"Your input should be: {min}")
                    else:
                        print(f"Your input should be: {min}-{max}")
                    continue
            
            else:
                print("Please enter a number. Thank you!")
                break

#THe function that will directed the user to the Menuoption 2
def goBack():
    print("[1] Go back to Main Menu")

    choice= ch(1,1)

    if choice==1:
        secondMenu()

#The function that ask for the email
def askemail():
    while True:
        emails= input("Enter the email of your friend:").strip()
        print()

        if emails in userDatabase.keys():
            return emails
        else:
            print("Enter an email that also exist \n")

            print("[1] Try again")
            print("[2] Go back to Main Menu")

            choice=ch(1,2)

            if choice==1:
                continue
            else: 
                break

#The function of to chack each of the files if it exist
#if atlase one og the files does not exist, the program will not run
def checkAllFiles():
    #The checker of each path
    def filechecker(path):
        file_exists = exists(path)
        if file_exists:
            return True
        else:
            print(f"{path} is not in the file")
            return False

    udp=filechecker(userDatabasePath)
    uadp=filechecker(userAccountDatabasePath)
    ufd=filechecker(userFriendDatabasePath)
    umdp=filechecker(userMessageDatabasePath)
    ufrdp=filechecker(userFriendRequestDatabasePath)
    noup=filechecker(numberOfUsers)
    return udp and uadp and ufd and umdp and ufrdp and noup

#The function that will fenerate the userid
def userID():
    getnumber = open(numberOfUsers, "r")
    userID=""
    numberofusers=0

    for n in getnumber:
        number=lineformatter(n, ' ')[0]
        if len(number)  ==  1:
            userID  =  "00{}".format(number)
        elif len(number)==2:
            userID  =  "0{}".format(number)
        else:
            userID  =  "{}".format(number)

        x=int(number)
        numberofusers=x+1

    getnumber.close()

    newnumber = open(numberOfUsers, "w")
    newnumber.write(encryption(str(numberofusers)))
    newnumber.close()

    return userID

'''             for loading the datas from the files'''
#THe function that will load the userdatabase, userAccountDatabase and UserMessageDatabase
def loadUserInformation():
    userDB= open(userDatabasePath, "r")
    userAccount = open(userAccountDatabasePath, "r")
    userFriends = open(userFriendDatabasePath, "r")

    for line in userDB:
        data=lineformatter(line,",")
        userDatabase[data[0]]={}
        userDatabase[data[0]]["UserID"]=data[2]
        userDatabase[data[0]]["Password"]=data[1]

    #for userfriends
    for line in userFriends:
        data=lineformatter(line,",")
        userFriendDatabase[data[0]]=data[1:]

    #for userAccount
    for line in userAccount:
        data=lineformatter(line,"<#>")
        userAccountDatabase[data[0]]={}
        userAccountDatabase[data[0]]["Name"]=data[1]
        userAccountDatabase[data[0]]["Age"]=data[2]
        userAccountDatabase[data[0]]["Bio"]=data[3]

#The function that will load the userFriendRequestDatabase and userMessageDatabase
def loadNotification():
    userMessages= open(userMessageDatabasePath, "r")
    userFriendRequest=open(userFriendRequestDatabasePath, "r")

    #from the perpective of the user
    #to<#>from<#>message
    for line in userMessages:
        data=lineformatter(line,"<#>")

        if data[0]==user: 
            if data[1]  not in userMessagesDatabase.keys():
                userMessagesDatabase[data[1]]=[]
                userMessagesDatabase[data[1]].append("T{}".format(data[2]))
            else:
                userMessagesDatabase[data[1]].append("T{}".format(data[2]))
        elif data[1]==user:
            if data[0]  not in userMessagesDatabase.keys():
                userMessagesDatabase[data[0]]=[]
                userMessagesDatabase[data[0]].append("M{}".format(data[2]))
            else:
                userMessagesDatabase[data[0]].append("M{}".format(data[2]))
        else:
            residualuserMessagesDatabase.append("<#>".join(data))


    #to,from
    for line in userFriendRequest:
        data=lineformatter(line,",")

        if data[0]==user:
            userFriendRequestDatabase.append(data[1])
        elif data[1]==user:
            usersentFriendRequestDatabase.append(data[0])
        else:
            residualuserFriendRequestDatabase.append(",".join(data))
    

'''            for saving changes in the database '''

#THe function that sill save a database to the file
def saveDatabase(*databases):
    global user

    for DB in databases:
        if DB=="userDatabase":
            userDB= open(userDatabasePath, "w")
            for email in userDatabase.keys():
                userDB.write(encryption("{},{},{}".format(email,
                userDatabase[email]['Password'],userDatabase[email]['UserID']))+'\n')
            userDB.close()
        
        #for saving in account database
        elif DB=="userAccountDatabase":
            userAccount = open(userAccountDatabasePath, "w")
            for userid in userAccountDatabase.keys():
                userAccount.write(encryption("{}<#>{}<#>{}<#>{}".format(userid,
                userAccountDatabase[userid]['Name'],userAccountDatabase[userid]['Age']
                ,userAccountDatabase[userid]['Bio']))+'\n')
            userAccount.close()
            

        #saving the changes in userdatabase friends
        elif DB=="userFriendDatabase":
            userFriends = open(userFriendDatabasePath, "w")
            for line in userFriendDatabase.keys():
                data="{},".format(line)

                for y in userFriendDatabase[line]:
                    if y == userFriendDatabase[line][-1]:
                        data+=(f"{y}")
                    else:
                        data+=(f"{y},")

                userFriends.write(encryption("{}".format(data)+'\n'))
            
            userFriends.close()

        #saving inthe messages
        elif DB=="userMessages":
            userMessages= open(userMessageDatabasePath, "w")
            for userid in userMessagesDatabase.keys():
                for mess in userMessagesDatabase[userid]:
                    if mess[0]=="M":
                        userMessages.write(encryption("{}<#>{}<#>{}".format(userid,user,mess[1:]))+'\n')
                    else:
                        userMessages.write(encryption("{}<#>{}<#>{}".format(user,userid,mess[1:]))+'\n')
            for line in residualuserMessagesDatabase:
                userMessages.write(encryption(line)+'\n')
            
            userMessages.close()

        #saving the changes in friend requests
        else:
            userFriendRequest=open(userFriendRequestDatabasePath, "w")
            for userid in userFriendRequestDatabase:
                userFriendRequest.write(encryption("{},{}".format(user,userid))+'\n')
            for userid in usersentFriendRequestDatabase:
                userFriendRequest.write(encryption("{},{}".format(userid,user))+'\n')
            for line in residualuserFriendRequestDatabase:
                userFriendRequest.write(encryption(line)+'\n')
            userFriendRequest.close()

'''            The Loging-in/ creating an account'''
#THe function that will create the account for the user
def createAccount():
    userid=""
    print("== Create Account ==")
    while True:

        emails=input("Enter your email here: ")
        password=input("Enter your password here: ")
        repasspord=input("Enter your passsword again: ")
        
        #check if the user have already an account
        if emails in userDatabase.keys():
            print("The email you used already have an account")
            continue
        elif password!=repasspord:
            print("The password are not the same")
            continue
        else:
            userid=userID()
            userDatabase[emails]={}
            userDatabase[emails]['UserID']=userid
            userDatabase[emails]['Password']=password
            break

    #added info
    name=input("Enter your name here: ")
    age=input("Enter your age here: ")
    bio=input("Enter you Bio here: ")
    
    userAccountDatabase[userid]={}
    userAccountDatabase[userid]["Name"]=name
    userAccountDatabase[userid]["Age"]=age
    userAccountDatabase[userid]["Bio"]=bio

    userFriendDatabase[userid]=[]
    print("\nSuccessfully created an account")
    print("You can proceed in logging in\n")


    saveDatabase('userAccountDatabase', 'userFriendDatabase', 'userDatabase', 'UserFriendRequest')
    firstMenu()

#THe function for logging in.
def logIn():
    global user,email
    print("Login Account")

    while True:
        if len(userDatabase)!=0:
            name=input("Enter your email here: ").strip() 
            password=input("Enter your password here: ").strip() 

            if name in userDatabase and userDatabase[name]["Password"]==password:
                print("You have successfully logged in")
                user=userDatabase[name]["UserID"]
                email=name
                return True
            elif name in userDatabase and userDatabase[name]["Password"]!=password:
                print("your password is incorrect. Try again")
                continue
            else:
                print("Your email is not yet registered. Create an account first.")
                continue
        else:
            print("The database is empty")

#The funciton for the Menuoption 1 
def firstMenu():
    loadUserInformation()

    print("Welcome to PYsbook!\n")
    print("[1] Create Account")
    print("[2] Log in")
    print("[0] Exit")

    choice=ch(0,2)

    while True:
        if choice==1:
            createAccount()
            break
        elif choice==2:
            enter=logIn()

            if(enter==True): 
                loadNotification()
                secondMenu()
            break
        elif choice==0:
            print("Thank You for using PYsbook")
            break

#The function will count the unanswered messages
def Messagescounter():
    counter=0
    for userid in userMessagesDatabase.keys():
        if userMessagesDatabase[userid][-1][0]=="T":
            counter+=1
    
    return counter

'''                  Functions for the second menu            '''
#For viewing the Account name, email, age and bio of the user
def viewOwnProfile():
    print(f"Account name : {userAccountDatabase[user]['Name']}")
    print(f"Email        : {email}")
    print(f"Age          : {userAccountDatabase[user]['Age']}")
    print(f"Bio          : {userAccountDatabase[user]['Bio']}\n")

#For viewing a specific friend of the user
def viewFriends():
    #view a friend
    print("== View Freind ==")
    emails= askemail()
    friend=userDatabase[emails]["UserID"]
    if len(userFriendDatabase[user])!=0:
        if friend in userFriendDatabase[user]:
            
            print(f"Name  : {userAccountDatabase[friend]['Name']} ")
            print(f"Email : {emails}")
            print(f"Age   : {userAccountDatabase[friend]['Age']}")
            print(f"Bio   : {userAccountDatabase[friend]['Bio']}\n")
        else:
            print("The email you have entered is not one of your friend")
    else:
        print("You don't currenly have friends")
        randomfriends()

#For changing the bio of the user 
def updateBio():
    #update bio
    print("== Update bio ==")
    print(f"Your current bio: {userAccountDatabase[user]['Bio']}")
    newbio=input("Enter new bio:")
    userAccountDatabase[user]['Bio']=newbio
    print("\nSuccessfully updated the bio")
    print(f"Your updated bio: {userAccountDatabase[user]['Bio']}\n")

#For changing the passwork
def updatePassword():
    print("== Update password ==")
    passw=userDatabase[email]['Password']
    Pass=input("Enter current password:")
    newPass=input("Enter new password:")
    renewpassword=input("Enter again your new password:")

    if Pass==passw and newPass==renewpassword and newPass!= passw:
        userDatabase[email]['Password']=newPass
        print("Successfully updated the Password")

    elif newPass==renewpassword and newPass== passw:
        print("The password you input is the same as your current password")
    else: 
        print("The password and the re-entered password is not the same")

#For viewing all of the friends
def viewAllFriends(listoffriends):
    #View all freinds
    counter2=1 #userFriendDatabase[user] 
    print("==  Friends  ==")

    if len(listoffriends)==0:
        print("You don't currently have friends\n")
        randomfriends()
        saveDatabase("userFriendRequest")
    else:
        for friend in listoffriends:
            print(f"[{counter2}] name: {userAccountDatabase[friend]['Name']}")
            counter2+=1
        
    print()

#for deleting a specific friend
def deleteFriend():

    #delete a friend
    print("== Unfriend ==")
    emails =askemail()
    friend=userDatabase[emails]["UserID"]

    if len(userFriendDatabase[user])!=0:
        if friend in userFriendDatabase[user]:
            friend=userDatabase[emails]["UserID"]
            print(f"Deleted: {userAccountDatabase[friend]['Name']}")
            userFriendDatabase[user].remove(friend)
            userFriendDatabase[friend].remove(user)
        else: 
            print("The email that you have entered is not your friend")
    else:
        print("You don't currently have friends to delete")
    print()

    viewAllFriends(userFriendDatabase[user])

#For deleting all of the friends
def deleteAllFriend():
    global email
    #delete a friend
    print("== Unfriend All ==")

    print("Do you want to delete all of your friend")
    print("[1] Yes")
    print("[2] No")

    choice=ch(1,2)
    
    if choice==1:
        password= input("Enter your password: ")
        if password == userDatabase[email]['Password']:
            userFriendDatabase[user]=[]
            print("Deleted all friends")
            viewAllFriends(userFriendDatabase[user])
        else:
            print("incorrect password")
    
    

#for adding a friend to the friend request form the there mutual freinds
def addfriends():
    print("== Add Friends == ")

    mutualFriendList=[]
    counter=1

    print("Mutual friends")
    for x in userFriendDatabase[user]:
        for mutuals in userFriendDatabase[x]:
            if mutuals!=user and mutuals not in mutualFriendList and mutuals not in usersentFriendRequestDatabase:
                mutualFriendList.append(mutuals)
                print(f"[{counter}] {userAccountDatabase[mutuals]['Name'] }")
                counter+=1

    #jorgb@yahoo.com
    print()
    print("[1] Enter using the Email")
    print("[2] Enter using the list")
    choice=ch(1,2)

    if choice==1:
        email= askemail()
        userid= userDatabase[email]["UserID"]
        if (userid in mutualFriendList):
            mutualFriendList.remove(userid)
            print(f"Sent a friend request to: {userAccountDatabase[userid]['Name']}\n")
            usersentFriendRequestDatabase.append(userid)
        else:
            print("Enter an email that is your mutual friend list")
    else:
        choicef=ch(1, len(mutualFriendList))-1 
        userid=mutualFriendList.pop(choicef)
        print(f"Sent a friend request to: {userAccountDatabase[userid]['Name']}\n")
        usersentFriendRequestDatabase.append(userid )

# for messaging the other friend of the user
def message():

    print("== Message ==")
    
    while True:
        print("[1] Respond to a message")
        print("[2] New message from a friend list")
        print("[3] Delete message")
        print("[4] Go back")
        
        useridMessages=[]
        choice=ch(1,4)

        #the code in responding a message
        if choice==1:

            count=1
            #print the 
            for userid in userMessagesDatabase.keys():
                useridMessages.append(userid)
                if userMessagesDatabase[userid][-1][0]=="M":
                    print(f"[{count}] {userAccountDatabase[userid]['Name']}| You:{userMessagesDatabase[userid][-1][1:]}")
                else:
                    print(f"[{count}] {userAccountDatabase[userid]['Name']}| {userMessagesDatabase[userid][-1][1:]}")
                count+=1

            choice1=ch(1, len(useridMessages))-1
            print(f"\nConversation with {userAccountDatabase[useridMessages[choice1]]['Name']}")

            #print the converssation
            for convo in userMessagesDatabase[useridMessages[choice1]]:
                if convo[0]=="M":
                    print(f"You:{convo[1:]}")
                else:
                    print(f"{userAccountDatabase[useridMessages[choice1]]['Name']}: {convo[1:]}")
                count+=1

            print()
            print(f"Message: {userAccountDatabase[useridMessages[choice1]]['Name']}")

            print("[1] Send a message")
            print("[0] Go back")
            choice=ch(0,1)
            if choice==1:
                mess= input("Enter your message here:")
                userMessagesDatabase[useridMessages[choice1]].append("M{}".format(mess))
                print("Message successfully sent")
                print()
            else:
                continue
            continue
            
        #For creating a new message
        elif choice==2:
            viewAllFriends(userFriendDatabase[user])
            flist=userFriendDatabase[user]

            choice2=ch(1,len(flist))-1
            
            print(f"Send a message to {userAccountDatabase[flist[choice2]]['Name']}")
            mess= input("Enter your message here:")
            if flist[choice2] in userMessagesDatabase:
                userMessagesDatabase[flist[choice2]].append("M{}".format(mess))
                print(f"Successfully sent a message to {userAccountDatabase[flist[choice2]]['Name']}")
            else:
                userMessagesDatabase[flist[choice2]]=[]
                userMessagesDatabase[flist[choice2]].append("M{}".format(mess))
                print(f"Successfully sent a message to {userAccountDatabase[flist[choice2]]['Name']}")
            continue

        #For deleting a message that the user created
        elif choice==3:
            ownmess=[]
            count=1
            
            for convo in userMessagesDatabase.keys():
                index=0
                for mess in userMessagesDatabase[convo]:
                    if mess[0]=="M":

                        ownmess.append([convo, index])
                        print(f"[{count}] Sent to {userAccountDatabase[convo]['Name']}: {mess[1:]}")
                        count+=1
                    index+=1
            choice=ch(1,len(ownmess))-1

            for i,userid in enumerate(ownmess[choice]):
                userMessagesDatabase[userid].pop(ownmess[choice][1])
                print("Successfully removed the message\n")
                break

            continue

        else:
            break

#the function for adding, deleting friend requests  
def friendrequest():
    global userFriendRequestDatabase
    def printfriendrequest():
        print("Friend requests:")
        counter=1
        if len(userFriendRequestDatabase)==0: 
            print("You currently have no friend Requests")
            
        else:
            for request in userFriendRequestDatabase:
                print(f"[{counter}] {userAccountDatabase[request]['Name']}")
                counter+=1
    while True:
        print("== Friend Request ==") 
        printfriendrequest() 
        print("\n[1] accept friend request")
        print("[2] delete friend request")
        print("[3] delete all friend request")
        print("[4] Go back")
        #pick
        choice=ch(1,4)
        

        #adding a new friend
        if choice==1:
            add=ch(1,len(userFriendRequestDatabase))
            newf=userFriendRequestDatabase.pop(add-1)
            userFriendDatabase[user].append(newf)
            print(f"succefully added {userAccountDatabase[newf]['Name']}\n")
            continue

        #delete friend request
        elif choice==2:
            
            number=ch(1,len(userFriendRequestDatabase))
            deletef=userFriendRequestDatabase.pop(number-1)
            printfriendrequest()
            print(f"Successfully deleted {userAccountDatabase[deletef]['Name']}\n")
            continue

        #delete all friendrequest
        elif choice==3:
            
            print("\nDo you want to delete all of your friend")
            print("[1] Yes")
            print("[2] No")

            choice=ch(1,2)
            
            if choice==1:
                userFriendRequestDatabase=[]
                printfriendrequest()
                print("Deleted all friends\n")
                secondMenu()
            else:
                continue

        else:
            break

#The function for the Menuoption 2 or if the user successfully logged in
def secondMenu():
    global user, email 

    print("\nAccess services:")
    print("[1] View your own profile")
    print("[2] View Friends")
    print("[3] Update Bio")
    print("[4] Update Password")
    print("[5] View All Friends")
    print("[6] Delete a Friend")
    print("[7] Delete all Freinds ")
    print("[8] Add Friends")
    print(f"[9] Messages ({Messagescounter()})")
    print(f"[10] Friend Requests ({len(userFriendRequestDatabase)})\n")
    print("[0] Log out")

    choice= ch(0,10)

    if choice==1:
        viewOwnProfile()
        goBack()
    elif choice==2:
        viewFriends()
        goBack()
    elif choice==3:
        updateBio()
        saveDatabase("userAccountDatabase")
        goBack()
    elif choice==4:
        updatePassword()
        saveDatabase("userDatabase")
        goBack()
    elif choice==5:
        viewAllFriends(userFriendDatabase[user])
        goBack()
    elif choice==6:
        deleteFriend()
        saveDatabase("userFriendDatabase")
        goBack()
    elif choice==7:
        deleteAllFriend()
        saveDatabase("userFriendDatabase")
        goBack()
    elif choice==8:
        addfriends()
        saveDatabase("userFriendRequest")
        goBack()

    elif choice==9:
        message()
        saveDatabase("userMessages")
        goBack()
    elif choice==10:
        friendrequest()
        saveDatabase("userFriendDatabase","userFriendRequest")
        goBack()
    else:
        print("You have logged out\n")
        firstMenu()

#This whill check the files firss if exists or not
def preRun():
    if checkAllFiles()==True:
        firstMenu()
    else:
        print("Check all the files if it exist first before running")

preRun()
