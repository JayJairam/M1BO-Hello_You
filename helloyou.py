"# M1BO-Hello_You" 
import time
import winsound

def dead():
    winsound.PlaySound("deathscream.wav", winsound.SND_FILENAME)
    print("""
                            ____________
                      .~      ,   . ~.
                     /                \
                    /      /~\/~\   ,  \
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
""")
    print("you died!!!")
    time.sleep(3.0)
    print("HINT:wat is het tegenovergestelde van slapen.")






def award1():
    print("Je hebt het wezen verslagen")
    time.sleep(2.7)
    print("Je bent de meest rijkste barbaar ooit.")
    winsound.PlaySound("coin.wav", winsound.SND_FILENAME)
    print(""" 
                   ██████████                                                
                                ▓▓░░▓▓░░▒▒░░  ░░▓▓                                              
                            ████░░░░░░░░░░██████████                                            
                          ██░░░░░░░░██████░░░░░░░░░░██████                                      
                        ██░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░████                                  
                      ▓▓░░  ░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓░░▒▒▒▒██▓▓▓▓░░▓▓██                  
                    ▓▓░░░░░░░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░████░░  ░░░░  ░░░░▓▓▓▓              
                    ██░░░░░░░░░░░░████▒▒▒▒░░░░░░░░░░░░░░░░██    ░░░░░░░░░░░░░░░░░░██            
                    ░░▓▓░░▒▒▓▓░░░░░░░░██████▒▒▒▒░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓          
                        ██░░▒▒████░░░░  ░░  ██████▒▒▒▒██  ░░░░░░░░░░░░░░██████░░░░░░░░██        
                          ██░░▒▒▒▒████░░  ░░  ░░░░████░░░░░░░░░░░░░░████▒▒▒▒▒▒██░░░░░░██        
                            ██░░▒▒▒▒██░░░░████░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░██      
                              ██░░██░░░░░░██▒▒████░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██      
                                ████░░░░░░██▒▒▒▒▒▒████░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░██    
                                  ██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░██    
                              ████  ░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██    
                              ██  ░░░░  ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▓▓▒▒▒▒▒▒▒▒▒▒██░░░░██    
                              ██░░░░░░░░▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░██▒▒▒▒▓▓▒▒▒▒██░░░░██    
                              ██░░░░████  ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▒▒▒▒██░░░░██    
                                ████        ██░░████▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▒▒██░░░░██    
                                          ██████░░  ██████▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒██░░░░██    
                            ████    ██████░░▒▒▒▒▒▒░░░░░░░░██▒▒▒▒▒▒▒▒██░░░░░░░░░░████░░░░░░██    
                          ██  ░░████░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░██    
                      ████  ░░▒▒▒▒▒▒  ░░░░░░░░░░    ░░░░░░░░██▓▓▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░██      
                    ▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░▓▓████▒▒▒▒▓▓░░░░░░░░░░░░██      
              ████████▒▒▒▒▒▒▒▒▒▒░░░░░░  ░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒████████░░░░░░░░██        
            ▓▓░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒████░░░░░░▓▓▓▓▒▒░░██        
          ██  ░░░░░░██░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒██  ░░▒▒▒▒▒▒██          
          ██░░░░░░░░██▒▒░░▒▒░░▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒██░░░░░░▒▒██          
            ██░░░░░░██▒▒▒▒▒▒▓▓░░░░░░░░██████▒▒▒▒▒▒▒▒▒▒▒▒████░░░░▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██            
            ██░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░████████████░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██            
            ██░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒▓▓            
            ▓▓░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒▓▓            
            ██░░░░░░██▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒██░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██            
            ██░░░░░░██▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒██░░░░░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██            
            ██░░░░░░██▒▒▒▒▒▒▒▒██▒▒██▓▓▒▒▒▒██░░░░░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██            
          ██░░░░░░░░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒██░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░██          
          ██░░░░░░░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░▒▒▒▒██          
            ██░░░░░░░░░░░░██████▒▒▒▒▒▒▒▒▒▒██░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒████░░░░░░▒▒▒▒▒▒██            
              ██░░░░░░░░░░░░░░░░████▒▒▒▒▒▒██░░░░░░░░▒▒██▓▓▒▒▒▒████░░░░░░░░░░░░░░░░░░██          
            ▓▓░░░░░░██████░░░░░░░░░░████▒▒██░░░░░░░░▒▒██▓▓████░░░░░░░░░░████░░░░████            
              ████████    ▓▓██░░░░░░  ░░████░░░░░░░░▒▒████░░░░░░░░▓▓████    ████                
                              ████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓                              
                                    ████░░░░░░░░░░░░░░░░░░████                                  
                                        ▓▓▓▓░░░░░░░░▒▒▓▓▓▓                                      
                                        ██░░░░░░▒▒▒▒░░░░██                                      
                                          ████░░░░░░████                                        
                                              ██████                                            
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒░░░░▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒
""")
    print("END")






