import random
import datetime
import platform
import time
import os

text = '''
                                                                                
                                       @&                       .@@@@   @@@@    
                                  @@@@%  @@*#@                  &%  (@ @,  @.   
        &@& &@&                (##&  %%  @(  @*                  @,  @/@,  @.   
   @( .@   @   @  *@         *@  #&  %%  @(  @*             &@@@@  @, @@,  @.   
   @   @   @   @   @         *@  #&  %%  @(  @*            #&  &#  @/ .@,  @.   
   @   @   @ @(*,,**@#       *@  #&  %%  @(  @*.(*         #&  &#  @/.@@@@@@#   
   @ %,@@.@@@*@,..  .@       *@              @#   .@*      #@&&@%  @/.@      @  
   @         &   #  %&       *@                 %@         #&    ,,    .*&%  @  
    @      @/     &@          @       @@      @#           .@       @&      @*  
     @     %     @             @%    /@    %@                @(    #%    @@     
     @           @             ,@          @,                (&          @      
      ./////////.               @&%%%%%%%%&@                  @&%%%%%%%%@@      
       #%%%%%%%*                  ((((((((                      ((((((((        

       STONE (0)                  PAPER (1)                    SCISSOR (2)      
To exit enter 'e'.                                                  
'''

def get_bot_reply():
    random.seed(int(datetime.datetime.now().timestamp())%100)
    bot_reply = random.randint(0, 2)
    return bot_reply

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    cnt = True
    player_score = 0
    bot_score = 0
    while cnt:
        clear_screen()
        print(f'Your Score: {player_score}', f'Bot Score: {bot_score}')
        print(text)
        player_reply = input('Enter your choice: ')
        if player_reply.isnumeric() and int(player_reply) in range(0, 3):
            player_reply = int(player_reply)
            bot_reply = get_bot_reply()
            clear_screen()
            if (player_reply == 0 and bot_reply == 1) or (player_reply == 1 and bot_reply == 2) or (player_reply == 2 and bot_reply == 0):
                print('Bot Wins')
                bot_score += 1
            elif player_reply == bot_reply:
                print('Draw')
            else:
                print('Player Wins')
                player_score += 1
            print(f'Your Score: {player_score}', f'Bot Score: {bot_score}')
            time.sleep(2)
        elif player_reply == 'e':
            cnt = False
            if player_score > bot_score:
                print('Player Wins!')
            elif player_score < bot_score:
                print('Bot Wins!')
            time.sleep(1)
        else:
            print('Invalid Input!')
            time.sleep(1)