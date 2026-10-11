<div align="right">

###### Made by ***Sotelo***

</div>

<div align="center">

# Pyessentials List

</div>

## Index

- [⚙️ Automation](#️-automation)
- [📊 Big Data](#-big-data)
- [🤖 Bots](#-bots)
- [📈 Data Science](#-data-science)
- [🖥️ Desktop Apps](#️-desktop-apps)
- [📉 Data Visualization](#-data-visualization)
- [🚀 DevOPS](#-devops)
- [💰 FinTech](#-fintech)
- [🧠 AI / AI](#-ai--ai)
- [📡 IoT](#-iot)
- [🛠️ System Administration](#️-system-administration)
- [📱 Phone Apps](#-phone-apps)
- [🎮 Videogames](#-videogames)
- [🌐 Web Development (Back-End)](#-web-development-back-end)
- [🕸️ Web Scraping](#️-web-scraping)

### 📋 Automation

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | Office Automation | Modifies, reads, and creates Excel files (.xlsx) in bulk without needing to open the program. | Automated generation of financial reports, inventories, and data analysis in Excel format. | &#9744; |
| [pypdf](https://pypdf.readthedocs.io/en/stable/) | Office Automation | Serves to split, merge, rotate, and extract text from thousands of PDF files automatically. | Mass processing of PDF documents such as invoices, contracts, or reports for archiving or data extraction. | &#9744; |
| [python-docx](https://python-docx.readthedocs.io/en/latest/) | Office Automation | Automates the creation and editing of reports and Word documents (.docx). | Automatic generation of corporate documents, customized contracts, and professionally formatted reports. | &#9744; |
| [playwright](https://playwright.dev/) | Web Automation | The fastest and most reliable modern library for automating Chrome, Firefox, and Safari. It is the current industry favorite. | End-to-end testing of modern web applications, dynamic scraping, and automation of complex browser workflows. | &#9744; |
| [selenium](https://selenium-python.readthedocs.io/) | Web Automation | The classic of all time. Slower than Playwright, but with a huge community and compatible with any old browser. | Legacy browser automation, cross-browser compatibility testing, and scraping of traditional websites. | &#9744; |
| [netmiko](https://ktbyers.github.io/netmiko/docs/netmiko/index.html) | Network Automation | Specifically designed to automate the configuration of network routers and switches (Cisco, Juniper, etc.). | Mass configuration of network equipment, configuration backups, and deployment of changes in enterprise network infrastructures. | &#9744; |
| [paramiko](https://docs.paramiko.org/en/stable/) | Network Automation | Automates secure SSH connections to execute commands on remote Linux servers. | Remote server administration, execution of maintenance scripts, and task automation in Linux environments. | &#9744; |
| [keyboard](https://pypi.org/project/keyboard/) | File and Task Automation | Library to take full control of the keyboard, allowing hook and simulation of global key presses. | Creating system hotkeys, macros, and desktop automation tasks. | &#9744; |
| [mouse](https://pypi.org/project/mouse/) | File and Task Automation | Sister library of keyboard designed specifically for controlling and listening to mouse events. | Automating clicks, window dragging, and screen coordinates. | &#9744; |
| [psutil](https://psutil.readthedocs.io/stable/) | File and Task Automation | Automates PC performance management (controls CPU usage, RAM, and open processes). | System resource monitoring, detection of processes consuming too many resources, and performance alert generation. | &#9744; |
| [pyautogui](https://pyautogui.readthedocs.io/en/latest/) | File and Task Automation | Controls the mouse and keyboard virtually to click, type, or drag screen elements automatically. | Automation of graphical interfaces that don't have an API, usability testing, and execution of repetitive tasks in desktop applications. | &#9744; |
| [pynput](https://pynput.readthedocs.io/en/latest/) | File and Task Automation | Advanced library to control and monitor input devices (keyboard and mouse) with detailed threading support. | Creating event loggers or custom controls within background applications. | &#9744; |
| [schedule](https://schedule.readthedocs.io/en/stable/) | File and Task Automation | Allows scheduling tasks to run at certain times using very simple syntax. | Scheduling of recurring scripts such as automatic backups, periodic report sending, and scheduled maintenance tasks. | &#9744; |
| [watchdog](https://python-watchdog.readthedocs.io/en/stable/) | File and Task Automation | Watches folders in real-time and executes actions if a file is created, deleted, or modified. | File synchronization between folders, automatic processing of incoming files, and monitoring of changes in critical directories. | &#9744; |

### 📊 Big Data

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [pyspark](https://spark.apache.org/docs/latest/api/python/) | Distributed Big Data | Apache Spark's distributed processing engine for terabyte-scale workloads. | Massive ETL, huge log analysis, and data pipelines over clusters. | &#9744; |
| [dask](https://docs.dask.org/en/stable/) | Distributed Big Data | Parallelizes Python compute, scaling from a laptop to a full cluster. | Parallel processing of arrays and dataframes larger than memory. | &#9744; |
| [polars](https://docs.pola.rs/) | Distributed Big Data | Blazing-fast Rust dataframe with multithreaded execution. | High-performance data analysis as a pandas alternative. | &#9744; |
| [pyarrow](https://arrow.apache.org/docs/python/) | Distributed Big Data | Python implementation of the Apache Arrow columnar format. | Data interoperability and efficient Parquet read/write. | &#9744; |
| [duckdb](https://duckdb.org/docs/) | Distributed Big Data | Embedded analytical (OLAP) database, serverless like SQLite. | Run SQL queries over local Parquet and CSV files. | &#9744; |
| [vaex](https://vaex.io/docs/) | Distributed Big Data | Handles billions of rows with memory-mapped dataframes. | Exploration and visualization of huge datasets. | &#9744; |
| [ray](https://docs.ray.io/en/latest/) | Distributed Big Data | Distributed framework to scale compute and machine learning. | Distributed training and parallel task execution. | &#9744; |
| [modin](https://modin.readthedocs.io/en/stable/) | Distributed Big Data | Speeds up pandas by spreading work across all CPU cores. | Drop-in replacement for pandas in existing scripts. | &#9744; |
| [apache-beam](https://beam.apache.org/documentation/) | Distributed Big Data | Unified model for batch and streaming processing. | Portable pipelines across different runners. | &#9744; |
| [apache-airflow](https://airflow.apache.org/docs/) | Orchestration | DAG-based workflow orchestrator for scheduling and monitoring. | Automating and monitoring complex data pipelines. | &#9744; |
| [kafka-python](https://kafka-python.readthedocs.io/en/master/) | Streaming | Apache Kafka client for producers and consumers. | Event streaming and distributed messaging. | &#9744; |
| [confluent-kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html) | Streaming | Optimized Kafka client built on librdkafka. | High-throughput event ingestion. | &#9744; |
| [pymongo](https://pymongo.readthedocs.io/en/stable/) | Databases | Official MongoDB client. | Storing and querying large NoSQL datasets. | &#9744; |
| [redis](https://redis-py.readthedocs.io/en/stable/) | Databases | Python Redis client. | High-speed caching, queues, and in-memory structures. | &#9744; |
| [h5py](https://docs.h5py.org/en/stable/) | Storage | Interface to HDF5 files for large arrays. | Efficiently storing scientific data. | &#9744; |
| [zstandard](https://python-zstandard.readthedocs.io/en/latest/) | Storage | High-performance zstd compression. | Compressing datasets before storing or transmitting. | &#9744; |

### 🤖 Bots

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [opencv-python](https://docs.opencv.org/5.0/) | Visual Simulation Bots | An advanced library that doesn't use official APIs, but instead "sees" the screen like a human to make decisions. It is widely used in video game bots along with pyautogui. Allows the bot to analyze the screen, search for a specific image (like an enemy or a button), and click on it. | On-screen element detection for video game automation, farming bots, and real-time visual recognition systems. | &#9744; |
| [alright](https://github.com/Kalebu/alright) | Messaging Bots | Selenium-based library that automates WhatsApp Web without needing to scan the QR code on each send (unlike other solutions). | Mass sending of WhatsApp messages, automated response bots, and management of business conversations without depending on paid APIs. | &#9744; |
| [discord.py](https://discordpy.readthedocs.io/en/stable/) | Messaging Bots | The queen and industry-standard library for creating interactive bots on Discord. Supports text commands, buttons, and audio systems. | Creation of Discord bots for communities, automatic moderation systems, audio playback in voice channels, and server management. | &#9744; |
| [python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/) | Messaging Bots | An excellent and well-maintained library to control the Telegram API. Allows you to do everything from simple command bots to complex interactive menus. | Development of Telegram bots for customer service, sending automated notifications, interactive polls, and automatic response systems. | &#9744; |
| [pywhatkit](https://pypi.org/project/pywhatkit/) | Messaging Bots | The most popular and simple library for automating WhatsApp. Uses web.whatsapp.com via browser to send scheduled messages. | Scheduled sending of WhatsApp messages to specific contacts at determined times, automation of reminders, and simple notifications. | &#9744; |
| [twitchio](https://twitchio.dev) | Messaging Bots | Specifically designed to create chat bots on Twitch, ideal for moderating channels, reading alerts, or interacting with live viewers. | Automated moderation of Twitch chats, response to viewer commands, channel points management, and custom alerts in streams. | &#9744; |
| [praw](https://praw.readthedocs.io/en/stable/) | Social Media Bots | The official library for interacting with Reddit. Allows you to create bots that moderate subreddits, respond to comments based on keywords, or publish threads. | Automatic moderation of subreddits, scheduled content publishing, trend analysis, and automated response to comments. | &#9744; |
| [tweepy](https://docs.tweepy.org/en/stable/) | Social Media Bots | The standard library for connecting with the X API (formerly Twitter). Serves to automate tweets, search hashtags, or monitor accounts in real-time. | Automated tweet publishing, monitoring of hashtags and mentions, sentiment analysis on social media, and management of X/Twitter accounts. | &#9744; |

### 📈 Data Science

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [numpy](https://numpy.org/doc/stable/) | Numerical Computing | Foundation of numerical computing in Python with multidimensional arrays and vectorized operations. | Backbone of almost every data, science, and AI library. | &#9744; |
| [pandas](https://pandas.pydata.org/docs/) | Data Analysis | Tabular data structures (DataFrames) to clean, transform, and analyze information. | Manipulating and analyzing structured datasets. | &#9744; |
| [scipy](https://docs.scipy.org/doc/scipy/) | Scientific Computing | Advanced optimization, integration, interpolation, and statistics functions. | Scientific computing and solving math problems. | &#9744; |
| [scikit-learn](https://scikit-learn.org/stable/) | Machine Learning | The reference library for classic machine learning models. | Classification, regression, clustering, and dimensionality reduction. | &#9744; |
| [statsmodels](https://www.statsmodels.org/stable/index.html) | Statistics | Statistical models and detailed hypothesis testing. | Advanced regressions and econometric analysis. | &#9744; |
| [sympy](https://docs.sympy.org/latest/index.html) | Symbolic Math | Symbolic computation (algebra, derivatives, integrals) in Python. | Solving equations and manipulating expressions symbolically. | &#9744; |
| [xgboost](https://xgboost.readthedocs.io/en/stable/) | Machine Learning | High-performance gradient boosting algorithm. | Winning predictive models on tabular data competitions. | &#9744; |
| [lightgbm](https://lightgbm.readthedocs.io/en/stable/) | Machine Learning | Fast, low-memory gradient boosting. | Efficiently training models on large datasets. | &#9744; |
| [catboost](https://catboost.ai/docs/) | Machine Learning | Gradient boosting with native support for categorical features. | Robust models without preprocessing categories. | &#9744; |
| [imbalanced-learn](https://imbalanced-learn.org/stable/) | Machine Learning | Resampling techniques for imbalanced datasets. | Fixing minority classes before training models. | &#9744; |
| [jupyter](https://jupyter.org/) / [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/) | Environments | Interactive notebooks and a data science work environment. | Exploration, prototyping, and documenting analyses. | &#9744; |
| [ydata-profiling](https://ydata-profiling.ydata.ai/docs/master/) | Exploratory Analysis | Auto-generates quality and statistics reports for a dataset. | Quick first look (EDA) at any dataset. | &#9744; |
| [shap](https://shap.readthedocs.io/en/latest/) | Interpretability | Explains model predictions through Shapley values. | Understanding which features drive predictions. | &#9744; |
| [lime](https://lime-ml.readthedocs.io/en/latest/) | Interpretability | Local interpretable explanations of classifiers and regressors. | Justifying specific predictions to stakeholders. | &#9744; |
| [nltk](https://www.nltk.org/) | NLP | Classic natural language processing toolkit. | Tokenization, stemming, and text analysis. | &#9744; |
| [spacy](https://spacy.io/) | NLP | Production NLP with fast, pretrained models. | Entity extraction and text pipelines at scale. | &#9744; |
| [yellowbrick](https://www.scikit-yb.org/en/latest/) | ML Visualization | Diagnostic visualizations for machine learning models. | Visually evaluating and comparing models. | &#9744; |
| [missingno](https://github.com/ResidentMario/missingno) | Exploratory Analysis | Visualizes missing data in a dataset. | Detecting and understanding null-value patterns. | &#9744; |

### 🖥️ Desktop Apps

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [customTkinter](https://customtkinter.tomschimansky.com/) | GUI Frameworks | Modern extension of Tkinter with automatic dark mode and natively styled visual components. | Creating modern and attractive interfaces without the outdated aesthetics of traditional Tkinter. | &#9744; |
| [Dear PyGui](https://dearpygui.readthedocs.io/en/latest/) | GUI Frameworks | Fast, low-level graphical user interface framework rendered by GPU using C++ (Dear ImGui). | Applications requiring high performance, development tools, and graphics processing. | &#9744; |
| [Flet](https://flet.dev/docs/) | GUI Frameworks | Flutter-based framework that allows building web, mobile, and desktop applications in Python. | Rapid development of modern and reactive interfaces with a single codebase. | &#9744; |
| [Kivy](https://kivy.org/doc/stable/) | GUI Frameworks | Open-source library for developing applications with touch interfaces and multi-platform support. | Applications with highly customized layouts, interactive kiosks, and mobile support. | &#9744; |
| [PySide](https://doc.qt.io/qtforpython-6/) | GUI Frameworks | Official and community bindings for the powerful industrial Qt framework in C++. | Complex, robust, and professional enterprise applications with design tools (Qt Designer). | &#9744; |
| [Tkinter](https://docs.python.org/3/library/tk.html) | GUI Frameworks | The default standard graphical user interface that comes integrated with the official Python installation. | Quick prototypes, lightweight internal tools, and simple applications without extra dependencies. | &#9745; |
| [wxPython](https://docs.wxpython.org/) | GUI Frameworks | Python binding for the C++ wxWidgets library, utilizing native operating system components. | Traditional applications that need to look exactly like the native programs of the system. | &#9744; |

### 📉 Data Visualization

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [matplotlib](https://matplotlib.org/stable/) | Base Charts | The most widely used and customizable plotting library in Python. | High-quality static charts and base for other libraries. | &#9744; |
| [seaborn](https://seaborn.pydata.org/) | Statistical Charts | High-level interface over matplotlib with statistical styling. | Distributions, correlations, and categorical plots. | &#9744; |
| [plotly](https://plotly.com/python/) | Interactive Charts | Interactive, web-publishable charts. | Dashboards and explorable visualizations with zoom and tooltips. | &#9744; |
| [kaleido](https://github.com/plotly/Kaleido) | Export | Engine to export Plotly figures to static images. | Saving interactive figures as PNG, SVG, or PDF. | &#9744; |
| [bokeh](https://docs.bokeh.org/en/latest/) | Interactive Charts | Interactive visualization built for browsers. | Interactive panels and live data applications. | &#9744; |
| [altair](https://altair-viz.github.io/) | Declarative Charts | Declarative grammar of graphics based on Vega-Lite. | Concise, reproducible charts in few lines. | &#9744; |
| [dash](https://dash.plotly.com/) | Dashboards | Framework to build analytical web apps with Plotly. | Interactive dashboards with controls and callbacks. | &#9744; |
| [streamlit](https://docs.streamlit.io/) | Dashboards | Build data web apps in minutes with just Python. | Dashboard prototypes and model demos. | &#9744; |
| [folium](https://python-visualization.github.io/folium/latest/) | Maps | Interactive Leaflet-based maps. | Geospatial visualization and heatmaps. | &#9744; |
| [geopandas](https://geopandas.org/en/stable/) | Geospatial | Extends pandas for geographic data. | Analyzing and visualizing vector data. | &#9744; |
| [networkx](https://networkx.org/documentation/stable/) | Graphs | Creation, analysis, and drawing of networks and graphs. | Visualizing relationships, social networks, and routes. | &#9744; |
| [wordcloud](https://github.com/amueller/word_cloud) | Text | Generates word clouds from text. | Visually summarizing term frequency. | &#9744; |
| [pydeck](https://deckgl.readthedocs.io/en/latest/) | Maps | Large-scale geospatial visualization with deck.gl. | 3D maps of millions of data points. | &#9744; |
| [mplfinance](https://github.com/matplotlib/mplfinance) | Finance | Financial charts (candlesticks, OHLC) over matplotlib. | Visualizing market prices and trends. | &#9744; |

### 🚀 DevOPS

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [fabric](https://docs.fabfile.org/en/stable/) | Server Automation | Runs shell commands on remote hosts over SSH. | Deployments and remote administration tasks. | &#9744; |
| [ansible](https://docs.ansible.com/ansible/latest/) | Configuration Management | Automates configuration and infrastructure deployment. | Declaratively provisioning servers (IaC). | &#9744; |
| [docker](https://docker-py.readthedocs.io/en/stable/) | Containers | Python SDK for the Docker API. | Managing containers and images from code. | &#9744; |
| [kubernetes](https://kubernetes.io/docs/reference/using-api/client-libraries/) | Orchestration | Official client to interact with Kubernetes clusters. | Deploying and managing workloads on K8s. | &#9744; |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | Cloud | Official AWS SDK. | Automating Amazon Web Services resources. | &#9744; |
| [invoke](https://www.pyinvoke.org/) | Task Automation | Runs tasks and shell commands from Python. | Defining build and deploy tasks. | &#9744; |
| [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) | Configuration | Parses and generates YAML files. | Reading configuration and IaC manifests. | &#9744; |
| [jinja2](https://jinja.palletsprojects.com/en/stable/) | Templating | Template engine to generate text and configs. | Rendering dynamic configuration files. | &#9744; |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Configuration | Loads environment variables from .env files. | Managing secrets and per-environment configs. | &#9744; |
| [click](https://click.palletsprojects.com/en/stable/) / [typer](https://typer.tiangolo.com/) | CLI | Frameworks to build command-line interfaces. | Creating clean, maintainable CLI tools. | &#9744; |
| [rich](https://rich.readthedocs.io/en/stable/) / [loguru](https://loguru.readthedocs.io/en/stable/) | Logging / Output | Rich console output and simple logging. | Readable logs and formatted consoles. | &#9744; |
| [prometheus-client](https://prometheus.github.io/client_python/) | Monitoring | Exposes metrics for Prometheus. | Instrumenting services and exporting metrics. | &#9744; |
| [opentelemetry-sdk](https://opentelemetry.io/docs/languages/python/) | Observability | Standard distributed traces and metrics. | Instrumenting applications for observability. | &#9744; |
| [pytest](https://docs.pytest.org/en/stable/) | Testing | Powerful, extensible testing framework. | Writing and running automated tests. | &#9744; |
| [pre-commit](https://pre-commit.com/) | Code Quality | Runs hooks before each commit. | Enforcing automatic formatting and linting. | &#9744; |
| [black](https://black.readthedocs.io/en/stable/) / [ruff](https://docs.astral.sh/ruff/) | Formatting / Linting | Code formatting and static analysis. | Keeping a consistent style and catching errors early. | &#9744; |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Typing | Static type checking. | Catching type errors before running. | &#9744; |

### 💰 FinTech

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [yfinance](https://ranaroussi.github.io/yfinance/) | Market Data | Downloads historical and live data from Yahoo Finance. | Stock, ETF, and crypto analysis. | &#9744; |
| [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) | Market Data | Accesses multiple financial data sources. | Fetching macro and market series. | &#9744; |
| [ccxt](https://docs.ccxt.com/) | Crypto | Unified library for dozens of crypto exchanges. | Algorithmic trading and cross-exchange arbitrage. | &#9744; |
| [alpaca-py](https://alpaca.markets/docs/) | Trading | Alpaca SDK for commission-free trading. | Automated stocks and crypto trading. | &#9744; |
| [ib_insync](https://ib-insync.readthedocs.io/) | Trading | Interacts with Interactive Brokers. | Algorithmic trading across global markets. | &#9744; |
| [backtrader](https://www.backtrader.com/docu/) | Backtesting | Backtesting and live-trading framework. | Testing strategies on historical data. | &#9744; |
| [zipline-reloaded](https://zipline.ml4trading.io/) | Backtesting | Backtesting engine used by Quantopian. | Developing and validating quant strategies. | &#9744; |
| [QuantLib](https://www.quantlib.org/) | Derivatives | Financial instrument pricing library. | Option pricing and interest-rate models. | &#9744; |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Indicators | Technical indicators over pandas dataframes. | Computing moving averages, RSI, MACD, and more. | &#9744; |
| [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/) | Indicators | Broad collection of technical indicators. | Technical analysis of price series. | &#9744; |
| [stockstats](https://github.com/jealous/stockstats) | Indicators | Adds indicator columns to a DataFrame. | Quick technical analysis over OHLC data. | &#9744; |
| [finnhub-python](https://finnhub.io/docs/api) | Market Data | Finnhub API client. | Company news and fundamentals. | &#9744; |
| [polygon-api-client](https://polygon.io/docs/) | Market Data | Polygon.io market data client. | High-quality data for strategies. | &#9744; |
| [stripe](https://stripe.com/docs/api) | Payments | Official Stripe SDK. | Online charges, subscriptions, and billing. | &#9744; |
| [plaid-python](https://plaid.com/docs/) | Banking | Connects to bank accounts via Plaid. | Bank aggregation and balance verification. | &#9744; |
| [paypalrestsdk](https://developer.paypal.com/) | Payments | PayPal integration. | Processing PayPal payments. | &#9744; |
| [cryptofeed](https://github.com/bmoscon/cryptofeed) | Crypto | Real-time exchange data streams. | Live order book and trade data. | &#9744; |
| [web3](https://web3py.readthedocs.io/en/stable/) | Blockchain | Interacts with the Ethereum blockchain. | DApps, contracts, and wallets in Python. | &#9744; |
| [pycoingecko](https://github.com/man-c/pycoingecko) | Crypto | CoinGecko API client. | Crypto prices and market data. | &#9744; |

### 🧠 AI / AI

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [tensorflow](https://www.tensorflow.org/api_docs/python/tf) | Deep Learning | Google's deep learning framework. | Neural networks and production deployment. | &#9744; |
| [torch](https://pytorch.org/docs/stable/index.html) | Deep Learning | Meta's deep learning framework, widely used in research. | Training neural networks and custom models. | &#9744; |
| [keras](https://keras.io/api/) | Deep Learning | High-level API to build neural networks. | Fast deep learning prototyping. | &#9744; |
| [transformers](https://huggingface.co/docs/transformers/index) | NLP / LLM | Pretrained models (BERT, GPT, etc.) from Hugging Face. | NLP, summarization, translation, and fine-tuning. | &#9744; |
| [datasets](https://huggingface.co/docs/datasets/index) | Data | Loads and processes Hugging Face datasets. | Preparing data to train models. | &#9744; |
| [sentence-transformers](https://www.sbert.net/) | Embeddings | Generates sentence and document embeddings. | Semantic search and text similarity. | &#9744; |
| [openai](https://platform.openai.com/docs/) | LLM API | Official OpenAI API client. | Using GPT for text, vision, and audio. | &#9744; |
| [anthropic](https://docs.anthropic.com/) | LLM API | Anthropic (Claude) API client. | Assistants and generation with Claude. | &#9744; |
| [google-generativeai](https://ai.google.dev/) | LLM API | Client for Google's Gemini models. | Multimodal generation with Gemini. | &#9744; |
| [langchain](https://python.langchain.com/docs/) | LLM Orchestration | Framework for LLM apps, chains, and agents. | Building assistants, RAG, and agents. | &#9744; |
| [langgraph](https://langchain-ai.github.io/langgraph/) | LLM Orchestration | Stateful graphs for LLM agents. | Complex agent flows with memory. | &#9744; |
| [llama-index](https://docs.llamaindex.ai/) | RAG | RAG and document indexing framework. | Question-answering over your own documents. | &#9744; |
| [chromadb](https://docs.trychroma.com/) | Vector DB | Embedded vector database. | Storing embeddings for semantic search. | &#9744; |
| [faiss-cpu](https://faiss.ai/) | Vector DB | Efficient vector similarity search. | Fast retrieval across millions of vectors. | &#9744; |
| [gymnasium](https://gymnasium.farama.org/) | Reinforcement Learning | Standard RL environments. | Training and evaluating RL agents. | &#9744; |
| [stable-baselines3](https://stable-baselines3.readthedocs.io/en/master/) | Reinforcement Learning | Reliable RL algorithm implementations. | Quickly prototyping RL agents. | &#9744; |
| [pytorch-lightning](https://lightning.ai/docs/pytorch/stable/) | Deep Learning | Training abstraction over PyTorch. | Scalable, organized training. | &#9744; |
| [diffusers](https://huggingface.co/docs/diffusers/index) | Generation | Diffusion models for images and audio. | Generating images with Stable Diffusion. | &#9744; |
| [ultralytics](https://docs.ultralytics.com/) | Vision | YOLO object detection models. | Real-time detection and segmentation. | &#9744; |
| [mediapipe](https://ai.google.dev/edge/mediapipe/solutions/guide) | Vision | Google's vision and pose solutions. | Hand, face, and body tracking. | &#9744; |
| [openai-whisper](https://github.com/openai/whisper) | Audio | Multilingual speech recognition. | Transcribing audio to text. | &#9744; |
| [pytesseract](https://github.com/madmaze/pytesseract) | OCR | OCR via the Tesseract engine. | Extracting text from images. | &#9744; |
| [prophet](https://facebook.github.io/prophet/) | Time Series | Meta's time series forecasting. | Demand and trend forecasting. | &#9744; |
| [mlflow](https://mlflow.org/docs/latest/index.html) | MLOps | ML model lifecycle management. | Tracking experiments and deploying models. | &#9744; |
| [wandb](https://docs.wandb.ai/) | MLOps | Experiment and metric tracking. | Visualizing and comparing training runs. | &#9744; |
| [peft](https://huggingface.co/docs/peft/index) | Fine-tuning | Efficient fine-tuning of large models (LoRA). | Adapting LLMs with few resources. | &#9744; |
| [crewai](https://docs.crewai.com/) | Agents | Framework for teams of AI agents. | Orchestrating multiple collaborating agents. | &#9744; |

### 📡 IoT

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [paho-mqtt](https://eclipse.dev/paho/index.php?page=clients/python/index.php) | Protocols | MQTT client for lightweight device messaging. | Sensor and actuator communication via a broker. | &#9744; |
| [aiomqtt](https://sbtinstruments.github.io/aiomqtt/) | Protocols | Asyncio-based MQTT client. | High-performance concurrent IoT. | &#9744; |
| [pyserial](https://pyserial.readthedocs.io/en/latest/) | Communication | Serial port communication. | Connecting Arduino, ESP32, and serial sensors. | &#9744; |
| [pymodbus](https://pymodbus.readthedocs.io/en/latest/) | Protocols | Implementation of the industrial Modbus protocol. | Reading PLCs and industrial equipment. | &#9744; |
| [asyncua](https://python-opcua.readthedocs.io/) | Protocols | OPC UA client and server. | Standardized industrial communication. | &#9744; |
| [gpiozero](https://gpiozero.readthedocs.io/en/stable/) | Hardware | Simple GPIO pin control on Raspberry Pi. | Reading buttons and controlling LEDs and relays. | &#9744; |
| [RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) | Hardware | Low-level access to Raspberry Pi GPIO. | Direct hardware control on the Pi. | &#9744; |
| [adafruit-blinka](https://docs.circuitpython.org/projects/blinka/en/latest/) | Hardware | Emulates CircuitPython on SBC boards. | Using Adafruit libraries on Raspberry Pi. | &#9744; |
| [smbus2](https://smbus2.readthedocs.io/en/latest/) | Hardware | I2C bus access. | Communicating with I2C sensors and displays. | &#9744; |
| [spidev](https://github.com/doceme/py-spidev) | Hardware | SPI bus access. | Connecting high-speed SPI devices. | &#9744; |
| [esptool](https://docs.espressif.com/projects/esptool/en/latest/) | Microcontrollers | Flashes firmware onto ESP chips. | Programming ESP8266 and ESP32. | &#9744; |
| [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) | Microcontrollers | Manages MicroPython boards. | Uploading and running code on microcontrollers. | &#9744; |
| [python-kasa](https://python-kasa.readthedocs.io/en/latest/) | Home Automation | Controls TP-Link Kasa devices. | Turning smart plugs and bulbs on and off. | &#9744; |
| [tuya-connector](https://github.com/tuya/tuya-connector-python) | Home Automation | Integrates Tuya cloud devices. | Controlling Tuya devices via API. | &#9744; |
| [bleak](https://bleak.readthedocs.io/en/latest/) | Bluetooth | Cross-platform Bluetooth Low Energy client. | Communicating with BLE sensors. | &#9744; |
| [influxdb-client](https://influxdb-client.readthedocs.io/en/stable/) | Data | InfluxDB client for time series. | Storing and querying IoT telemetry. | &#9744; |

### 🛠️ System Administration

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [paramiko](https://docs.paramiko.org/en/stable/) | SSH | SSH implementation in Python. | Running remote commands and transferring files. | &#9744; |
| [fabric](https://docs.fabfile.org/en/stable/) | Automation | Runs admin tasks across multiple hosts. | Remote deployments and maintenance. | &#9744; |
| [psutil](https://psutil.readthedocs.io/stable/) | Monitoring | Retrieves process and resource information. | Monitoring CPU, RAM, disk, and network. | &#9744; |
| [distro](https://distro.readthedocs.io/en/latest/) | System | Detects the Linux distribution. | Adapting scripts to each distro. | &#9744; |
| [netifaces](https://netifaces.readthedocs.io/en/stable/) | Network | Interface and address information. | Inventorying local network configuration. | &#9744; |
| [python-crontab](https://pypi.org/project/python-crontab/) | Scheduling | Manages cron jobs from Python. | Creating and editing crontabs programmatically. | &#9744; |
| [croniter](https://github.com/kiorky/croniter) | Scheduling | Parses and computes cron expressions. | Determining upcoming task runs. | &#9744; |
| [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) | Configuration | YAML parsing. | Reading service and infrastructure configs. | &#9744; |
| [ansible](https://docs.ansible.com/ansible/latest/) | Configuration | Agentless configuration automation. | Provisioning and maintaining server fleets. | &#9744; |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | Cloud | AWS SDK. | Managing cloud resources via code. | &#9744; |
| [docker](https://docker-py.readthedocs.io/en/stable/) | Containers | Docker API SDK. | Automating container management. | &#9744; |
| [kubernetes](https://kubernetes.io/docs/reference/using-api/client-libraries/) | Orchestration | Kubernetes API client. | Managing clusters and workloads. | &#9744; |
| [pyvmomi](https://github.com/vmware/pyvmomi) | Virtualization | VMware vSphere SDK. | Managing VMware virtual machines. | &#9744; |
| [libvirt-python](https://libvirt.org/python.html) | Virtualization | libvirt bindings for KVM/QEMU. | Managing VMs on Linux. | &#9744; |
| [ldap3](https://ldap3.readthedocs.io/en/latest/) | Directories | Pure-Python LDAP client. | Auth and queries on Active Directory. | &#9744; |
| [cryptography](https://cryptography.io/en/latest/) | Security | Modern cryptographic primitives. | Encryption, signing, and certificate management. | &#9744; |
| [scapy](https://scapy.readthedocs.io/en/latest/) | Networking | Packet manipulation. | Sniffing, scanning, and traffic analysis. | &#9744; |
| [netaddr](https://netaddr.readthedocs.io/en/latest/) | Networking | Working with network addresses and ranges. | Calculating subnets and validating IPs. | &#9744; |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | Networking | Measures connection speed. | Monitoring link bandwidth. | &#9744; |

### 📱 Phone Apps

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [kivy](https://kivy.org/doc/stable/) | Mobile Framework | Cross-platform framework with touch support. | Mobile and desktop apps from a single base. | &#9744; |
| [kivymd](https://kivymd.readthedocs.io/en/latest/) | Mobile UI | Implements Material Design over Kivy. | Interfaces with a modern Android look. | &#9744; |
| [buildozer](https://buildozer.readthedocs.io/en/latest/) | Packaging | Packages Kivy apps for Android/iOS. | Compiling installable APKs. | &#9744; |
| [briefcase](https://briefcase.readthedocs.io/en/stable/) | Packaging | Packages BeeWare apps for multiple platforms. | Distributing native desktop and mobile apps. | &#9744; |
| [toga](https://toga.readthedocs.io/en/latest/) | Mobile Framework | BeeWare's native cross-platform UI. | Apps with native system widgets. | &#9744; |
| [flet](https://flet.dev/docs/) | Mobile Framework | Builds cross-platform apps with Flutter in Python. | Mobile and web apps from a single base. | &#9744; |
| [plyer](https://plyer.readthedocs.io/en/latest/) | Native APIs | Accesses device features (GPS, camera, etc.). | Using phone hardware portably. | &#9744; |
| [pyjnius](https://pyjnius.readthedocs.io/en/latest/) | Bridges | Accesses Java classes from Python. | Integrating native Android APIs. | &#9744; |
| [pyobjus](https://pyobjus.readthedocs.io/en/latest/) | Bridges | Accesses Objective-C classes from Python. | Integrating native iOS APIs. | &#9744; |
| [appium-python-client](https://appium.github.io/python-client-sphinx/) | Testing | Appium client to automate mobile apps. | Automated testing on Android and iOS. | &#9744; |
| [uiautomator2](https://github.com/openatx/uiautomator2) | Automation | Controls Android devices from Python. | Automating an Android phone's UI. | &#9744; |

### 🎮 Videogames

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [pygame](https://www.pygame.org/docs/) | 2D Engine | The classic library for 2D games in Python. | Prototypes, 2D games, and education. | &#9744; |
| [pyglet](https://pyglet.readthedocs.io/en/latest/) | 2D/3D Engine | Lightweight, cross-platform multimedia framework. | Games and graphical apps with OpenGL. | &#9744; |
| [arcade](https://api.arcade.academy/en/latest/) | 2D Engine | Modern, simple framework for 2D games. | 2D games with sprites and simple physics. | &#9744; |
| [panda3d](https://docs.panda3d.org/1.10/python/index) | 3D Engine | Full 3D engine for games and simulations. | 3D games, visualizations, and simulators. | &#9744; |
| [moderngl](https://moderngl.readthedocs.io/en/latest/) | Graphics | Modern OpenGL wrapper. | High-performance custom rendering. | &#9744; |
| [ursina](https://www.ursinaengine.org/documentation.html) | 3D Engine | Easy-to-use 3D engine over Panda3D. | 3D games and quick prototypes. | &#9744; |
| [PyOpenGL](https://pyopengl.sourceforge.net/documentation/) | Graphics | OpenGL bindings. | Low-level graphics rendering. | &#9744; |
| [pymunk](https://www.pymunk.org/en/latest/) | Physics | 2D physics engine (Chipmunk). | Simulating 2D collisions and rigid bodies. | &#9744; |
| [Box2D](https://github.com/pybox2d/pybox2d) | Physics | Box2D physics engine bindings. | Realistic 2D physics in games. | &#9744; |
| [pytmx](https://pytmx.readthedocs.io/en/latest/) | Levels | Loads TMX maps from Tiled. | Designing levels for 2D games. | &#9744; |
| [pygame-menu](https://pygame-menu.readthedocs.io/en/latest/) | Game UI | Creates game menus with pygame. | Menus, options, and pauses. | &#9744; |
| [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/) | Game UI | UI system for pygame. | Buttons, sliders, and windows in games. | &#9744; |
| [pybullet](https://pybullet.org/wordpress/) | 3D Physics | 3D physics and robotics simulation. | Robotics and 3D physics simulators. | &#9744; |
| [harfang3d](https://www.harfang3d.com/documentation/) | 3D Engine | Lightweight, cross-platform 3D engine. | 3D games and VR apps. | &#9744; |

### 🌐 Web Development (Back-End)

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [flask](https://flask.palletsprojects.com/en/stable/) | Microframework | Minimalist and flexible web microframework. | Lightweight APIs and web apps. | &#9744; |
| [django](https://docs.djangoproject.com/en/stable/) | Full-Stack Framework | Complete framework with ORM, admin, and auth included. | Large web applications built fast. | &#9744; |
| [fastapi](https://fastapi.tiangolo.com/) | API Framework | Modern typed, async API framework. | High-performance, documented REST APIs. | &#9744; |
| [starlette](https://www.starlette.io/) | API Framework | Lightweight ASGI framework, FastAPI's base. | Low-level async services. | &#9744; |
| [uvicorn](https://www.uvicorn.org/) | Server | Fast ASGI server. | Serving async apps in dev and production. | &#9744; |
| [gunicorn](https://docs.gunicorn.org/en/stable/) | Server | Production WSGI server. | Robustly deploying WSGI apps. | &#9744; |
| [aiohttp](https://docs.aiohttp.org/en/stable/) | Async | Async HTTP client and server. | High-performance concurrent APIs and clients. | &#9744; |
| [sqlalchemy](https://docs.sqlalchemy.org/en/20/) | ORM | Powerful ORM and SQL toolkit. | Modeling and querying relational databases. | &#9744; |
| [alembic](https://alembic.sqlalchemy.org/en/latest/) | Migrations | Database migrations for SQLAlchemy. | Evolving schemas without data loss. | &#9744; |
| [pydantic](https://docs.pydantic.dev/latest/) | Validation | Typed data validation and serialization. | Validating payloads and configs. | &#9744; |
| [psycopg2-binary](https://www.psycopg.org/docs/) | Database | PostgreSQL driver. | Connecting apps to PostgreSQL. | &#9744; |
| [pymongo](https://pymongo.readthedocs.io/en/stable/) | Database | MongoDB client. | NoSQL persistence in web apps. | &#9744; |
| [redis](https://redis-py.readthedocs.io/en/stable/) | Database | Redis client. | Web app caching and sessions. | &#9744; |
| [jinja2](https://jinja.palletsprojects.com/en/stable/) | Templating | HTML template engine. | Server-side page rendering. | &#9744; |
| [celery](https://docs.celeryq.dev/en/stable/) | Queues | Distributed task queue. | Running heavy jobs in the background. | &#9744; |
| [httpx](https://www.python-httpx.org/) | HTTP | Modern HTTP client with async support. | Consuming external APIs from the back-end. | &#9744; |
| [websockets](https://websockets.readthedocs.io/en/stable/) | Real-Time | WebSocket protocol implementation. | Chat and real-time data. | &#9744; |
| [strawberry-graphql](https://strawberry.rocks/docs) | GraphQL | Type-based GraphQL framework. | Building GraphQL APIs in Python. | &#9744; |
| [djangorestframework](https://www.django-rest-framework.org/) | API Framework | Toolkit to build REST APIs with Django. | Robust APIs on Django projects. | &#9744; |

### 🕸️ Web Scraping

| Library/API | Category | Description | Primary Use | Pre-installed |
| :--- | :--- | :--- | :--- | :---: |
| [requests](https://requests.readthedocs.io/en/latest/) | HTTP | The most popular HTTP library in Python. | Making requests to pages and APIs. | &#9744; |
| [httpx](https://www.python-httpx.org/) | HTTP | Modern HTTP client with async and HTTP/2. | High-performance concurrent scraping. | &#9744; |
| [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | HTML Parsing | Parses and navigates HTML tolerantly. | Extracting data from web pages. | &#9744; |
| [lxml](https://lxml.de/) | HTML Parsing | Fast C-based HTML/XML parser. | Processing HTML/XML at high speed. | &#9744; |
| [scrapy](https://docs.scrapy.org/en/latest/) | Framework | Full scraping framework with spiders. | Large-scale crawlers and scraping pipelines. | &#9744; |
| [selenium](https://selenium-python.readthedocs.io/) | Browser | Automates real browsers. | Scraping JavaScript-heavy sites. | &#9744; |
| [playwright](https://playwright.dev/python/) | Browser | Modern, fast browser automation. | Dynamic scraping and complex flows. | &#9744; |
| [mechanicalsoup](https://mechanicalsoup.readthedocs.io/en/stable/) | Browser | Simple navigation over requests and BeautifulSoup. | Filling and submitting forms easily. | &#9744; |
| [requests-html](https://requests.readthedocs.io/projects/requests-html/en/latest/) | Browser | JavaScript-rendered HTML over requests. | Easy scraping of dynamic pages. | &#9744; |
| [pyquery](https://pythonhosted.org/pyquery/) | HTML Parsing | jQuery-like selectors over HTML. | Extracting data with concise CSS selectors. | &#9744; |
| [parsel](https://parsel.readthedocs.io/en/latest/) | HTML Parsing | XPath/CSS selectors used by Scrapy. | Extracting data from HTML/XML. | &#9744; |
| [fake-useragent](https://fake-useragent.readthedocs.io/en/latest/) | Antibot | Generates random user-agents. | Avoiding browser-fingerprint blocks. | &#9744; |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Antibot | Solves Cloudflare challenges. | Scraping Cloudflare-protected sites. | &#9744; |
| [selenium-wire](https://github.com/wkeeling/selenium-wire) | Antibot | Inspects network traffic in Selenium. | Capturing requests and responses. | &#9744; |
| [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | Antibot | Undetectable Chrome Driver. | Avoiding bot detection. | &#9744; |
| [curl-cffi](https://curl-cffi.readthedocs.io/en/latest/) | HTTP | Imitates curl/browser fingerprints. | Bypassing TLS and antibot protections. | &#9744; |
| [newspaper3k](https://newspaper.readthedocs.io/en/latest/) | Extraction | Extracts articles and news. | Gathering and analyzing news. | &#9744; |
| [trafilatura](https://trafilatura.readthedocs.io/en/latest/) | Extraction | Extracts the main content of pages. | Getting clean article text. | &#9744; |
