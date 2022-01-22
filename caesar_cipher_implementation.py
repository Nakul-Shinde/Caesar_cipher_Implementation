logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)


def ceaser_cipher_encrypt(text,shift_number):
    list_text=[]
    new_list=[" "]*len(text)
    list_text[:0]=text
    #print(list_text)
    word_list=['a','b','c','d','e','f',
               'g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t',
               'u','v','w','x','y','z',
               'a','b','c','d','e','f',
               'g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t',
               'u','v','w','x','y','z' ]
    
   
    
    for i in range(0,len(list_text)):
            for j in range(0,len(word_list)):
                if list_text[i]==word_list[j]:
                    character=word_list[j+shift_number]
                    new_list[i]=character
                   # print(new_list[i])
                    break
                else:
                    new_list[i]=list_text[i]
                
    combined_list="".join(new_list)
                    
    print(combined_list)  
    

def ceaser_cipher_decrypt(text,shift_number):
    list_text=[]
    new_list=[" "]*len(text)
    list_text[:0]=text
    #print(list_text)
    word_list=['a','b','c','d','e','f',
               'g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t',
               'u','v','w','x','y','z',
               'a','b','c','d','e','f',
               'g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t',
               'u','v','w','x','y','z' ]


    
    for i in range(0,len(list_text)):
            for j in range(0,len(word_list)):
                if list_text[i]==word_list[j]:
                    character=word_list[j-shift_number]
                    new_list[i]=character
                   # print(new_list[i])
                    break
                else:
                    new_list[i]=list_text[i]
                
    combined_list="".join(new_list)
                    
    print(combined_list) 


print("Welcome to caeser cipher")

conti='y'

while(conti=='y'):
    user_choice=input("Please type 'encrypt' for encryption or 'decrypt'for decryption:")    
    
    if user_choice=='encrypt':
        enter_text=input("Please enter your Text:\t").lower()
        shift_number=int(input("Please enter your shift number:\t")) 
        enter_shift_number=shift_number%26
        ceaser_cipher_encrypt(enter_text,enter_shift_number)
        conti=input("Do you want to continue?(y/n)")
        
    else:
        enter_text=input("Please enter your Text:\t").lower()
        shift_number=int(input("Please enter your shift number:\t")) 
        enter_shift_number=shift_number%26
        ceaser_cipher_encrypt(enter_text,enter_shift_number)
        conti=input("Do you want to continue?(y/n)")
    
    
       



