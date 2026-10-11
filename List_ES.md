<div align="right">

###### Hecho por ***Sotelo***

</div>

<div align="center">

# Pyessentials Lista

</div>

## Indice

- [⚙️ Automatización](#-automatización)
- [📊 Big Data](#-big-data)
- [🤖 Bots](#-bots)
- [📈 Ciencia de Datos](#-ciencia-de-datos)
- [🖥️ Apps De Escritorio](#-apps-de-escritorio)
- [📉 Visualización de Datos](#-visualización-de-datos)
- [🚀 DevOPS](#-devops)
- [💰 FinTech](#-fintech)
- [🧠 IA / AI](#-ia--ai)
- [📡 IoT](#-iot)
- [🛠️ Administración de Sistemas](#-administración-de-sistemas)
- [📱 Apps Para Teléfonos](#-apps-para-teléfonos)
- [🎮 Videojuegos](#-videojuegos)
- [🌐 Desarrollo Web (Back-End)](#-desarrollo-web-back-end)
- [🕸️ Web Scraping](#-web-scraping)

### ⚙️ Automatización

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | Automatización Ofimática | Modifica, lee y crea archivos de Excel (.xlsx) de forma masiva sin necesidad de abrir el programa. | Generación de reportes financieros, inventarios y análisis de datos en formato Excel de manera automatizada. | &#9744; |
| [pypdf](https://pypdf.readthedocs.io/en/stable/) | Automatización Ofimática | Sirve para dividir, fusionar, rotar y extraer texto de miles de archivos PDF automáticamente. | Procesamiento masivo de documentos PDF como facturas, contratos o informes para archivado o extracción de datos. | &#9744; |
| [python-docx](https://python-docx.readthedocs.io/en/latest/) | Automatización Ofimática | Automatiza la creación y edición de informes y documentos de Word (.docx). | Generación automática de documentos corporativos, contratos personalizados y reportes con formato profesional. | &#9744; |
| [playwright](https://playwright.dev/) | Automatización Web | La librería moderna más rápida y fiable para automatizar Chrome, Firefox y Safari. Es la favorita actual de la industria. | Pruebas end-to-end de aplicaciones web modernas, scraping dinámico y automatización de flujos de trabajo complejos en el navegador. | &#9744; |
| [selenium](https://selenium-python.readthedocs.io/) | Automatización Web | El clásico de toda la vida. Más lento que Playwright, pero con una comunidad gigantesca y compatible con cualquier navegador viejo. | Automatización de navegadores legacy, pruebas de compatibilidad entre navegadores y scraping de sitios web tradicionales. | &#9744; |
| [netmiko](https://ktbyers.github.io/netmiko/docs/netmiko/index.html) | Automatización de Redes | Diseñada específicamente para automatizar la configuración de routers y switches de red (Cisco, Juniper, etc.). | Configuración masiva de equipos de red, backup de configuraciones y despliegue de cambios en infraestructuras de red empresariales. | &#9744; |
| [paramiko](https://docs.paramiko.org/en/stable/) | Automatización de Redes | Automatiza conexiones seguras por SSH para ejecutar comandos en servidores Linux remotos. | Administración remota de servidores, ejecución de scripts de mantenimiento y automatización de tareas en entornos Linux. | &#9744; |
| [keyboard](https://pypi.org/project/keyboard/) | Automatización de Archivos y Tareas | Librería para tomar control total del teclado, permitiendo escuchar y simular pulsaciones de teclas globales. | Creación de atajos de teclado del sistema (hotkeys), macros y automatización de tareas de escritorio. | &#9744; |
| [mouse](https://pypi.org/project/mouse/) | Automatización de Archivos y Tareas | Librería hermana de keyboard diseñada específicamente para el control y escucha de eventos del ratón. | Automatizar clics, arrastres de ventanas y coordenadas de pantalla. | &#9744; |
| [psutil](https://psutil.readthedocs.io/stable/) | Automatización de Archivos y Tareas | Automatiza la gestión del rendimiento del PC (controla el uso de CPU, RAM y los procesos abiertos). | Monitorización de recursos del sistema, detección de procesos que consumen demasiados recursos y generación de alertas de rendimiento. | &#9744; |
| [pyautogui](https://pyautogui.readthedocs.io/en/latest/) | Automatización de Archivos y Tareas | Controla el ratón y el teclado de forma virtual para hacer clics, escribir o arrastrar elementos de la pantalla automáticamente. | Automatización de interfaces gráficas que no tienen API, pruebas de usabilidad y ejecución de tareas repetitivas en aplicaciones de escritorio. | &#9744; |
| [pynput](https://pynput.readthedocs.io/en/latest/) | Automatización de Archivos y Tareas | Librería avanzada para controlar y monitorear los dispositivos de entrada (teclado y ratón) con soporte detallado de hilos. | Crear registradores de eventos (loggers) o controles personalizados dentro de aplicaciones de fondo. | &#9744; |
| [schedule](https://schedule.readthedocs.io/en/stable/) | Automatización de Archivos y Tareas | Permite programar tareas para que se ejecuten cada cierto tiempo usando una sintaxis muy sencilla. | Programación de scripts recurrentes como backups automáticos, envío de reportes periódicos y tareas de mantenimiento programadas. | &#9744; |
| [watchdog](https://python-watchdog.readthedocs.io/en/stable/) | Automatización de Archivos y Tareas | Vigila carpetas en tiempo real y ejecuta acciones si un archivo se crea, borra o modifica. | Sincronización de archivos entre carpetas, procesamiento automático de archivos entrantes y monitoreo de cambios en directorios críticos. | &#9744; |

### 📊 Big Data

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [pyspark](https://spark.apache.org/docs/latest/api/python/) | Big Data Distribuido | Motor de procesamiento distribuido de Apache Spark para trabajar con volúmenes de datos a escala de terabytes. | ETL masivo, análisis de logs gigantes y construcción de pipelines de datos sobre clústeres. | &#9744; |
| [dask](https://docs.dask.org/en/stable/) | Big Data Distribuido | Paraleliza el cómputo en Python, escalando desde un portátil hasta un clúster completo. | Procesamiento paralelo de arrays y dataframes más grandes que la memoria disponible. | &#9744; |
| [polars](https://docs.pola.rs/) | Big Data Distribuido | Dataframe ultrarrápido escrito en Rust con ejecución multihilo y API expresiva. | Análisis de datos de alto rendimiento como alternativa a pandas. | &#9744; |
| [pyarrow](https://arrow.apache.org/docs/python/) | Big Data Distribuido | Implementación en Python del formato columnar Apache Arrow. | Interoperabilidad de datos entre librerías y lectura/escritura eficiente de Parquet. | &#9744; |
| [duckdb](https://duckdb.org/docs/) | Big Data Distribuido | Base de datos analítica embebida (OLAP) al estilo SQLite, sin servidor. | Ejecutar consultas SQL sobre archivos Parquet y CSV locales. | &#9744; |
| [vaex](https://vaex.io/docs/) | Big Data Distribuido | Maneja dataframes de miles de millones de filas con memoria mapeada. | Exploración y visualización de datasets gigantes. | &#9744; |
| [ray](https://docs.ray.io/en/latest/) | Big Data Distribuido | Framework distribuido para escalar cómputo y machine learning. | Entrenamiento distribuido y ejecución de tareas paralelas. | &#9744; |
| [modin](https://modin.readthedocs.io/en/stable/) | Big Data Distribuido | Acelera pandas repartiendo el trabajo entre todos los núcleos del equipo. | Reemplazo directo (drop-in) de pandas en scripts existentes. | &#9744; |
| [apache-beam](https://beam.apache.org/documentation/) | Big Data Distribuido | Modelo unificado para procesamiento por lotes y en streaming. | Pipelines portables entre distintos motores de ejecución. | &#9744; |
| [apache-airflow](https://airflow.apache.org/docs/) | Orquestación | Orquestador de workflows basado en DAGs para programar y monitorizar. | Automatizar y vigilar pipelines de datos complejos. | &#9744; |
| [kafka-python](https://kafka-python.readthedocs.io/en/master/) | Streaming | Cliente de Apache Kafka para productores y consumidores. | Streaming de eventos y mensajería distribuida. | &#9744; |
| [confluent-kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html) | Streaming | Cliente optimizado de Kafka basado en librdkafka. | Alta productividad en la ingesta de eventos. | &#9744; |
| [pymongo](https://pymongo.readthedocs.io/en/stable/) | Bases de Datos | Cliente oficial de MongoDB. | Almacenar y consultar grandes volúmenes de datos NoSQL. | &#9744; |
| [redis](https://redis-py.readthedocs.io/en/stable/) | Bases de Datos | Cliente de Redis en Python. | Caché, colas y estructuras en memoria de alta velocidad. | &#9744; |
| [h5py](https://docs.h5py.org/en/stable/) | Almacenamiento | Interfaz a archivos HDF5 para grandes arrays. | Guardar datos científicos de forma eficiente. | &#9744; |
| [zstandard](https://python-zstandard.readthedocs.io/en/latest/) | Almacenamiento | Compresión zstd de alto rendimiento. | Comprimir datasets antes de almacenarlos o transmitirlos. | &#9744; |

### 🤖 Bots

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [opencv-python](https://docs.opencv.org/5.0/) | Bots de Simulación Visual | Librería avanzada que no usan APIs oficiales, sino que "ven" la pantalla como un humano para tomar decisiones. se usa muchísimo en bots de videojuegos junto a pyautogui. Permite al bot analizar la pantalla, buscar una imagen concreta (como un enemigo o un botón) y hacer clic sobre ella. | Detección de elementos en pantalla para automatización de videojuegos, bots de farming y sistemas de reconocimiento visual en tiempo real. | &#9744; |
| [alright](https://github.com/Kalebu/alright) | Bots para Mensajería | Librería basada en Selenium que automatiza WhatsApp Web sin necesidad de escanear el QR en cada envío (a diferencia de otras soluciones). | Envío masivo de mensajes de WhatsApp, bots de respuesta automatizada y gestión de conversaciones comerciales sin depender de APIs de pago. | &#9744; |
| [discord.py](https://discordpy.readthedocs.io/en/stable/) | Bots para Mensajería | La librería reina y estándar de la industria para crear bots interactivos en Discord. Soporta comandos de texto, botones y sistemas de audio. | Creación de bots de Discord para comunidades, sistemas de moderación automática, reproducción de audio en canales de voz y gestión de servidores. | &#9744; |
| [python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/) | Bots para Mensajería | Una librería excelente y muy mantenida para controlar la API de Telegram. Te permite hacer desde bots de comandos simples hasta menús interactivos complejos. | Desarrollo de bots de Telegram para atención al cliente, envío de notificaciones automatizadas, encuestas interactivas y sistemas de respuesta automática. | &#9744; |
| [pywhatkit](https://pypi.org/project/pywhatkit/) | Bots para Mensajería | La librería más popular y sencilla para automatizar WhatsApp. Usa web.whatsapp.com mediante el navegador para enviar mensajes programados. | Envío programado de mensajes de WhatsApp a contactos específicos en horarios determinados, automatización de recordatorios y notificaciones simples. | &#9744; |
| [twitchio](https://twitchio.dev) | Bots para Mensajería | Diseñada específicamente para crear bots de chat en Twitch, ideal para moderar canales, leer alertas o interactuar con los espectadores en vivo. | Moderación automatizada de chats de Twitch, respuesta a comandos de espectadores, gestión de puntos del canal y alertas personalizadas en streams. | &#9744; |
| [praw](https://praw.readthedocs.io/en/stable/) | Bots para Redes Sociales | La librería oficial para interactuar con Reddit. Te permite crear bots que moderen subreddits, respondan comentarios basados en palabras clave o publiquen hilos. | Moderación automática de subreddits, publicación programada de contenido, análisis de tendencias y respuesta automatizada a comentarios. | &#9744; |
| [tweepy](https://docs.tweepy.org/en/stable/) | Bots para Redes Sociales | La librería estándar para conectar con la API de X (anteriormente Twitter). Sirve para automatizar tweets, buscar hashtags o monitorizar cuentas en tiempo real. | Publicación automatizada de tweets, monitorización de hashtags y menciones, análisis de sentimiento en redes y gestión de cuentas de X/Twitter. | &#9744; |

### 📈 Ciencia de Datos

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [numpy](https://numpy.org/doc/stable/) | Cálculo Numérico | Base del cálculo numérico en Python con arrays multidimensionales y operaciones vectorizadas. | Cimientos de casi toda librería de datos, ciencia e IA. | &#9744; |
| [pandas](https://pandas.pydata.org/docs/) | Análisis de Datos | Estructuras de datos tabulares (DataFrames) para limpiar, transformar y analizar información. | Manipulación y análisis de datasets estructurados. | &#9744; |
| [scipy](https://docs.scipy.org/doc/scipy/) | Cálculo Científico | Funciones avanzadas de optimización, integración, interpolación y estadística. | Cálculo científico y resolución de problemas matemáticos. | &#9744; |
| [scikit-learn](https://scikit-learn.org/stable/) | Machine Learning | La librería de referencia para modelos clásicos de machine learning. | Clasificación, regresión, clustering y reducción de dimensionalidad. | &#9744; |
| [statsmodels](https://www.statsmodels.org/stable/index.html) | Estadística | Modelos estadísticos y pruebas de hipótesis detalladas. | Regresiones avanzadas y análisis econométrico. | &#9744; |
| [sympy](https://docs.sympy.org/latest/index.html) | Matemática Simbólica | Cálculo simbólico (álgebra, derivadas, integrales) en Python. | Resolver ecuaciones y manipular expresiones de forma simbólica. | &#9744; |
| [xgboost](https://xgboost.readthedocs.io/en/stable/) | Machine Learning | Algoritmo de gradient boosting de alto rendimiento. | Modelos predictivos ganadores en competiciones de datos tabulares. | &#9744; |
| [lightgbm](https://lightgbm.readthedocs.io/en/stable/) | Machine Learning | Gradient boosting rápido y de bajo consumo de memoria. | Entrenamiento eficiente de modelos sobre grandes datasets. | &#9744; |
| [catboost](https://catboost.ai/docs/) | Machine Learning | Gradient boosting con soporte nativo para variables categóricas. | Modelos robustos sin necesidad de preprocesar categorías. | &#9744; |
| [imbalanced-learn](https://imbalanced-learn.org/stable/) | Machine Learning | Técnicas de remuestreo para datasets desbalanceados. | Corregir clases minoritarias antes de entrenar modelos. | &#9744; |
| [jupyter](https://jupyter.org/) / [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/) | Entornos | Cuadernos interactivos y entorno de trabajo para ciencia de datos. | Exploración, prototipado y documentación de análisis. | &#9744; |
| [ydata-profiling](https://ydata-profiling.ydata.ai/docs/master/) | Análisis Exploratorio | Genera reportes automáticos de calidad y estadísticas de un dataset. | Primer vistazo rápido (EDA) a cualquier conjunto de datos. | &#9744; |
| [shap](https://shap.readthedocs.io/en/latest/) | Interpretabilidad | Explica las predicciones de los modelos mediante valores de Shapley. | Entender qué variables influyen en las predicciones. | &#9744; |
| [lime](https://lime-ml.readthedocs.io/en/latest/) | Interpretabilidad | Explicaciones locales interpretables de clasificadores y regresores. | Justificar predicciones concretas ante stakeholders. | &#9744; |
| [nltk](https://www.nltk.org/) | NLP | Kit clásico de procesamiento de lenguaje natural. | Tokenización, stemming y análisis de texto. | &#9744; |
| [spacy](https://spacy.io/) | NLP | NLP de producción con modelos rápidos y preentrenados. | Extracción de entidades y pipelines de texto a escala. | &#9744; |
| [yellowbrick](https://www.scikit-yb.org/en/latest/) | Visualización ML | Visualizaciones diagnósticas para modelos de machine learning. | Evaluar y comparar modelos de forma visual. | &#9744; |
| [missingno](https://github.com/ResidentMario/missingno) | Análisis Exploratorio | Visualiza los datos faltantes de un dataset. | Detectar y entender patrones de valores nulos. | &#9744; |

### 🖥️ Apps De Escritorio

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [customTkinter](https://customtkinter.tomschimansky.com/) | GUI Frameworks | Extensión moderna de Tkinter con diseño oscuro automático y componentes visuales estilizados de forma nativa. | Crear interfaces modernas y atractivas sin la estética antigua de Tkinter tradicional. | &#9744; |
| [Dear PyGui](https://dearpygui.readthedocs.io/en/latest/) | GUI Frameworks | Framework de interfaz gráfica rápido, de bajo nivel y renderizado por GPU mediante C++ (Dear ImGui). | Aplicaciones que requieren alto rendimiento, herramientas de desarrollo y procesamiento de gráficos. | &#9744; |
| [Flet](https://flet.dev/docs/) | GUI Frameworks | Framework basado en Flutter que permite construir aplicaciones web, móviles y de escritorio en Python. | Desarrollo rápido de interfaces modernas y reactivas con un solo código base. | &#9744; |
| [Kivy](https://kivy.org/doc/stable/) | GUI Frameworks | Librería de código abierto para el desarrollo de aplicaciones con interfaces táctiles y soporte multiplataforma. | Aplicaciones con diseños altamente personalizados, quioscos interactivos y soporte móvil. | &#9744; |
| [PySide](https://doc.qt.io/qtforpython-6/) | GUI Frameworks | Enlaces (bindings) oficiales y comunitarios del potente framework industrial Qt en C++. | Aplicaciones empresariales complejas, robustas y de nivel profesional con herramientas de diseño (Qt Designer). | &#9744; |
| [Tkinter](https://docs.python.org/3/library/tk.html) | GUI Frameworks | La interfaz gráfica estándar por defecto que viene integrada en la instalación oficial de Python. | Prototipos rápidos, herramientas internas ligeras y aplicaciones sencillas que no requieran dependencias. | &#9745; |
| [wxPython](https://docs.wxpython.org/) | GUI Frameworks | Enlace de Python para la biblioteca wxWidgets en C++, utilizando los componentes nativos del sistema operativo. | Aplicaciones tradicionales que necesitan verse exactamente igual que los programas nativos del sistema. | &#9744; |

### 📉 Visualización de Datos

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [matplotlib](https://matplotlib.org/stable/) | Gráficos Base | La librería de gráficos más usada y personalizable de Python. | Gráficas estáticas de alta calidad y base para otras librerías. | &#9744; |
| [seaborn](https://seaborn.pydata.org/) | Gráficos Estadísticos | Interfaz de alto nivel sobre matplotlib con estética estadística. | Distribuciones, correlaciones y gráficos categóricos. | &#9744; |
| [plotly](https://plotly.com/python/) | Gráficos Interactivos | Gráficos interactivos y publicables en web. | Dashboards y visualizaciones explorables con zoom y tooltips. | &#9744; |
| [kaleido](https://github.com/plotly/Kaleido) | Exportación | Motor para exportar gráficos de Plotly a imágenes estáticas. | Guardar figuras interactivas como PNG, SVG o PDF. | &#9744; |
| [bokeh](https://docs.bokeh.org/en/latest/) | Gráficos Interactivos | Visualización interactiva pensada para navegadores. | Paneles interactivos y aplicaciones de datos en vivo. | &#9744; |
| [altair](https://altair-viz.github.io/) | Gráficos Declarativos | Gramática de gráficos declarativa basada en Vega-Lite. | Gráficos concisos y reproducibles con pocas líneas. | &#9744; |
| [dash](https://dash.plotly.com/) | Dashboards | Framework para construir apps analíticas web con Plotly. | Dashboards interactivos con controles y callbacks. | &#9744; |
| [streamlit](https://docs.streamlit.io/) | Dashboards | Crea apps de datos web en minutos con solo Python. | Prototipos de dashboards y demos de modelos. | &#9744; |
| [folium](https://python-visualization.github.io/folium/latest/) | Mapas | Mapas interactivos basados en Leaflet. | Visualización geoespacial y mapas de calor. | &#9744; |
| [geopandas](https://geopandas.org/en/stable/) | Geoespacial | Extiende pandas para datos geográficos. | Análisis y visualización de datos vectoriales. | &#9744; |
| [networkx](https://networkx.org/documentation/stable/) | Grafos | Creación, análisis y dibujo de redes y grafos. | Visualizar relaciones, redes sociales y rutas. | &#9744; |
| [wordcloud](https://github.com/amueller/word_cloud) | Texto | Genera nubes de palabras a partir de texto. | Resumir visualmente la frecuencia de términos. | &#9744; |
| [pydeck](https://deckgl.readthedocs.io/en/latest/) | Mapas | Visualización geoespacial de gran escala con deck.gl. | Mapas 3D de millones de puntos de datos. | &#9744; |
| [mplfinance](https://github.com/matplotlib/mplfinance) | Finanzas | Gráficos financieros (velas, OHLC) sobre matplotlib. | Visualizar precios y tendencias de mercado. | &#9744; |

### 🚀 DevOPS

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [fabric](https://docs.fabfile.org/en/stable/) | Automatización de Servidores | Ejecuta comandos shell sobre hosts remotos vía SSH. | Despliegues y tareas de administración remota. | &#9744; |
| [ansible](https://docs.ansible.com/ansible/latest/) | Gestión de Configuración | Automatiza la configuración y despliegue de infraestructura. | Aprovisionar servidores de forma declarativa (IaC). | &#9744; |
| [docker](https://docker-py.readthedocs.io/en/stable/) | Contenedores | SDK de Python para la API de Docker. | Gestionar contenedores e imágenes desde código. | &#9744; |
| [kubernetes](https://kubernetes.io/docs/reference/using-api/client-libraries/) | Orquestación | Cliente oficial para interactuar con clústeres de Kubernetes. | Desplegar y gestionar workloads en K8s. | &#9744; |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | Cloud | SDK oficial de AWS. | Automatizar recursos de Amazon Web Services. | &#9744; |
| [invoke](https://www.pyinvoke.org/) | Automatización de Tareas | Ejecuta tareas y comandos de shell desde Python. | Definir tareas de build y despliegue. | &#9744; |
| [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) | Configuración | Parseo y generación de archivos YAML. | Leer manifiestos de configuración e IaC. | &#9744; |
| [jinja2](https://jinja.palletsprojects.com/en/stable/) | Plantillas | Motor de plantillas para generar texto y configs. | Renderizar archivos de configuración dinámicos. | &#9744; |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Configuración | Carga variables de entorno desde archivos .env. | Gestionar secretos y configs por entorno. | &#9744; |
| [click](https://click.palletsprojects.com/en/stable/) / [typer](https://typer.tiangolo.com/) | CLI | Frameworks para construir interfaces de línea de comandos. | Crear herramientas CLI limpias y mantenibles. | &#9744; |
| [rich](https://rich.readthedocs.io/en/stable/) / [loguru](https://loguru.readthedocs.io/en/stable/) | Logging / Salida | Salida de consola enriquecida y logging sencillo. | Logs legibles y consolas con formato. | &#9744; |
| [prometheus-client](https://prometheus.github.io/client_python/) | Monitorización | Expone métricas para Prometheus. | Instrumentar servicios y exportar métricas. | &#9744; |
| [opentelemetry-sdk](https://opentelemetry.io/docs/languages/python/) | Observabilidad | Trazas y métricas distribuidas estándar. | Instrumentar aplicaciones para observabilidad. | &#9744; |
| [pytest](https://docs.pytest.org/en/stable/) | Testing | Framework de pruebas potente y extensible. | Escribir y ejecutar pruebas automatizadas. | &#9744; |
| [pre-commit](https://pre-commit.com/) | Calidad de Código | Ejecuta hooks antes de cada commit. | Asegurar formato y linting automáticos. | &#9744; |
| [black](https://black.readthedocs.io/en/stable/) / [ruff](https://docs.astral.sh/ruff/) | Formato / Linting | Formateo y análisis estático de código. | Mantener un estilo y detectar errores temprano. | &#9744; |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Tipado | Comprobación estática de tipos. | Detectar errores de tipos antes de ejecutar. | &#9744; |

### 💰 FinTech

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [yfinance](https://ranaroussi.github.io/yfinance/) | Datos de Mercado | Descarga datos históricos y en vivo de Yahoo Finance. | Análisis de acciones, ETFs y criptomonedas. | &#9744; |
| [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) | Datos de Mercado | Accede a múltiples fuentes de datos financieros. | Obtener series macroeconómicas y de mercado. | &#9744; |
| [ccxt](https://docs.ccxt.com/) | Criptomonedas | Librería unificada para decenas de exchanges cripto. | Trading algorítmico y arbitraje entre exchanges. | &#9744; |
| [alpaca-py](https://alpaca.markets/docs/) | Trading | SDK de Alpaca para trading comisionado cero. | Operar acciones y cripto de forma automatizada. | &#9744; |
| [ib_insync](https://ib-insync.readthedocs.io/) | Trading | Interactúa con Interactive Brokers. | Trading algorítmico sobre mercados globales. | &#9744; |
| [backtrader](https://www.backtrader.com/docu/) | Backtesting | Framework de backtesting y trading en vivo. | Probar estrategias con datos históricos. | &#9744; |
| [zipline-reloaded](https://zipline.ml4trading.io/) | Backtesting | Motor de backtesting usado por Quantopian. | Desarrollar y validar estrategias cuantitativas. | &#9744; |
| [QuantLib](https://www.quantlib.org/) | Derivados | Librería de valoración de instrumentos financieros. | Precio de opciones y modelos de tipos de interés. | &#9744; |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Indicadores | Indicadores técnicos sobre dataframes de pandas. | Calcular medias, RSI, MACD y más. | &#9744; |
| [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/) | Indicadores | Amplia colección de indicadores técnicos. | Análisis técnico de series de precios. | &#9744; |
| [stockstats](https://github.com/jealous/stockstats) | Indicadores | Añade columnas de indicadores a un DataFrame. | Análisis técnico rápido sobre datos OHLC. | &#9744; |
| [finnhub-python](https://finnhub.io/docs/api) | Datos de Mercado | Cliente de la API de Finnhub. | Noticias y datos fundamentales de empresas. | &#9744; |
| [polygon-api-client](https://polygon.io/docs/) | Datos de Mercado | Cliente de datos de mercado de Polygon.io. | Datos de alta calidad para estrategias. | &#9744; |
| [stripe](https://stripe.com/docs/api) | Pagos | SDK oficial de Stripe. | Cobros online, suscripciones y facturación. | &#9744; |
| [plaid-python](https://plaid.com/docs/) | Banca | Conexión con cuentas bancarias vía Plaid. | Agregación bancaria y verificación de fondos. | &#9744; |
| [paypalrestsdk](https://developer.paypal.com/) | Pagos | Integración con PayPal. | Procesar pagos con PayPal. | &#9744; |
| [cryptofeed](https://github.com/bmoscon/cryptofeed) | Criptomonedas | Streams de datos de exchanges en tiempo real. | Datos de order book y trades en vivo. | &#9744; |
| [web3](https://web3py.readthedocs.io/en/stable/) | Blockchain | Interactúa con la blockchain de Ethereum. | DApps, contratos y monederos en Python. | &#9744; |
| [pycoingecko](https://github.com/man-c/pycoingecko) | Criptomonedas | Cliente de la API de CoinGecko. | Precios y datos de mercado de cripto. | &#9744; |

### 🧠 IA / AI

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [tensorflow](https://www.tensorflow.org/api_docs/python/tf) | Deep Learning | Framework de deep learning de Google. | Redes neuronales y despliegue en producción. | &#9744; |
| [torch](https://pytorch.org/docs/stable/index.html) | Deep Learning | Framework de deep learning de Meta, muy usado en investigación. | Entrenamiento de redes neuronales y modelos custom. | &#9744; |
| [keras](https://keras.io/api/) | Deep Learning | API de alto nivel para construir redes neuronales. | Prototipado rápido de modelos de deep learning. | &#9744; |
| [transformers](https://huggingface.co/docs/transformers/index) | NLP / LLM | Modelos preentrenados (BERT, GPT, etc.) de Hugging Face. | NLP, resumen, traducción y fine-tuning. | &#9744; |
| [datasets](https://huggingface.co/docs/datasets/index) | Datos | Carga y procesa datasets de Hugging Face. | Preparar datos para entrenar modelos. | &#9744; |
| [sentence-transformers](https://www.sbert.net/) | Embeddings | Genera embeddings de frases y documentos. | Búsqueda semántica y similitud de texto. | &#9744; |
| [openai](https://platform.openai.com/docs/) | LLM API | Cliente oficial de la API de OpenAI. | Usar GPT para texto, visión y audio. | &#9744; |
| [anthropic](https://docs.anthropic.com/) | LLM API | Cliente de la API de Anthropic (Claude). | Asistentes y generación con Claude. | &#9744; |
| [google-generativeai](https://ai.google.dev/) | LLM API | Cliente de los modelos Gemini de Google. | Generación multimodal con Gemini. | &#9744; |
| [langchain](https://python.langchain.com/docs/) | Orquestación LLM | Framework para apps con LLMs, cadenas y agentes. | Construir asistentes, RAG y agentes. | &#9744; |
| [langgraph](https://langchain-ai.github.io/langgraph/) | Orquestación LLM | Grafos de estado para agentes con LLMs. | Flujos de agentes complejos y con memoria. | &#9744; |
| [llama-index](https://docs.llamaindex.ai/) | RAG | Framework de RAG e indexación de documentos. | Preguntas sobre tus propios documentos. | &#9744; |
| [chromadb](https://docs.trychroma.com/) | Vector DB | Base de datos vectorial embebida. | Almacenar embeddings para búsqueda semántica. | &#9744; |
| [faiss-cpu](https://faiss.ai/) | Vector DB | Búsqueda de similitud eficiente de vectores. | Recuperación rápida en millones de vectores. | &#9744; |
| [gymnasium](https://gymnasium.farama.org/) | Reinforcement Learning | Entornos estándar de RL. | Entrenar y evaluar agentes de refuerzo. | &#9744; |
| [stable-baselines3](https://stable-baselines3.readthedocs.io/en/master/) | Reinforcement Learning | Implementaciones fiables de algoritmos de RL. | Prototipar agentes de RL rápidamente. | &#9744; |
| [pytorch-lightning](https://lightning.ai/docs/pytorch/stable/) | Deep Learning | Abstracción de entrenamiento sobre PyTorch. | Entrenamiento escalable y ordenado. | &#9744; |
| [diffusers](https://huggingface.co/docs/diffusers/index) | Generación | Modelos de difusión para imágenes y audio. | Generar imágenes con Stable Diffusion. | &#9744; |
| [ultralytics](https://docs.ultralytics.com/) | Visión | Modelos YOLO de detección de objetos. | Detección y segmentación en tiempo real. | &#9744; |
| [mediapipe](https://ai.google.dev/edge/mediapipe/solutions/guide) | Visión | Soluciones de visión y pose de Google. | Seguimiento de manos, rostro y cuerpo. | &#9744; |
| [openai-whisper](https://github.com/openai/whisper) | Audio | Reconocimiento de voz multilingüe. | Transcribir audio a texto. | &#9744; |
| [pytesseract](https://github.com/madmaze/pytesseract) | OCR | OCR mediante el motor Tesseract. | Extraer texto de imágenes. | &#9744; |
| [prophet](https://facebook.github.io/prophet/) | Series Temporales | Pronóstico de series temporales de Meta. | Predicciones de demanda y tendencias. | &#9744; |
| [mlflow](https://mlflow.org/docs/latest/index.html) | MLOps | Gestión del ciclo de vida de modelos ML. | Registrar experimentos y desplegar modelos. | &#9744; |
| [wandb](https://docs.wandb.ai/) | MLOps | Seguimiento de experimentos y métricas. | Visualizar entrenamientos y compararlos. | &#9744; |
| [peft](https://huggingface.co/docs/peft/index) | Fine-tuning | Fine-tuning eficiente de modelos grandes (LoRA). | Adaptar LLMs con pocos recursos. | &#9744; |
| [crewai](https://docs.crewai.com/) | Agentes | Framework para equipos de agentes IA. | Orquestar múltiples agentes colaborativos. | &#9744; |

### 📡 IoT

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [paho-mqtt](https://eclipse.dev/paho/index.php?page=clients/python/index.php) | Protocolos | Cliente MQTT para mensajería ligera entre dispositivos. | Comunicación de sensores y actuadores vía broker. | &#9744; |
| [aiomqtt](https://sbtinstruments.github.io/aiomqtt/) | Protocolos | Cliente MQTT asíncrono basado en asyncio. | IoT concurrente de alto rendimiento. | &#9744; |
| [pyserial](https://pyserial.readthedocs.io/en/latest/) | Comunicación | Comunicación por puerto serie. | Conectar Arduino, ESP32 y sensores serie. | &#9744; |
| [pymodbus](https://pymodbus.readthedocs.io/en/latest/) | Protocolos | Implementación del protocolo industrial Modbus. | Leer PLCs y equipos industriales. | &#9744; |
| [asyncua](https://python-opcua.readthedocs.io/) | Protocolos | Cliente y servidor OPC UA. | Comunicación industrial estandarizada. | &#9744; |
| [gpiozero](https://gpiozero.readthedocs.io/en/stable/) | Hardware | Control sencillo de pines GPIO en Raspberry Pi. | Leer botones y controlar LEDs y relés. | &#9744; |
| [RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) | Hardware | Acceso de bajo nivel a los GPIO de Raspberry Pi. | Control directo de hardware en la Pi. | &#9744; |
| [adafruit-blinka](https://docs.circuitpython.org/projects/blinka/en/latest/) | Hardware | Emula CircuitPython sobre placas SBC. | Usar librerías Adafruit en Raspberry Pi. | &#9744; |
| [smbus2](https://smbus2.readthedocs.io/en/latest/) | Hardware | Acceso al bus I2C. | Comunicar con sensores y pantallas I2C. | &#9744; |
| [spidev](https://github.com/doceme/py-spidev) | Hardware | Acceso al bus SPI. | Conectar dispositivos de alta velocidad por SPI. | &#9744; |
| [esptool](https://docs.espressif.com/projects/esptool/en/latest/) | Microcontroladores | Flashea firmware en chips ESP. | Programar ESP8266 y ESP32. | &#9744; |
| [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) | Microcontroladores | Gestiona placas con MicroPython. | Subir y ejecutar código en microcontroladores. | &#9744; |
| [python-kasa](https://python-kasa.readthedocs.io/en/latest/) | Domótica | Controla dispositivos TP-Link Kasa. | Encender y apagar enchufes y bombillas inteligentes. | &#9744; |
| [tuya-connector](https://github.com/tuya/tuya-connector-python) | Domótica | Integra dispositivos de la nube Tuya. | Controlar dispositivos Tuya vía API. | &#9744; |
| [bleak](https://bleak.readthedocs.io/en/latest/) | Bluetooth | Cliente Bluetooth Low Energy multiplataforma. | Comunicar con sensores BLE. | &#9744; |
| [influxdb-client](https://influxdb-client.readthedocs.io/en/stable/) | Datos | Cliente de InfluxDB para series temporales. | Guardar y consultar telemetría IoT. | &#9744; |

### 🛠️ Administración de Sistemas

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [paramiko](https://docs.paramiko.org/en/stable/) | SSH | Implementación de SSH en Python. | Ejecutar comandos y transferir archivos remotos. | &#9744; |
| [fabric](https://docs.fabfile.org/en/stable/) | Automatización | Ejecuta tareas de administración sobre múltiples hosts. | Despliegues y mantenimiento remoto. | &#9744; |
| [psutil](https://psutil.readthedocs.io/stable/) | Monitorización | Recupera información de procesos y recursos. | Monitorizar CPU, RAM, disco y red. | &#9744; |
| [distro](https://distro.readthedocs.io/en/latest/) | Sistema | Detecta la distribución de Linux. | Adaptar scripts a cada distro. | &#9744; |
| [netifaces](https://netifaces.readthedocs.io/en/stable/) | Red | Información de interfaces y direcciones de red. | Inventariar configuración de red local. | &#9744; |
| [python-crontab](https://pypi.org/project/python-crontab/) | Programación | Gestiona tareas cron desde Python. | Crear y editar crontabs programáticamente. | &#9744; |
| [croniter](https://github.com/kiorky/croniter) | Programación | Interpreta y calcula expresiones cron. | Determinar próximas ejecuciones de tareas. | &#9744; |
| [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) | Configuración | Parseo de archivos YAML. | Leer configs de servicios e infraestructura. | &#9744; |
| [ansible](https://docs.ansible.com/ansible/latest/) | Configuración | Automatización de configuración sin agente. | Aprovisionar y mantener flotas de servidores. | &#9744; |
| [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) | Cloud | SDK de AWS. | Administrar recursos cloud por código. | &#9744; |
| [docker](https://docker-py.readthedocs.io/en/stable/) | Contenedores | SDK de la API de Docker. | Automatizar gestión de contenedores. | &#9744; |
| [kubernetes](https://kubernetes.io/docs/reference/using-api/client-libraries/) | Orquestación | Cliente de la API de Kubernetes. | Administrar clústeres y workloads. | &#9744; |
| [pyvmomi](https://github.com/vmware/pyvmomi) | Virtualización | SDK de VMware vSphere. | Gestionar máquinas virtuales VMware. | &#9744; |
| [libvirt-python](https://libvirt.org/python.html) | Virtualización | Enlaces de libvirt para KVM/QEMU. | Administrar VMs en Linux. | &#9744; |
| [ldap3](https://ldap3.readthedocs.io/en/latest/) | Directorios | Cliente LDAP puro en Python. | Autenticación y consultas en Active Directory. | &#9744; |
| [cryptography](https://cryptography.io/en/latest/) | Seguridad | Primitivas criptográficas modernas. | Cifrado, firmas y gestión de certificados. | &#9744; |
| [scapy](https://scapy.readthedocs.io/en/latest/) | Redes | Manipulación de paquetes de red. | Sniffing, escaneo y análisis de tráfico. | &#9744; |
| [netaddr](https://netaddr.readthedocs.io/en/latest/) | Redes | Trabajo con direcciones y rangos de red. | Calcular subredes y validar IPs. | &#9744; |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | Redes | Mide velocidad de conexión. | Monitorizar el ancho de banda del enlace. | &#9744; |

### 📱 Apps Para Teléfonos

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [kivy](https://kivy.org/doc/stable/) | Framework Móvil | Framework multiplataforma con soporte táctil. | Apps móviles y de escritorio con una sola base. | &#9744; |
| [kivymd](https://kivymd.readthedocs.io/en/latest/) | UI Móvil | Implementa Material Design sobre Kivy. | Interfaces con estética Android moderna. | &#9744; |
| [buildozer](https://buildozer.readthedocs.io/en/latest/) | Empaquetado | Empaqueta apps Kivy para Android/iOS. | Compilar APKs listas para instalar. | &#9744; |
| [briefcase](https://briefcase.readthedocs.io/en/stable/) | Empaquetado | Empaqueta apps con BeeWare para múltiples plataformas. | Distribuir apps nativas de escritorio y móvil. | &#9744; |
| [toga](https://toga.readthedocs.io/en/latest/) | Framework Móvil | UI nativa multiplataforma de BeeWare. | Apps con widgets nativos del sistema. | &#9744; |
| [flet](https://flet.dev/docs/) | Framework Móvil | Construye apps multiplataforma con Flutter en Python. | Apps móviles y web con una sola base. | &#9744; |
| [plyer](https://plyer.readthedocs.io/en/latest/) | APIs Nativas | Accede a funciones del dispositivo (GPS, cámara, etc.). | Usar hardware del móvil de forma portable. | &#9744; |
| [pyjnius](https://pyjnius.readthedocs.io/en/latest/) | Puentes | Accede a clases Java desde Python. | Integrar APIs Android nativas. | &#9744; |
| [pyobjus](https://pyobjus.readthedocs.io/en/latest/) | Puentes | Accede a clases Objective-C desde Python. | Integrar APIs nativas de iOS. | &#9744; |
| [appium-python-client](https://appium.github.io/python-client-sphinx/) | Testing | Cliente de Appium para automatizar apps móviles. | Pruebas automatizadas en Android e iOS. | &#9744; |
| [uiautomator2](https://github.com/openatx/uiautomator2) | Automatización | Controla dispositivos Android desde Python. | Automatizar la UI de un teléfono Android. | &#9744; |

### 🎮 Videojuegos

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [pygame](https://www.pygame.org/docs/) | Motor 2D | La librería clásica para juegos 2D en Python. | Prototipos, juegos 2D y educación. | &#9744; |
| [pyglet](https://pyglet.readthedocs.io/en/latest/) | Motor 2D/3D | Framework multimedia ligero y multiplataforma. | Juegos y apps gráficas con OpenGL. | &#9744; |
| [arcade](https://api.arcade.academy/en/latest/) | Motor 2D | Framework moderno y sencillo para juegos 2D. | Juegos 2D con sprites y físicas simples. | &#9744; |
| [panda3d](https://docs.panda3d.org/1.10/python/index) | Motor 3D | Motor 3D completo para juegos y simulaciones. | Juegos 3D, visualizaciones y simuladores. | &#9744; |
| [moderngl](https://moderngl.readthedocs.io/en/latest/) | Gráficos | Envoltorio de OpenGL moderno. | Renderizado de alto rendimiento personalizado. | &#9744; |
| [ursina](https://www.ursinaengine.org/documentation.html) | Motor 3D | Motor 3D fácil de usar sobre Panda3D. | Juegos 3D y prototipos rápidos. | &#9744; |
| [PyOpenGL](https://pyopengl.sourceforge.net/documentation/) | Gráficos | Enlaces a OpenGL. | Renderizado gráfico de bajo nivel. | &#9744; |
| [pymunk](https://www.pymunk.org/en/latest/) | Físicas | Motor de físicas 2D (Chipmunk). | Simular colisiones y cuerpos rígidos 2D. | &#9744; |
| [Box2D](https://github.com/pybox2d/pybox2d) | Físicas | Enlaces del motor de físicas Box2D. | Físicas 2D realistas en juegos. | &#9744; |
| [pytmx](https://pytmx.readthedocs.io/en/latest/) | Niveles | Carga mapas TMX de Tiled. | Diseñar niveles para juegos 2D. | &#9744; |
| [pygame-menu](https://pygame-menu.readthedocs.io/en/latest/) | UI de Juegos | Crea menús para juegos con pygame. | Menús, opciones y pausas. | &#9744; |
| [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/) | UI de Juegos | Sistema de UI para pygame. | Botones, sliders y ventanas en juegos. | &#9744; |
| [pybullet](https://pybullet.org/wordpress/) | Físicas 3D | Simulación de físicas y robótica 3D. | Simuladores de robótica y físicas 3D. | &#9744; |
| [harfang3d](https://www.harfang3d.com/documentation/) | Motor 3D | Motor 3D ligero y multiplataforma. | Juegos 3D y apps de realidad virtual. | &#9744; |

### 🌐 Desarrollo Web (Back-End)

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [flask](https://flask.palletsprojects.com/en/stable/) | Microframework | Microframework web minimalista y flexible. | APIs y apps web ligeras. | &#9744; |
| [django](https://docs.djangoproject.com/en/stable/) | Framework Full-Stack | Framework completo con ORM, admin y auth incluidos. | Aplicaciones web grandes y rápidas de arrancar. | &#9744; |
| [fastapi](https://fastapi.tiangolo.com/) | API Framework | Framework moderno de APIs con tipado y async. | APIs REST de alto rendimiento y documentadas. | &#9744; |
| [starlette](https://www.starlette.io/) | API Framework | Framework ASGI ligero, base de FastAPI. | Servicios async de bajo nivel. | &#9744; |
| [uvicorn](https://www.uvicorn.org/) | Servidor | Servidor ASGI rápido. | Servir apps async en desarrollo y producción. | &#9744; |
| [gunicorn](https://docs.gunicorn.org/en/stable/) | Servidor | Servidor WSGI de producción. | Desplegar apps WSGI de forma robusta. | &#9744; |
| [aiohttp](https://docs.aiohttp.org/en/stable/) | Async | Cliente y servidor HTTP asíncronos. | APIs y clientes concurrentes de alto rendimiento. | &#9744; |
| [sqlalchemy](https://docs.sqlalchemy.org/en/20/) | ORM | ORM y toolkit SQL potente. | Modelar y consultar bases de datos relacionales. | &#9744; |
| [alembic](https://alembic.sqlalchemy.org/en/latest/) | Migraciones | Migraciones de base de datos para SQLAlchemy. | Evolucionar el esquema sin perder datos. | &#9744; |
| [pydantic](https://docs.pydantic.dev/latest/) | Validación | Validación y serialización de datos con tipos. | Validar payloads y configuraciones. | &#9744; |
| [psycopg2-binary](https://www.psycopg.org/docs/) | Base de Datos | Driver de PostgreSQL. | Conectar apps con PostgreSQL. | &#9744; |
| [pymongo](https://pymongo.readthedocs.io/en/stable/) | Base de Datos | Cliente de MongoDB. | Persistencia NoSQL en apps web. | &#9744; |
| [redis](https://redis-py.readthedocs.io/en/stable/) | Base de Datos | Cliente de Redis. | Caché y sesiones de aplicaciones web. | &#9744; |
| [jinja2](https://jinja.palletsprojects.com/en/stable/) | Plantillas | Motor de plantillas HTML. | Renderizar páginas del lado del servidor. | &#9744; |
| [celery](https://docs.celeryq.dev/en/stable/) | Colas | Cola de tareas distribuidas. | Ejecutar trabajos pesados en segundo plano. | &#9744; |
| [httpx](https://www.python-httpx.org/) | HTTP | Cliente HTTP moderno con soporte async. | Consumir APIs externas desde el back-end. | &#9744; |
| [websockets](https://websockets.readthedocs.io/en/stable/) | Tiempo Real | Implementación del protocolo WebSocket. | Chat y datos en tiempo real. | &#9744; |
| [strawberry-graphql](https://strawberry.rocks/docs) | GraphQL | Framework GraphQL basado en tipos. | Construir APIs GraphQL en Python. | &#9744; |
| [djangorestframework](https://www.django-rest-framework.org/) | API Framework | Toolkit para construir APIs REST con Django. | APIs robustas sobre proyectos Django. | &#9744; |

### 🕸️ Web Scraping

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [requests](https://requests.readthedocs.io/en/latest/) | HTTP | La librería HTTP más popular de Python. | Hacer peticiones a páginas y APIs. | &#9744; |
| [httpx](https://www.python-httpx.org/) | HTTP | Cliente HTTP moderno con async y HTTP/2. | Scraping concurrente de alto rendimiento. | &#9744; |
| [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Parsing HTML | Parsea y navega HTML de forma tolerante. | Extraer datos de páginas web. | &#9744; |
| [lxml](https://lxml.de/) | Parsing HTML | Parser HTML/XML rápido basado en C. | Procesar HTML/XML a gran velocidad. | &#9744; |
| [scrapy](https://docs.scrapy.org/en/latest/) | Framework | Framework completo de scraping con spiders. | Crawlers y pipelines de scraping a gran escala. | &#9744; |
| [selenium](https://selenium-python.readthedocs.io/) | Navegador | Automatiza navegadores reales. | Scraping de sitios con JavaScript. | &#9744; |
| [playwright](https://playwright.dev/python/) | Navegador | Automatización de navegadores moderna y rápida. | Scraping dinámico y flujos complejos. | &#9744; |
| [mechanicalsoup](https://mechanicalsoup.readthedocs.io/en/stable/) | Navegador | Navegación sencilla sobre requests y BeautifulSoup. | Rellenar y enviar formularios fácilmente. | &#9744; |
| [requests-html](https://requests.readthedocs.io/projects/requests-html/en/latest/) | Navegador | HTML renderizado con JavaScript sobre requests. | Scraping sencillo de páginas dinámicas. | &#9744; |
| [pyquery](https://pythonhosted.org/pyquery/) | Parsing HTML | Selecciones tipo jQuery sobre HTML. | Extraer datos con selectores CSS concisos. | &#9744; |
| [parsel](https://parsel.readthedocs.io/en/latest/) | Parsing HTML | Selectores XPath/CSS usados por Scrapy. | Extraer datos de HTML/XML. | &#9744; |
| [fake-useragent](https://fake-useragent.readthedocs.io/en/latest/) | Antibot | Genera user-agents aleatorios. | Evitar bloqueos por huella del navegador. | &#9744; |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Antibot | Resuelve retos de Cloudflare. | Scrapear sitios protegidos por Cloudflare. | &#9744; |
| [selenium-wire](https://github.com/wkeeling/selenium-wire) | Antibot | Inspecciona tráfico de red en Selenium. | Capturar peticiones y respuestas. | &#9744; |
| [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | Antibot | Chrome Driver indetectable. | Evitar la detección de bots. | &#9744; |
| [curl-cffi](https://curl-cffi.readthedocs.io/en/latest/) | HTTP | Imita la huella de curl/navegadores. | Bypassear protecciones TLS y antibot. | &#9744; |
| [newspaper3k](https://newspaper.readthedocs.io/en/latest/) | Extracción | Extrae artículos y noticias. | Recopilar y analizar noticias. | &#9744; |
| [trafilatura](https://trafilatura.readthedocs.io/en/latest/) | Extracción | Extrae el contenido principal de páginas. | Obtener texto limpio de artículos. | &#9744; |
