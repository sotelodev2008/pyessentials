<div align="right">

###### Hecho por ***Sotelo***

</div>

<div align="center">

# Pyessentials Lista

</div>

## Indice

- [⚙️ Automatización](#️-automatización)
- [🤖 Bots](#-bots)

### ⚙️ Automatización

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | Automatización Ofimática | Modifica, lee y crea archivos de Excel (.xlsx) de forma masiva sin necesidad de abrir el programa. | Generación de reportes financieros, inventarios y análisis de datos en formato Excel de manera automatizada. | &#9744; |
| [pypdf](https://pypdf.readthedocs.io/en/stable/) | Automatización Ofimática | Sirve para dividir, fusionar, rotar y extraer texto de miles de archivos PDF automáticamente. | Procesamiento masivo de documentos PDF como facturas, contratos o informes para archivado o extracción de datos. | &#9744; |
| [python-docx](https://python-docx.readthedocs.io/en/latest/) | Automatización Ofimática | Automatiza la creación y edición de informes y documentos de Word (.docx). | Generación automática de documentos corporativos, contratos personalizados y reportes con formato profesional. | &#9744; |
| [playwright](https://playwright.dev/) | Automatización Web | La librería moderna más rápida y fiable para automatizar Chrome, Firefox y Safari. Es la favorita actual de la industria. | Pruebas end-to-end de aplicaciones web modernas, scraping dinámico y automatización de flujos de trabajo complejos en el navegador. | &#9744; |
| [selenium](https://selenium-python.readthedocs.io/) | Automatización Web | El clásico de toda la vida. Más lento que Playwright, pero con una comunidad gigantesca y compatible con cualquier navegador viejo. | Automatización de navegadores legacy, pruebas de compatibilidad entre navegadores y scraping de sitios web tradicionales. | &#9744; |
| [netmiko](https://ktbyers.github.io/netmiko/docs/netmiko/index.html) | Automatización Web | Diseñada específicamente para automatizar la configuración de routers y switches de red (Cisco, Juniper, etc.). | Configuración masiva de equipos de red, backup de configuraciones y despliegue de cambios en infraestructuras de red empresariales. | &#9744; |
| [paramiko](https://docs.paramiko.org/en/stable/) | Automatización Web | Automatiza conexiones seguras por SSH para ejecutar comandos en servidores Linux remotos. | Administración remota de servidores, ejecución de scripts de mantenimiento y automatización de tareas en entornos Linux. | &#9744; |
| [keyboard](https://pypi.org/project/keyboard/) | Automatización de Archivos y Tareas | Librería para tomar control total del teclado, permitiendo escuchar y simular pulsaciones de teclas globales. | Creación de atajos de teclado del sistema (hotkeys), macros y automatización de tareas de escritorio. | &#9744; |
| [mouse](https://pypi.org/project/mouse/) | Automatización de Archivos y Tareas | Librería hermana de keyboard diseñada específicamente para el control y escucha de eventos del ratón. | Automatizar clics, arrastres de ventanas y coordenadas de pantalla. | &#9744; |
| [psutil](https://psutil.readthedocs.io/stable/) | Automatización de Archivos y Tareas | Automatiza la gestión del rendimiento del PC (controla el uso de CPU, RAM y los procesos abiertos). | Monitorización de recursos del sistema, detección de procesos que consumen demasiados recursos y generación de alertas de rendimiento. | &#9744; |
| [pyautogui](https://pyautogui.readthedocs.io/en/latest/) | Automatización de Archivos y Tareas | Controla el ratón y el teclado de forma virtual para hacer clics, escribir o arrastrar elementos de la pantalla automáticamente. | Automatización de interfaces gráficas que no tienen API, pruebas de usabilidad y ejecución de tareas repetitivas en aplicaciones de escritorio | &#9744; |
| [pyinput](https://pynput.readthedocs.io/en/latest/) | Automatización de Archivos y Tareas | Librería avanzada para controlar y monitorear los dispositivos de entrada (teclado y ratón) con soporte detallado de hilos. | Crear registradores de eventos (loggers) o controles personalizados dentro de aplicaciones de fondo. | &#9744; |
| [schedule](https://schedule.readthedocs.io/en/stable/) | Automatización de Archivos y Tareas | Permite programar tareas para que se ejecuten cada cierto tiempo usando una sintaxis muy sencilla | Programación de scripts recurrentes como backups automáticos, envío de reportes periódicos y tareas de mantenimiento programadas. | &#9744; |
| [watchdog](https://python-watchdog.readthedocs.io/en/stable/) | Automatización de Archivos y Tareas |  Vigila carpetas en tiempo real y ejecuta acciones si un archivo se crea, borra o modifica. | Sincronización de archivos entre carpetas, procesamiento automático de archivos entrantes y monitoreo de cambios en directorios críticos. | &#9744; |

### 🤖 Bots

| Libreria/Api | Categoria | Descripción | Uso Principal | Preinstalada |
| :--- | :--- | :--- | :--- | :---: |
| [opencv-python](https://docs.opencv.org/5.0/) | Bots de Simulación Visual | Librería avanzada que no usan APIs oficiales, sino que "ven" la pantalla como un humano para tomar decisiones. se usa muchísimo en bots de videojuegos junto a pyautogui. Permite al bot analizar la pantalla, buscar una imagen concreta (como un enemigo o un botón) y hacer clic sobre ella. | Detección de elementos en pantalla para automatización de videojuegos, bots de farming y sistemas de reconocimiento visual en tiempo real. | &#9744; |
| [alright](https://github.com/Kalebu/alright) | Bots para Mensajería | Librería basada en Selenium que automatiza WhatsApp Web sin necesidad de escanear el QR en cada envío (a diferencia de otras soluciones). | Envío masivo de mensajes de WhatsApp, bots de respuesta automatizada y gestión de conversaciones comerciales sin depender de APIs de pago. | &#9744; |
| [discord.py](https://discordpy.readthedocs.io/en/stable/) | Bots para Mensajería | La librería reina y estándar de la industria para crear bots interactivos en Discord. Soporta comandos de texto, botones y sistemas de audio. | Creación de bots de Discord para comunidades, sistemas de moderación automática, reproducción de audio en canales de voz y gestión de servidores. | &#9744; |
| [python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/) | Bots para Mensajería | Una librería excelente y muy mantenida para controlar la API de Telegram. Te permite hacer desde bots de comandos simples hasta menús interactivos complejos. | Desarrollo de bots de Telegram para atención al cliente, envío de notificaciones automatizadas, encuestas interactivas y sistemas de respuesta automática. | &#9744; |
| [pywhatkit](https://pypi.org/project/pywhatkit/) | Bots para Mensajería | La librería más popular y sencilla para automatizar WhatsApp. Usa [web.whatsapp.com](web.whatsapp.com) mediante el navegador para enviar mensajes programados. | Envío programado de mensajes de WhatsApp a contactos específicos en horarios determinados, automatización de recordatorios y notificaciones simples. | &#9744; |
| [twitchio](https://twitchio.dev) | Bots para Mensajería | Diseñada específicamente para crear bots de chat en Twitch, ideal para moderar canales, leer alertas o interactuar con los espectadores en vivo. | Moderación automatizada de chats de Twitch, respuesta a comandos de espectadores, gestión de puntos del canal y alertas personalizadas en streams. | &#9744; |
| [praw](https://praw.readthedocs.io/en/stable/) | Bots para Redes Sociales | La librería oficial para interactuar con Reddit. Te permite crear bots que moderen subreddits, respondan comentarios basados en palabras clave o publiquen hilos. | Moderación automática de subreddits, publicación programada de contenido, análisis de tendencias y respuesta automatizada a comentarios. | &#9744; |
| [tweepy](https://docs.tweepy.org/en/stable/) | Bots para Redes Sociales | La librería estándar para conectar con la API de X (anteriormente Twitter). Sirve para automatizar tweets, buscar hashtags o monitorizar cuentas en tiempo real. | Publicación automatizada de tweets, monitorización de hashtags y menciones, análisis de sentimiento en redes y gestión de cuentas de X/Twitter. | &#9744; |
