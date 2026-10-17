from sys import platform
from sys import argv as arg
from sys import exit as getout
from subprocess import run
from subprocess import CalledProcessError

# Cambiar link por el del repositorio

banner = '''
88""Yb Yb  dP 888888 .dP"Y8 .dP"Y8 888888 88b 88 888888 88    db    88     .dP"Y8 
88__dP  YbdP  88__   `Ybo." `Ybo." 88__   88Yb88   88   88   dPYb   88     `Ybo." 
88"""    8P   88""   o.`Y8b o.`Y8b 88""   88 Y88   88   88  dP__Yb  88  .o o.`Y8b 
88      dP    888888 8bodP' 8bodP' 888888 88  Y8   88   88 dP""""Yb 88ood8 8bodP' 
'''

class pyessentials:
    def __init__(self, argument="Null"):
        self.argument = argument
        self.os = platform

    # Cada categoría con su lista de librerías/APIs
    LIBRARIES = {
        "-a": ["openpyxl", "pypdf", "python-docx", "playwright", "selenium", "netmiko", "paramiko", "keyboard", "mouse", "psutil", "pyautogui", "pynput", "schedule", "watchdog"],  # Automation
        "-b": ["pyspark", "dask", "pandas", "polars", "pyarrow", "fastparquet", "duckdb", "vaex", "ray", "modin", "apache-beam", "apache-airflow", "luigi", "prefect", "dagster", "kafka-python", "confluent-kafka", "happybase", "cassandra-driver", "pyhive", "pymongo", "redis", "h5py", "tables", "zstandard", "petl", "findspark"],  # Big Data
        "-B": ["opencv-python", "alright", "discord.py", "python-telegram-bot", "pywhatkit", "twitchio", "praw", "tweepy"],  # Bots
        "-d": ["numpy", "pandas", "scipy", "scikit-learn", "statsmodels", "sympy", "xgboost", "lightgbm", "catboost", "imbalanced-learn", "jupyter", "jupyterlab", "notebook", "ipython", "ydata-profiling", "feature-engine", "shap", "lime", "nltk", "spacy", "gensim", "yellowbrick", "mlxtend", "missingno"],  # Data Science
        "-D": ["customtkinter", "dearpygui", "flet", "kivy", "PySide6", "wxPython"],  # Desktop Apps
        "-V": ["matplotlib", "seaborn", "plotly", "kaleido", "bokeh", "altair", "dash", "streamlit", "folium", "plotnine", "pygal", "holoviews", "hvplot", "panel", "geopandas", "graphviz", "networkx", "wordcloud", "missingno", "pydeck", "squarify", "mplfinance"],  # Data Visualization
        "-o": ["fabric", "ansible", "docker", "kubernetes", "boto3", "google-cloud-storage", "azure-mgmt-resource", "invoke", "pyyaml", "jinja2", "python-dotenv", "click", "typer", "rich", "loguru", "prometheus-client", "opentelemetry-api", "opentelemetry-sdk", "pytest", "tox", "nox", "pre-commit", "black", "flake8", "mypy", "pylint", "ruff", "coverage", "plumbum", "ansible-lint"],  # DevOPS
        "-f": ["yfinance", "pandas-datareader", "ccxt", "alpaca-py", "ib_insync", "backtrader", "zipline-reloaded", "pyfolio", "QuantLib", "ta", "pandas-ta", "finta", "stockstats", "yahooquery", "finnhub-python", "polygon-api-client", "stripe", "plaid-python", "paypalrestsdk", "braintree", "cryptofeed", "web3", "pycoingecko", "mplfinance"],  # FinTech
        "-I": ["tensorflow", "torch", "keras", "scikit-learn", "transformers", "datasets", "tokenizers", "accelerate", "sentence-transformers", "openai", "anthropic", "google-generativeai", "cohere", "langchain", "langgraph", "llama-index", "chromadb", "faiss-cpu", "pinecone-client", "sentencepiece", "nltk", "spacy", "gymnasium", "stable-baselines3", "pytorch-lightning", "jax", "flax", "diffusers", "ultralytics", "mediapipe", "openai-whisper", "SpeechRecognition", "pyttsx3", "pytesseract", "prophet", "mlflow", "wandb", "onnx", "onnxruntime", "peft", "trl", "pyautogen", "crewai"],  # IA/AI
        "-i": ["paho-mqtt", "aiomqtt", "pyserial", "pymodbus", "asyncua", "gpiozero", "RPi.GPIO", "adafruit-blinka", "board", "busio", "smbus2", "spidev", "esptool", "ampy", "mpremote", "python-kasa", "tuya-connector", "bleak", "bluepy", "influxdb-client", "pymongo", "coapthon3"],  # IoT
        "-s": ["paramiko", "fabric", "psutil", "distro", "netifaces", "python-crontab", "croniter", "schedule", "pyyaml", "jinja2", "ansible", "boto3", "docker", "kubernetes", "pyvmomi", "libvirt-python", "prometheus-client", "ldap3", "cryptography", "passlib", "bcrypt", "pyopenssl", "sshtunnel", "netaddr", "scapy", "dnspython", "whois", "speedtest-cli", "invoke", "plumbum"],  # System Administration
        "-p": ["kivy", "kivymd", "buildozer", "briefcase", "toga", "flet", "plyer", "pyjnius", "pyobjus", "python-for-android", "appium-python-client", "uiautomator2", "kivy-garden"],  # Phone Apps
        "-v": ["pygame", "pyglet", "arcade", "panda3d", "moderngl", "pyrr", "ursina", "PyOpenGL", "raylib", "pymunk", "Box2D", "pytmx", "pygame-menu", "pygame_gui", "tcod", "esper", "noise", "opensimplex", "pybullet", "harfang3d", "thorpy", "glfw"],  # Videogames
        "-w": ["flask", "django", "fastapi", "starlette", "uvicorn", "gunicorn", "hypercorn", "aiohttp", "tornado", "bottle", "pyramid", "sanic", "litestar", "quart", "sqlalchemy", "alembic", "pydantic", "databases", "asyncpg", "psycopg2-binary", "pymysql", "mysql-connector-python", "pymongo", "redis", "motor", "sqlmodel", "peewee", "tortoise-orm", "jinja2", "wtforms", "flask-login", "flask-sqlalchemy", "passlib", "bcrypt", "python-jose", "pyjwt", "celery", "rq", "httpx", "websockets", "graphene", "strawberry-graphql", "djangorestframework"],  # Web Development (Back-End)
        "-S": ["requests", "httpx", "beautifulsoup4", "lxml", "scrapy", "selenium", "playwright", "mechanicalsoup", "requests-html", "pyquery", "html5lib", "parsel", "w3lib", "fake-useragent", "cloudscraper", "aiohttp", "tqdm", "pandas", "cssselect", "selenium-wire", "undetected-chromedriver", "curl-cffi", "newspaper3k", "trafilatura", "readability-lxml"],  # Web Scraping
    }

    NAMES = {
        "-A": "All-In",
        "-a": "Automation",
        "-b": "Big Data",
        "-B": "Bots",
        "-d": "Data Science",
        "-D": "Desktop Apps",
        "-V": "Data Visualization",
        "-o": "DevOPS",
        "-f": "FinTech",
        "-I": "IA/AI",
        "-i": "IoT",
        "-s": "System Administration",
        "-p": "Phone Apps",
        "-v": "Videogames",
        "-w": "Web Development (Back-End)",
        "-S": "Web Scraping",
        "-h": "Help",
    }

    DESCRIPTIONS = {
        "-a": "Writing scripts to perform repetitive computer tasks automatically, such as organizing files, etc...",
        "-b": "Processing and analyzing massive volumes of data that are too large for traditional software",
        "-B": "Programs designed to run automated tasks over the internet by simulating human behavior, such as Discord bots",
        "-d": "A field combining statistics and programming to analyze complex data, uncover hidden patterns, and help businesses make smart decisions.",
        "-D": "Developing traditional software programs that run directly on a computer's operating system",
        "-V": "Turning raw numbers and datasets into interactive charts, graphs, and dashboards to make information easy to understand at a glance.",
        "-o": "Automating the bridge between writing code and running it on servers.",
        "-f": "Building software for the financial sector, ranging from digital payment gateways and mobile banking to algorithmic stock trading.",
        "-I": "Developing systems capable of simulating human intelligence to learn, reason, solve complex problems, or generate content autonomously.",
        "-i": "Connecting everyday physical objects and devices to the internet.",
        "-s": "Managing, configuring, and securing a company's servers and networks to ensure all digital infrastructure runs smoothly without downtime.",
        "-p": "Designing and developing software applications tailored specifically to run on smartphones and tablets",
        "-v": "Creating interactive entertainment software, covering everything from game logic and physics engines to enemy behavior.",
        "-w": "Building the internal structure of websites, including servers, databases, and APIs essentially everything that happens behind the scenes.",
        "-S": "Developing specialized software to automatically browse websites and extract data into a clean, structured format.",
    }

    def link(self, text, url):
        link_s = "\033]8;;"  # Start a sequence in the OS, the 8 means that the sequence is a LINK
        delimiter = "\033\\"  # Tell to the terminal that the following text will be visible
        link_e = "\033]8;;\033\\"  # Tells the terminal that the sequence have already ended
        blue = "\033[34m"  # Tells the terminal to output text in blue
        reset = "\033[0m"  # Reset the terminal output color
        color = f"{blue}{text}{reset}"

        return f"{link_s}{url}{delimiter}{color}{link_e}"

    def space(self, spaces):
        for i in range(spaces):
            print("")

    def OS_CHECK(self):
        if self.os == "win32":  # Every Windows
            return "pip"
        elif self.os == "linux" or self.os == "darwin":  # Every Linux / macOS
            return "pip3"
        return "pip"

    def help(self):
        print("All, AI, Automation, Big Data, Bots, Data Science, Desktop Apps, Data Visualization, DevOPS, FinTech, IoT, System Administration, Phone apps, Videogames, Web Development (Back-End), Web Scrapping")
        print("pyessentials - python meta-installer")
        if self.os == "win32":
            print("Usage: python pyessentials [Argument] [Breaker]")
        else:
            print("Usage: python3 pyessentials [Argument] [Breaker]")
        print("Available Arguments:")
        print("  -A - All-In : install every Api/Library of every category")
        for flag in ["-a", "-b", "-B", "-d", "-D", "-V", "-o", "-f", "-I", "-i", "-s", "-p", "-v", "-w", "-S"]:
            print(f"  {flag} - {self.NAMES[flag]} : {self.DESCRIPTIONS[flag]}")

    # --- NUEVO: instala una lista concreta y termina ---
    def install(self, lista, name=None):
        if not lista:
            print("\nThere is nothing to install, bye")
            getout()
        pip = self.OS_CHECK()
        etiqueta = f"'{name}' " if name else ""
        print(f"\nInstalling {etiqueta}({len(lista)} packages)...")
        self.space(1)
        run([pip, "install", *lista])
        getout()

    # --- NUEVO: sub-menú de una categoría para instalar librerías individuales ---
    def library_menu(self, flag):
        name = self.NAMES[flag]
        libs = self.LIBRARIES[flag]
        self.space(2)
        print(f"=== {name} ({len(libs)} available packages) ===")
        print("Pick the ones you want to install individually:\n")
        for i, lib in enumerate(libs, 1):
            print(f"  {i:>3}. {lib}")
        self.space(1)
        print("    0. All packages of this category")
        print("  You can also write several numbers separated by commas (e.g. 1,3,5)\n")
        try:
            seleccion = input("choose: ").strip()
        except KeyboardInterrupt:
            print("\nCancelled")
            getout()

        # Vacío, 0 o "all" => toda la categoría
        if seleccion in ("", "0", "all", "All", "ALL"):
            self.install(list(libs), name)

        elegidos = []
        for parte in seleccion.split(","):
            parte = parte.strip()
            if not parte:
                continue
            try:
                indice = int(parte)
            except ValueError:
                print(f"  '{parte}' is not a number, skipping it")
                continue
            if 1 <= indice <= len(libs):
                elegidos.append(libs[indice - 1])
            else:
                print(f"  {indice} is out of range, skipping it")

        elegidos = list(dict.fromkeys(elegidos))  # sin repetidos, conservando orden
        self.install(elegidos, name)

    def menu(self):
        print("Welcome to pyessentials, a little installer that helps you to install every API/Library that you will need for the 'campus' of programming you want to learn.")
        print(f"\nChoose one of the following categories (If you want to know what it is in every category, look it here at it's {self.link('repo', 'https://github.com/sotelodev2008/pyessentials')})")
        self.space(2)
        print("1. All\n2. Automation\n3. Big Data\n4. Bots\n5. Data Science\n6. Desktop Apps\n7. Data Visualization\n8. DevOPS\n9. FinTech\n10. IA/AI\n11. Iot\n12. System Administration\n13. Phone apps\n14. Videogames\n15. Web Development (Back-End)\n16. Web Scraping")
        try:
            opcion = int(input("choose an option: "))
        except ValueError:
            print("Do you know what is a number, it is a mathematical object used to count, measure, and label.")
            getout()

        mapping = {1: "-A", 2: "-a", 3: "-b", 4: "-B", 5: "-d", 6: "-D", 7: "-V", 8: "-o", 9: "-f", 10: "-I", 11: "-i", 12: "-s", 13: "-p", 14: "-v", 15: "-w", 16: "-S"}

        if opcion not in mapping:
            print("Dude, I know there are too many options to choose, however, there are only 16, so, how in the actual fuck did you choose that?\nTry again")
            getout()

        flag = mapping[opcion]

        if flag == "-A":  # All-In : junta todo sin repetir y lo instala
            lista = []
            for key in self.LIBRARIES:
                lista.extend(self.LIBRARIES[key])
            lista = list(dict.fromkeys(lista))
            self.install(lista, "All-In")
        else:
            self.library_menu(flag)

    def main(self):
        self.space(4)
        print(banner)
        self.space(4)
        if self.argument == "Null":
            self.menu()
        if self.argument == "-h":
            self.help()
            getout()
        if self.argument != "-A" and self.argument not in self.LIBRARIES:
            print("Choose a valid argument, or instead, use -h to see every argument")
            getout()

        if self.argument == "-A":  # All-In : junta todo sin repetir
            lista = []
            for key in self.LIBRARIES:
                lista.extend(self.LIBRARIES[key])
            lista = list(dict.fromkeys(lista))
            self.install(lista, "All-In")
        else:
            self.install(self.LIBRARIES[self.argument], self.NAMES[self.argument])

if len(arg) <= 1:
    sol = pyessentials()
elif len(arg) == 2:
    sol = pyessentials(arg[1])
else:
    print("Too much arguments")
    getout()

try:
    sol.main()

except FileNotFoundError:
    print("\nYou don't have installed python/pip, or maybe you don't have it on path")
    getout()

except CalledProcessError as e:
    print(f"\nError during the installation, this is the error output:\n{e.returncode}")
    getout()

except KeyboardInterrupt:
    print("\nInstallation Cancelled")

except Exception as e:
    print(f"\nUnexpected Error:\n{e}")