def award2():
    print("Je bent sterkste barbaar ooit geworden")
    time.sleep(2.7)
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠁⠀⠉⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⢀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣼⣰⢷⡤⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠉⣿⠈⢻⡀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢹⡀⠀⢷⡀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠘⣧⠀⢸⡇⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠶⠾⠿⢷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠘⣦⠀⣇⠀⠘⣿⣤⣶⡶⠶⠛⠛⠛⠛⠶⠶⣤⣾⠋⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠘⣦⣿⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡟⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠁⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⢰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠶⠛⠉⢀⣄⠀⠀⠀⢀⣿⠃⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⡶⠟⠋⠁⠀⠀⠀⣼⡇⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⣀⣀⣠⠿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⣀⣤⣤⣿⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⢻⡇⠀⠀⠀⠀⢠⣄⠀⢶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠟⠛⠋⠹⢿⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠘⢷⡄⠙⣧⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠁⠀⠀⠀⠀⠘⢸⡀⠀⠿⠀⠀⠀⣠⣤⣤⣄⣄⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⡀⠀⠀⠀⢸⡟⠻⣿⣦⡀⠀⠀⠀⠙⢾⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⣴⡏⠁⠀⠀⠹⣷⠀⠀⠀⠀⣠⡿⠋⠀⠀⠈⣷⠀⠀⠀⣾⠃⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠘⢷⣄⡀⣀⣠⣿⠀⠀⠀⠀⠻⣧⣄⣀⣠⣴⠿⠁⠀⢠⡟⠀⠀⠀⠀⠀⠙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡽⣦⡀⣀⠀⠀⠉⠉⠉⠉⠀⢀⣀⣀⡀⠀⠉⠉⠉⠁⠀⠀⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠃⠈⢿⣿⣧⣄⠀⠀⠰⣦⣀⣭⡿⣟⣍⣀⣿⠆⠀⠀⡀⣠⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣤⣽⣷⣤⣤⠀⠀⠀⠀⠀
⠀⢀⣿⡆⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⢀⣴⠖⠋⠁⠈⠻⣿⣿⣿⣶⣶⣤⡉⠉⠀⠈⠉⢉⣀⣤⣶⣶⣿⣿⣿⠃⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠉⠻⣷⣄⠀⠀⠀
⠀⣼⡏⣿⠀⢀⣤⠽⠖⠒⠒⠲⣤⣤⡾⠋⠀⠀⠀⠀⠀⠈⠈⠙⢿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⣀⣤⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⠀⠀
⢰⣿⠁⢹⠀⠈⠀⠀⠀⠀⠀⠀⠀⣿⠷⠦⠄⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⢀⣠⠶⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀
⣸⡇⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠉⠉⠛⠋⠉⠙⢧⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆
⣿⡇⠀⠀⠈⠆⠀⠀⣠⠟⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⠀⠀⠀⠀⠀⠀⠀⠈⠱⣄⣸⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡇
⢻⣧⠀⠀⠀⠀⠀⣸⣥⣄⡀⠀⠀⣾⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠂⠀⠀⠀⠀⠀⠀⣿⡇
⢸⣿⣦⠀⠀⠀⠚⠉⠀⠈⠉⠻⣾⣿⡏⢻⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣟⢘⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠐⡟⠀⠀⠀⠀⠀⠀⢀⣿⠁
⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣇⠈⠻⠷⠦⠤⣄⣀⣀⣀⣀⣠⣿⣿⣄⠀⠀⠀⠀⠀⣠⡾⠋⠄⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⣸⠟⠀
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣔⠢⠤⠤⠀⠀⠈⠉⠉⠉⢤⠀⠙⠓⠦⠤⣤⣼⠋⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀
⠀⢻⣷⣖⠦⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠈⢳⡀⠈⠛⢦⣀⡀⠀⠀⠘⢷⠀⠀⠀⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⣠⠏⠀⠀⠀⠀⣀⣴⡿⠋⠀⠀⠀
⠀⠀⠙⠻⣦⡀⠈⠛⠆⠀⠀⠀⣠⣤⡤⠀⠿⣤⣀⡙⠢⠀⠀⠈⠙⠃⣠⣤⠾⠓⠛⠛⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡴⠞⠁⢀⣠⣤⠖⢛⣿⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢷⣤⡁⠀⣴⠞⠁⠀⠀⠀⠀⠈⠙⠿⣷⣄⣀⣠⠶⠞⠋⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠞⠋⠁⠀⢀⣾⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣧⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣤⣀⣀⠀⠀⠈⠂⢀⣤⠾⠋⠀⠀⠀⠀⠀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⢀⣠⠎⣠⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⣦⠀⠀⠀⠀⠀⠀⠀⣿⣇⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢐⣯⣶⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣄⠸⣆⠀⠀⠲⣆⠀⠀⢸⣿⣶⣮⣉⡙⠓⠒⠒⠒⠒⠒⠈⠉⠁⠀⠀⠀⠀⠀⢀⣶⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠷⠾⠷⣦⣾⠟⠻⠟⠛⠁⠀⠈⠛⠛⢿⣶⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⣨⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠛⠻⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print("END")
    winsound.PlaySound("strongend.wav", winsound.SND_FILENAME)






