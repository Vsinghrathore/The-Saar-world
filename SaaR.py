import os 
print("\n\t\t-------_______WELCOME TO THE SAAR WORLD_______------")

while True:
    
               print("""
               option 01: Run date command.
               option 02: Check IP .
               option 03: open calendar.
               option 04: open manual for calendar.
               option 05: To run browser.
               option 06: To open new terminal.
               option 07: To see the detailed information about your Linux              
               option 08: To check the disk space.
               Option 09: To open content of The-saar-world.
               Option 10: To Exit.
               \n
               """)
               choice = int(input("Which command you want to run Enter your choice :"))
               if choice == 1:
                     date = os.system("date")
                     print(date)
               elif choice == 2:
                     IP= os.system("ifconfig")
                     print(IP)
               elif choice == 3:
                     cal= os.system("cal")
                     print(cal)
               elif choice == 4:
                     mancal= os.system("man cal")
                     print(mancal)
               elif choice == 5:
                     firefox= os.system("firefox -p")
                     print(firefox)
               elif choice == 6:
                     newterminal= os.system("gnome-terminal")
                     print(newterminal)
               elif choice == 7:
                     uname= os.system("uname")
                     print(uname)
               elif choice == 8:
                     disk= os.system("du")
                     print(disk)
               elif choice == 9:
                     cat= os.system("cat The-saar-world.py")
                     print(cat)
               elif choice == 10:
                     exit= os.system("exit")
                     print(exit)
                     print("exit the program")
                     break
               else:
                     print("please enter the valid option")
      













