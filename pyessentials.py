from sys import platform
from sys import argv as arg
from sys import exit as getout
from subprocess import run
from subprocess import CalledProcessError

# Cambiar link por el del repositorio

banner = '''
88""Yb Yb  dP 888888 .dP"Y8 .dP"Y8 888888 88b 88 888888 88    db    88     .dP"Y8 
88__dP  YbdP  88__   `Ybo." `Ybo." 88__   88Yb88   88   88   dPYb   88     `Ybo." 
88"""    8P   88""   o.`Y8b o.`Y8b 88""   88 Y88   88   88  dP__Yb  88  .o o.`Y8b 
88      dP    888888 8bodP' 8bodP' 888888 88  Y8   88   88 dP""""Yb 88ood8 8bodP' 
'''

class pyessentials:
    def __init__(self, argument = "Null"):
        self.argument = argument
        self.os = platform

    def link(self, text, url):
        link_s = "\033]8;;" # Start a sequence in the OS, the 8 means that the sequence is a LINK
        delimiter = "\033\\" # Tell to the terminal that the following text will be visible
        link_e = "\033]8;;\033\\" # Tells the terminal that the sequence have already ended
        blue = "\033[34m" # Tells the terminal to output text in blue
        reset = "\033[0m" # Reset the terminal output color
        color = f"{blue}{text}{reset}"

        return f"{link_s}{url}{delimiter}{color}{link_e}"

    def space(self, spaces):
        for i in range(spaces):
            print("")

    def OS_CHECK(self):
        if self.os == "win32": # Every Windows
            return "pip"
        elif self.os == "linux" or self.os == "darwin": # Every Linux
            return "pip3"

    def main(self):
        self.space(4)
        print(banner)
        self.space(4)
        if self.argument != "Null":
            if self.argument not in ["-A", "-a", "-b", "-B", "-d", "-D", "-V", "-o", "-f", "-I", "-i", "-s", "-p", "-v", "-w", "-S", "-h"]:
                print("Choose a valid argument, or instead, use -h to see every argument")
            else:
                pip = self.OS_CHECK()
                if self.argument == "-A": # All-In
                    lista = ["openpyxl", "pypdf", "python-docx", "playwright", "selenium", "netmiko", "paramiko", "keyboard", "mouse", "psutil", "pyautogui", "pynput", "schedule", "watchdog", # Automation
                    "opencv-python", "alright", "discord.py", "python-telegram-bot", "pywhatkit", "twitchio", "praw", "tweepy",] #Bots
                    run([pip, "install", *lista])
                    getout()
                elif self.argument == "-a": # Automation
                    lista = ["openpyxl", "pypdf", "python-docx", "playwright", "selenium", "netmiko", "paramiko", "keyboard", "mouse", "psutil", "pyautogui", "pynput", "schedule", "watchdog"]
                    run([pip, "install", *lista])
                    getout()
                elif self.argument == "-b": # Big Data
                    print("Work In Progress")
                    getout()
                elif self.argument == "-B": # Bots
                    lista = ["opencv-python", "alright", "discord.py", "python-telegram-bot", "pywhatkit", "twitchio", "praw", "tweepy"]
                    run([pip, "install", *lista])
                    getout()
                elif self.argument == "-d": # Data Science
                    print("Work In Progress")
                    getout()
                elif self.argument == "-D": # Desktop Apps
                    print("Work In Progress")
                    getout()
                elif self.argument == "-V": # Data Visualization
                    print("Work In Progress")
                    getout()
                elif self.argument == "-o": # DevOPS
                    print("Work In Progress")
                    getout()
                elif self.argument == "-f": # Fin Tech
                    print("Work In Progress")
                    getout()
                elif self.argument == "-I": # IA/AI
                    print("Work In Progress")
                    getout()
                elif self.argument == "-i": # IoT
                    print("Work In Progress")
                    getout()
                elif self.argument == "-s": # System Administration
                    print("Work In Progress")
                    getout()
                elif self.argument == "-p": # Phone Apps
                    print("Work In Progress")
                    getout()
                elif self.argument == "-v": # Videogames
                    print("Work In Progress")
                    getout()
                elif self.argument == "-w": # Web Development (Back End)
                    print("Work In Progress")
                    getout()
                elif self.argument == "-S": # Web Scraping
                    print("Work In Progress")
                    getout()
                elif self.argument == "-h": # HELP
                    print("All, AI, Automation, Big Data, Bots, Data Science, Desktop Apps, Data Visualization, DevOPS, FinTech, IoT, System Administration, Phone apps, Videogames, Web Development (Back-End), Web Scrapping")
                    print("pyessentials - python meta-installer")
                    if self.os == "win32":
                        print("Usage: python pyessentials [Argument] [Breaker]")
                    else:
                        print("Usage: python3 pyessentials [Argument] [Breaker]")
                    print("Available Arguments:")
                    print("  -A - All-In : install every Api/Library of every category")
                    print("  -a - Automation : Writing scripts to perform repetitive computer tasks automatically, such as organizing files, etc...")
                    print("  -b - Big Data : Processing and analyzing massive volumes of data that are too large for traditional software")
                    print("  -B - Bots : Programs designed to run automated tasks over the internet by simulating human behavior, such as Discord bots")
                    print("  -d - Data Science : A field combining statistics and programming to analyze complex data, uncover hidden patterns, and help businesses make smart decisions.")
                    print("  -D - Desktop Apps : Developing traditional software programs that run directly on a computer's operating system")
                    print("  -V - Data Visualization : Turning raw numbers and datasets into interactive charts, graphs, and dashboards to make information easy to understand at a glance.")
                    print("  -o - DevOPS : Automating the bridge between writing code and running it on servers.")
                    print("  -f - FinTech : Building software for the financial sector, ranging from digital payment gateways and mobile banking to algorithmic stock trading.")
                    print("  -I - IA/AI : Developing systems capable of simulating human intelligence to learn, reason, solve complex problems, or generate content autonomously.")
                    print("  -i - IoT: Connecting everyday physical objects and devices to the internet.")
                    print("  -s - System Administration : Managing, configuring, and securing a company's servers and networks to ensure all digital infrastructure runs smoothly without downtime.")
                    print("  -p - Phone Apps : Designing and developing software applications tailored specifically to run on smartphones and tablets")
                    print("  -v - Videogames : Creating interactive entertainment software, covering everything from game logic and physics engines to enemy behavior.")
                    print("  -w - Web Development (Back-End) : Building the internal structure of websites, including servers, databases, and APIs essentially everything that happens behind the scenes.")
                    print("  -S - Web Scraping : Developing specialized software to automatically browse websites and extract data into a clean, structured format.")
                    getout()
        else:
            print("Welcome to pyessentials, a little installer that helps you to install every API/Library that you will need for the 'campus' of programming you want to learn.")
            print(f"\nChoose one of the following categories (If you want to know what it is in every category, look it here at it's {self.link("repo", "https://github.com/sotelodev2008/pyessentials")})")
            self.space(2)
            print("1. All\n2. Automation\n3. Big Data\n4. Bots\n5. Data Science\n6. Desktop Apps\n7. Data Visualization\n8. DevOPS\n9. FinTech\n10. IA/AI\n11. Iot\n12. System Administration\n13. Phone apps\n14. Videogames\n15. Web Development (Back-End)\n16.Web Scraping")
            try:
                opcion = int(input("choose an option: "))
            except ValueError:
                print("Do you know what is a number, it is a mathematical object used to count, measure, and label.")
            if opcion == 1:
                self.argument == "-A"
            elif opcion == 2:
                self.argument == "-a"
            elif opcion == 3:
                self.argument == "-b"
            elif opcion == 4:
                self.argument == "-B"
            elif opcion == 5:
                self.argument == "-d"
            elif opcion == 6:
                self.argument == "-D"
            elif opcion == 7:
                self.argument == "-V"
            elif opcion == 8:
                self.argument == "-o"
            elif opcion == 9:
                self.argument == "-f"
            elif opcion == 10:
                self.argument == "-I"
            elif opcion == 11:
                self.argument == "-i"
            elif opcion == 12:
                self.argument == "-s"
            elif opcion == 13:
                self.argument == "-p"
            elif opcion == 14:
                self.argument == "-v"
            elif opcion == 15:
                self.argument == "-w"
            elif opcion == 16:
                self.argument == "-S"
            else:
                print("Dude, I know there are too many options to choose, however, there are only 16, so, how in the actual fuck did you choose that?\nTry again")
                getout()
            self.main()

if len(arg) <= 1:
    sol = pyessentials()
elif len(arg) == 2:
    sol = pyessentials(arg[1])
else:
    print("Too much arguments")

try:
    sol.main()

except FileNotFoundError:
    print("\nYou don't have installed python/pip, or maybe you don't have it on path")
    getout()

except CalledProcessError as e:
    print(f"\nError during the installation, this is the error output {e.returncode}")
    getout()

except KeyboardInterrupt:
    print("\nInstallation Cancelled")

except Exception as e:
    print(f"\nUnexpected Error {e.returncode}")