def award3():
    print("Met de artefact heb je de krachten van thor geerfd")
    time.sleep(5.0)
    print("""
    ░░          ░░                ░░                        ░░                        ░░    
░░          ░░      ░░        ░░                                        ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░                ░░      ░░░░░░░░░░░░░░    ░░                        ░░    
░░          ░░  ████████████████████████████████████████████████████████▒▒        ░░    
░░          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████      ░░    
░░        ██░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    ░░    
░░░░░░  ░░▓▓▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░      ██░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░▒▒░░░░░░░░▒▒▒▒░░▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒░░██  ░░    
░░      ██░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░██  ░░    
░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██░░░░░░░░
░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░      ██░░▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  ░░    
░░░░░░░░██░░▒▒░░░░░░░░░░░░░░░░▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░██░░░░  ░░
░░░░░░░░██░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒▒░░░░██░░░░░░░░
░░░░    ██░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░██  ░░    
░░        ██░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░██    ░░    
░░          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██      ░░    
░░          ░░  ████████████████████████████████████████████████████████▒▒        ░░    
░░░░░░░░░░░░░░░░░░░░▒▒  ░░░░░░▒▒░░░░░░██▓▓▓▓▓▓██▓▓██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░      ██▓▓▓▓▓▓▓▓▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░                        ░░    
░░          ░░      ░░        ░░      ██░░▓▓▓▓▓▓░░██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██    ░░                        ░░    
░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░  ██▓▓░░▓▓▒▒▓▓██░░░░░░  ░░░░  ░░░░░░░░░░░░░░░░░░░░  
░░          ░░                ░░      ██▓▓▓▓░░▓▓▓▓██    ░░                        ░░    
░░          ░░                ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░                        ░░    
░░          ░░      ░░        ░░      ██░░▓▓▓▓▓▓░░██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██                    ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓░░▓▓░░▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
░░          ░░      ░░        ░░      ██▓▓▓▓░░▓▓▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░                        ░░    
░░          ░░                ░░      ██░░▓▓▓▓▓▓░░██    ░░                        ░░    
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ██▓▓▓▓░░▓▓▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░              ░░        ░░    
            ░░      ░░        ░░      ██░░▓▓▓▓▓▓░░██    ░░              ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ██░░▓▓▓▓▓▓▒▒██░░░░░░░░░░  ░░  ░░░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ██▓▓▓▓░░▓▓▓▓██  ░░░░                        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░                        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░      ░░        ░░      ██░░▓▓▓▓▓▓░░██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ██▓▓▓▓░░▓▓▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░              ░░        ░░    
░░░░░░░░░░░░░░    ░░░░░░  ░░  ░░  ░░  ▒▒▓▓▓▓▓▓▓▓▓▓▒▒  ░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░  
            ░░                ░░      ██░░▓▓▓▓▓▓░░██                                    
░░          ░░      ░░        ░░      ██▓▓░░▓▓░░▓▓██    ░░                        ░░    
░░          ░░      ░░        ░░      ██▓▓▓▓░░▓▓▓▓██    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ░░▓▓▓▓▓▓▓▓▓▓░░    ░░                        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░      ░░        ░░      ██░░▓▓▓▓▓▓░░██    ░░              ░░        ░░    
░░          ░░                ░░      ░░▒▒░░▓▓░░▒▒░░    ░░                        ░░    
░░          ░░      ░░        ░░      ░░▒▒▓▓░░▒▒▒▒░░    ░░              ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░      ░░▓▓▒▒▒▒▓▓▒▒░░  ░░░░              ░░        ░░    
░░          ░░                ░░      ░░░░▒▒▒▒▒▒░░░░    ░░                        ░░    
░░          ░░                ░░      ▓▓░░░░░░░░░░▓▓    ░░                        ░░    
░░          ░░      ░░        ░░      ▓▓          ▓▓    ░░              ░░        ░░    
░░░░░░░░░░░░░░░░░░  ░░    ░░░░░░    ░░▓▓░░░░  ░░  ▓▓░░░░░░    ░░░░  ░░░░░░░░    ░░░░░░░░
            ░░      ░░        ░░      ▓▓          ▓▓    ░░              ░░        ░░    
░░          ░░      ░░        ░░      ▓▓          ▓▓    ░░              ░░        ░░    
░░          ░░      ░░        ░░        ▓▓          ▓▓  ░░              ░░        ░░    
░░          ░░      ░░        ░░        ▓▓          ▓▓  ░░              ░░        ░░    
░░          ░░      ░░        ░░        ▓▓          ▓▓  ░░              ░░        ░░    
░░          ░░      ░░        ░░          ▓▓          ▓▓▒▒                        ░░    
░░          ░░      ░░        ░░          ▓▓          ▓▓▒▒              ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░▓▓░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░          ▓▓          ▓▓▒▒                        ░░    
░░░░░░  ░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░      ▓▓▒▒░░░░░░░░    ░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░            ▓▓          ▒▒▓▓                      ░░    
░░          ░░                ░░            ▓▓          ▒▒▓▓            ░░        ░░    
░░          ░░      ░░        ░░            ▓▓          ▒▒▓▓            ░░        ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░                ░░              ▓▓        ░░  ▓▓                    ░░    
░░          ░░                ░░              ▓▓        ░░  ▓▓          ░░        ░░    
░░          ░░                ░░              ▓▓        ░░  ▓▓                    ░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░      ░░        ░░              ░░▓▓      ░░    ▓▓        ░░        ░░    
░░          ░░                ░░                ▓▓            ▓▓                  ░░    
░░          ░░                ░░                ▓▓      ░░    ▓▓                  ░░    
░░          ░░      ░░        ░░      ░░          ▓▓    ░░  ▓▓          ░░        ░░    
░░          ░░                ░░                    ▓▓▓▓▓▓▓▓            ░░        ░░    
░░          ░░      ░░        ░░                        ░░              ░░        ░░    
""")
    print("END")
    winsound.PlaySound("thor.wav", winsound.SND_FILENAME)






