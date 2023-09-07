# Python Program which puts questions in Front of User and let them play till they give right answers...
import os
alive_in_game='y'
question_no=-1
questions=["Which is the coldest location in the earth?",
         "Which is the highest peak in India?",
         "Which is the continent with the most number of countries?",
         "Which is the fastest animal on land?",
         "Which is the first element on the periodic table of elements?",
         "Which is the largest state of India?",
         "Which is the hardest substance available on earth?",
         "The national river of India?",
         "Which is the hottest continent on Earth?",
         "Which is the instrument used to measure blood pressure?",
         "Which is the largest Democracy country in the world?",
         "Which animal is known as the Ship of the Desert”?",
         "Which is the largest bone in the human body?",
         "Which animal is known as the king of the jungle?",
         "Which is the largest freshwater lake in India?"]

# answers=["antartica","Kanchanjangha","Africa","Cheetah",
#          "Hydrogen","Rajasthan","Diamond","Ganga","Africa",
#          "Sphygmomanometer","India","Camel","femer","lion",
#          "Wular lake"]

print("Hello! Welcome to KBC... I'm your host and I will ask you questions and guide you through this journey..\n")
print("Instead of just replying with option number reply with typing entire option...\n")

while(alive_in_game=='y'):
    question_no=question_no+1
    match question_no:
        case 0:
            print("Here is your First question for 1000 INR")
            print(questions[question_no])
            print("a. Belgium\t b. Iceland\n c. antartica\t d. greenland")
            ans=str(input())
            os.system('cls')
            if(ans=='antartica'):
                won_amount=1000
                print("Right Answer! you have won 1000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
        case 1:
            print("Here is your second question for 2000 INR")
            print(questions[question_no])
            print("a. Nanda Devi\t b. kanchanjangha\n c. trisul\t d.anamudi")
            ans=str(input())
            os.system('cls')
            if(ans=='kanchanjangha'):
                won_amount=2000
                print("Right Answer! you have won 2000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
                
        case 2:
            print("Here is your third question for 3000 INR")
            print(questions[question_no])
            print("a. asia\t b. europe\n c. africa\t d.australia")
            ans=str(input())
            os.system('cls')
            if(ans=='africa'):
                won_amount=3000
                print("Right Answer! you have won 3000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
                
        case 3:
            print("Here is your fourth question for 5000 INR")
            print(questions[question_no])
            print("a. cheetah\t b. leapord\n c. tiger\t d.lion")
            ans=str(input())
            os.system('cls')
            if(ans=='cheetah'):
                won_amount=5000
                print("Right Answer! you have won 5000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
                
        case 4:
            print("Here is your fifth question for 10000 INR")
            print(questions[question_no])
            print("a. oxygen\t b. hydrogen\n c. neon\t d.Iron")
            ans=str(input())
            os.system('cls')
            if(ans=='hydrogen'):
                won_amount=10000
                print("Right Answer! you have won 10000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
                
        case 5:
            print("Here is your sixth question for 20000 INR")
            print(questions[question_no])
            print("a. uttar pradesh\t b. rajasthan\n c. haryana\t d.punjab")
            ans=str(input())
            os.system('cls')
            if(ans=='rajasthan'):
                won_amount=20000
                print("Right Answer! you have won 20000 INR...\n")
            else:
               print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
               alive_in_game='n'
                
        case 6:
            print("Here is your seventh question for 40000 INR")
            print(questions[question_no])
            print("a. Iron\t b. Platinum\n c. titanium\t d.Diamond")
            ans=str(input())
            os.system('cls')
            if(ans=='Diamond'):
                won_amount=40000
                print("Right Answer! you have won 40000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 7:
            print("Here is your Eighth question for 80000 INR")
            print(questions[question_no])
            print("a. ganga\t b. yamuna\n c. Brahmputra\t d. mandakini")
            ans=str(input())
            os.system('cls')
            if(ans=='ganga'):
                won_amount=80000
                print("Right Answer! you have won 80000 INR...\n")
            else:
               print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
               alive_in_game='n'
        case 8:
            print("Here is your Ninth question for 160000 INR")
            print(questions[question_no])
            print("a. asia\t b. europe\n c. south america\t d. africa")
            ans=str(input())
            os.system('cls')
            if(ans=='africa'):
                won_amount=160000
                print("Right Answer! you have won 160000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 9:
            print("Here is your tenth question for 320000 INR")
            print(questions[question_no])
            print("a. micrometer\t b. polygraph\n c. Sphygmomanometer\t d. accumulator")
            ans=str(input())
            os.system('cls')
            if(ans=='Sphygmomanometer'):
                won_amount=320000
                print("Right Answer! you have won 320000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 10:
            print("Here is your eleventh question for 640000 INR")
            print(questions[question_no])
            print("a. India\t b. USA\n c. Brazil\t d. China")
            ans=str(input())
            os.system('cls')
            if(ans=='India'):
                won_amount=640000
                print("Right Answer! you have won 640000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 11:
            print("Here is your Twelefth question for 1250000 INR")
            print(questions[question_no])
            print("a. yak\t b. goat\n c. camel\t d. ostritch")
            ans=str(input())
            os.system('cls')
            if(ans=='camel'):
                won_amount=1250000
                print("Right Answer! you have won 1250000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 12:
            print("Here is your Thirteenth question for 2500000 INR")
            print(questions[question_no])
            print("a. skull\t b. pelvis\n c. femur\t d. clavicle")
            ans=str(input())
            os.system('cls')
            if(ans=='femur'):
                won_amount=2500000
                print("Right Answer! you have won 2500000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 13:
            print("Here is your Thirteenth question for 5000000 INR")
            print(questions[question_no])
            print("a. tiger\t b. bear\n c. old yak\t d. lion")
            ans=str(input())
            os.system('cls')
            if(ans=='lion'):
                won_amount=5000000
                print("Right Answer! you have won 5000000 INR...\n")
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
        case 14:
            print("Here is your 1 crore INR question")
            print(questions[question_no])
            print("a. dal lake\t b. tsomogo cho\n c. wular lake\t d. loktak lake")
            ans=str(input())
            os.system('cls')
            if(ans=='wular lake'):
                won_amount=10000000
                print("Right Answer! you have won 10000000 INR...\n")
                alive_in_game='c'
            else:
                print("your answer was incorrect.... hence you are eliminated..\n however you won..", won_amount," INR")
                alive_in_game='n'
                
                
if(alive_in_game=='c'):
    print("ek croreeeeeeeeeeeeee!!!!!!!! \n Adbhut.... Adbhut...") 