def barbaar():
    print("""
                            .-'`-.
                               /  | | \
                              /   | |  \
                             |  __|_|___|
                             |' |||
                             |(   _L   ||
                             \|`-'__`-'|'
                              |  `--'  |
                             _|        |-.
                         .-'| |  \     /  `-.
                        /   | |\     .'      `-.
                       /    | | `''''           \
                      J     | |             _____|
                      |  |  J J         .-'   ___ `-.
                      |  \   L L      .'  .-'  |  `-.`.
                      | \|   | |     /  .'|    |    |\ \
                      |  |   J J   .' .'  |    |    | \ \
                      |  |    L L J  /    |    |    |  \ L
                     /   |     \ \F J|    |    |    |   LJ
                     |   |      \J F | () | () | () | ()| L
                    J  \ |       FJ  |    |  / _`-. |   J |
                    |    |      J |  |    | //    \ |   J |
                   J     |\     | |  |    ||:(     ||   J |
                   |     | `----| |  |    ||::`._.:||   | F
                   |     /\_    | |  |    ||:::::::F|   | F
                   |    |  /`---| |  |    | \:::::/ |   FJ
                   F    |  / |  J |  |    |  `-:-'  |  J F
                  J_.--/  /  |  J J  | () | () | () |()FJ
                   |  |    /     L L |    |    |    | / F
                   |  |     |    \ \ |    |    |    |/ /
                 |`-. |    |     |\ \|    |    |    / /
                 J'\ \|    |     | `.`.   |    |  .'.'
                / .'> |    |     |  `-.`-.|____.-'.'
              .' /::'_|    |/    |    `-.______.-'
             / .::/   \    |     |           |  |
           .' /::'     |--._     |           |--|
          / .::/       |    `-.__|     ____.-|//|
        .' /::'        |        F `--'      ||< |
       / .::/          |       J   |        FL\\|
     .' /::'           )       |   |        F| >|
    / .::/            (        \   |        F|//|
  .' /::'              \       /   |        F|--|
 / .::/                 |` `' '(   (      ' J|  |
| /::'                  |  | ` \   \  `    / J  |
|_:/                    |  | | |    |`-  ''F J  J
                        |    ' F    |   "" |  `-'
                        |     J     |      |
                        |     /     |      |
                        |   .'      |      F
                       /---'(       J     J
                     .'     \        L    |
                  .-'        )       L    F
                .'       .---'       \__.-'
 VK            (       .'             L   |
                `-----'               |   \
                                      J    \
                                       L    L
                                       |    F
                                       `-.-'
""")






def computer():
    print("""
     .__________________________.
    | .___________________. |==|
    | |     STARTING GAME ][-==-
    | |                   | |  |
    | |                   | |  |
    | |                   | |  |
    | |                   | |  |
    | |                   | |  |
    | | ]                 | | ,|
    | !___________________! |(c|
    !_______________________!__!
    |    ___ -=      ___ -= | ,|
    | ---[_]---   ---[_]--- |(c|

    !_______________________!__!
   /                            \
  /  [][][][][][][][][][][][][]  \
 /  [][][][][][][][][][][][][][]  \
(  [][][][][____________][][][][]  )
 \ ------------------------------ /
  \______________________________/
  """)     






def easteregg():
    print("wow je bent wakker geworden uit je droom.")
    winsound.PlaySound("wekker.wav", winsound.SND_FILENAME)
    print("Je moeder roept je om klaar te maken voor school")
    print("Daarin tegen heb je geen zin om naar school te gaan, jij komt met het idee om je ziek te melden wat ga je doen")
    for i in range(5):
        choice = input()
        if choice == 'naar school gaan':
            print("Je ging naar school en had een saaie dag.")
            time.sleep(3.0)
            print("END")
        elif choice == 'ziek melden':
            print("Je bleeft thuis en starte the game THE Barbarian op en speelde de spel.")          
            winsound.PlaySound("startup.wav", winsound.SND_FILENAME)
            computer()
            time.sleep(4.0)
            intro()
            break
        else:
            print("kiez uit ziek melden of naar school gaan.")     





def intro():
    print("Jij bent een barbaar met de meest sterksten krachten maar die krachten heb je niet zomaar gekregen, je hebt ze gekregen van een tovenaar genaamd Skeletor.")
    time.sleep(3.0)
    print("De tovenaar geeft je dagelijkse questen op om je krachten te behouden.")
    time.sleep(3.0)
    print("Doe je dat niet dan verlies je je krachten en verwoest de tovenaar je thuisland.")
    time.sleep(3.0)
    print("De tovenaar geeft je drie keuzen om drie verschillenden questen te doen. Je kan kiezen tussen de CAVES, de DUNGOUN of de FOREST.")
    print("Kiez uit caves, dungoun, forest")




def caves2():
    print("mine de daimonds en word de rijkste barbaar ooit of je pakt het hoofd van het monster en word de sterkste barbaar ooit.")
    for i in range(5):
        choice = input()
        if choice == 'diamonds':
            award1()
        elif choice == 'hoofd meenemen':
            award2()
        else:
            print("kiez uit daimonds of hoofd meenemen")




def caves():
    print("Je komt bij de gevaarlijke Caves aan, genaamd dodelijke grotten.")
    time.sleep(2.7)
    print("Daar moest je diamonds halen of het hoofd van de monster voor de tovenaar.")
    time.sleep(2.7)
    winsound.PlaySound("monster.wav", winsound.SND_FILENAME)
    print("Je ziet de daimonds maar daarnaast zie je een grote monster genaamd roadhog.")
    print("wat ga je doen, ga je voor de daimonds of val je de monster aan")
    
    for i in range(5):
        choice = input()
        if choice == 'daimonds':
            dead()
            break
        elif choice == 'val monster aan':
            print("hoera je hebt de monster verslagen")
            time.sleep(2.8)
            caves2()
            break
        else:
            print("kiez uit val monster aan of daimonds")




def dungoun2():
    print("Nu kan je kiezen om de kist te pakken of om de kop te pakken van de draak")
    for i in range(5):
        choice = input()
        if choice == 'pak kist':
            award1()
        elif choice == 'pak kop':
            award2()
        else:
            print("kiez uit pak kist of pak kop.")




def dungoun():
    print("Je komt bij de dungoun aan waar vele barbaren zijn gesneuveld. Hier moest je een schatkist vinden vol met goud of je moet de titanen draak verslaan.")
    time.sleep(2.8)
    print("Je ziet de kist vol met goud liggen en een grot verder op zie de draak slapen.")
    time.sleep(3.0)
    print("wat ga je doen? Pak je de kist of versla je de draak")

    for i in range(5):
        choice = input()
        if choice == 'pak kist':
            print("Je pakt de schatkist en opeens laat je een gouden munt vallen hiermee heb je de draak wakker gemaakt en eet je op")
            winsound.PlaySound("dragonscream.wav", winsound.SND_FILENAME)
            dead()
        elif choice == 'versla draak':
            print("Je hebt de draak met moeite verslagen")
            dungoun2()
        else:
            print("kiez uit pak kist of versla draak")




def forest2():
    print("Je gaat verder in de graveyard en ziet het goud wat je zocht")
    time.sleep(3.0)
    print("maar daarnaast zie je een glinsterende artefact, deze artefact kan je nieuwe super powers te krijgen.")
    print("wat ga je meenemen het goud of de artefact")
    for i in range(5):
        choice = input()
        if choice == 'goud meenemen':
            award1()
        elif choice == 'artefact meenemen':
            award3()
        else:
            print("kiez uit goud meenemen of artefact meenemen.")
        



def forest():
    print("Je gaat naar het meest verdoemde bos ooit en je doel is om de artefact te vinden of om het goud te vinden.")
    time.sleep(2.8)
    print("Zodra je het bos inkomt zie een groot skelleton met een zwaard en je ziet een pad met enter graveyard.")
    time.sleep(2.7)
    print("Wat ga je doen versla je de skelleton of enter graveyard")
    for i in range(5):
        choice = input()
        if choice == 'enter graveyard':
            print("Je enterd de graveyard, je bent langs grote skelleton lang gelopen opeens valt er iets uit je zak de grote skeleton hoort het en valt jouw aan, de skeleton is te sterk voor jouw en verslaat jouw.")
            time.sleep(4.0)
            dead()
        elif choice == 'versla skelleton':
            print("Je gaat met volle moed de strijd aan tegen de skelleton de skelleton ziet jouw en valt als eerst aan en mist zijn slag, hij slaat toe en verslaat de skelleton.")
            time.sleep(4.0)
            forest2()
        else:
            print("kiez uit versla skelleton of enter graveyard")




intro()
for i in range(5):
    choice = input() 
    if choice == 'caves':
        winsound.PlaySound("introsound.wav", winsound.SND_FILENAME)
        barbaar()
        caves()
    elif choice == 'dungoun':
        winsound.PlaySound("introsound.wav", winsound.SND_FILENAME)
        barbaar()
        dungoun()
    elif choice == 'forest':
        winsound.PlaySound("introsound.wav", winsound.SND_FILENAME)
        barbaar()
        forest()
    elif choice == 'WAKE-UP':
        easteregg()
    else:
        print("kiez uit dungoun, caves of forest") 