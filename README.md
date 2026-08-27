# pyessentials - Library Meta-Installer for Python


## 📋 Table of Contents / Indice

[🇬🇧 English](#-english-guide) | [🇪🇸 Español](#-guía-en-español)

**English Content:**

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Prerequisites](#-prerequisites)
- [🚀 Usage](#-usage)
- [📌 Available Arguments](#-available-arguments)
- [🎯 Quick Example](#-quick-example)

  

**Contenido en Español:**
- [📖 Descripción general](#-Overview)
- [✨ Características](#-caracteristicas)
- [🛠️ Requisitos previos](#-requisitos-previos)
- [🚀 Uso](#-uso)
- [📌 Argumentos Disponibles](#-argumentos-disponibles)
- [🎯 Ejemplo](#-ejemplo)

---

## 🇬🇧 English Guide

### 📖 Overview

**pyessentials** is a command-line utility designed to simplify your Python development workflow. It allows you to bulk-install groups of libraries and APIs organized into specialized development domains ("programming campuses"), adapting automatically to your active operating system.

**pyessentials** es una herramienta de línea de comandos diseñada para simplificar la configuración del entorno de desarrollo de Python. Permite instalar de forma masiva grupos de librerías y APIs organizadas por categorías especializadas ("campus de programación"), adaptándose automáticamente al sistema operativo detectado.


### ✨ Features

*   **Modular Installation:** Choose the exact category of libraries you need based on your study field or project target.
*   **Cross-Platform Support:** Automatically detects whether you are running on Windows (using `pip`) or Linux/macOS (using `pip3`).
*   **Safe & Optimized Execution:** Leverages structural list unpacking using the `*` operator to feed external subprocess arguments reliably.
*   **Sleek Terminal Output:** Features a distinctive ASCII banner and native interactive hyperlinks using ANSI escape sequences directly in the shell.



### 🛠️ Prerequisites

*   **Python 3.x** installed and configured on your operating system.
*   The **pip** or **pip3** package manager added correctly to your system's environment variables (`PATH`).
*   Using a virtual environment (venv) is highly recommended to avoid package conflicts.



### 🚀 Usage

To execute the meta-installer, open a terminal window in the directory where the script is located and pass the flag corresponding to your desired category.

#### Basic Syntax

**On Windows Systems:**
```bash
python pyessentials.py [Argument]
```

**On Linux / macOS Systems:**
```bash
python3 pyessentials.py [Argument]
```

*If you execute the script **without any arguments**, the program will display a welcome message listing the available categories along with a direct link to the project repository so you can review the details for each one.*


### 📌 Available Arguments

If you want to see the list of APIs / Libraries on every campus [click here](./List_EN.md) 

You can pass the `-h` flag at any time to display the help menu with detailed descriptions. The currently supported arguments are:

| Flag | Category | Complete |
| :--- | :--- | :---: |
| `-A` | **All-In** | ***Temporaly*** |
| `-a` | **Automation** | &#9745; |
| `-b` | **Big Data** | &#9744; |
| `-B` | **Bots** | &#9745; |
| `-d` | **Data Science** | &#9744; |
| `-D` | **Desktop Apps** | &#9744; |
| `-V` | **Data Viz** | &#9744; |
| `-o` | **DevOPS** | &#9744; |
| `-f` | **FinTech** | &#9744; |
| `-I` | **IA / AI** | &#9744; |
| `-i` | **IoT** | &#9744; |
| `-s` | **SysAdmin** | &#9744; |
| `-p` | **Phone Apps** | &#9744; |
| `-v` | **Videogames** | &#9744; |
| `-w` | **Web (Back-End)**| &#9744; |
| `-S` | **Web Scraping** | &#9744; |
| `-h` | **Help** | &#9745; |



### 🎯 Quick Example

If you want to start learning the Automation track and need to prepare your environment inside a Linux terminal, simply run:

```bash
python3 pyessentials.py -B
```

The script will render the custom banner and trigger the bulk installation of the required dependencies seamlessly without further manual tasks.

---

## 🇪🇸 Guía en Español


### ✨ Características

*   **Instalación Modular:** Elige la categoría exacta de librerías que necesitas según tu área de estudio o trabajo.
*   **Multiplataforma:** Detecta automáticamente si estás en Windows (usando `pip`) o en Linux/macOS (usando `pip3`).
*   **Seguridad y Optimización:** Concatenación y desempaquetado estructurado mediante el uso del operador `*` en los argumentos de ejecución.
*   **Interfaz Atractiva:** Incluye un banner ASCII distintivo y enlaces integrados nativos en la consola mediante códigos de escape ANSI.



### 🛠️ Requisitos previos

*   **Python 3.x** instalado en el sistema operativo.
*   El administrador de paquetes **pip** o **pip3** configurado correctamente en las variables de entorno (`PATH`).
*   Se sugiere ejecutar este instalador dentro de un venv (Espacio Virtual) para proteger la integridad de tus paquetes globales.


### 🚀 Uso

Para ejecutar el instalador, abre una terminal en la ruta donde se encuentra guardado el script y pásale el argumento correspondiente a la categoría deseada.

#### Sintaxis básica

**En sistemas Windows:**
```bash
python pyessentials.py [Argumento]
```

**En sistemas Linux / macOS:**
```bash
python3 pyessentials.py [Argumento]
```

*Si ejecutas el script **sin argumentos**, el programa mostrará un mensaje de bienvenida que enumera las categorías disponibles junto con un enlace directo al repositorio del proyecto para que puedas consultar los detalles de cada una.*


### 📌 Argumentos Disponibles

Si quieres ver la lista de APIs / Librerias de cada campus, [haz click aquí](./List_ES.md)

Puedes usar el parámetro `-h` para desplegar el menú de ayuda con la descripción detallada. Las opciones soportadas actualmente son:

| Argumento | Categoría | Terminado |
| :--- | :--- | :---: |
| `-A` | **All-In** | ***Temporalmente*** |
| `-a` | **Automation** | &#9745; |
| `-b` | **Big Data** | &#9744; |
| `-B` | **Bots** | &#9745; |
| `-d` | **Data Science** | &#9744; |
| `-D` | **Desktop Apps** | &#9744; |
| `-V` | **Data Viz** | &#9744; |
| `-o` | **DevOPS** | &#9744; |
| `-f` | **FinTech** | &#9744; |
| `-I` | **IA / AI** | &#9744; |
| `-i` | **IoT** | &#9744; |
| `-s` | **SysAdmin** | &#9744; |
| `-p` | **Phone Apps** | &#9744; |
| `-v` | **Videogames** | &#9744; |
| `-w` | **Web (Back-End)**| &#9744; |
| `-S` | **Web Scraping** | &#9744; |
| `-h` | **Help** | &#9745; |

---

### 🎯 Ejemplo

Si vas a iniciar en el campus de automatización y necesitas preparar tu entorno en un sistema Linux, abre la terminal y escribe:

```bash
python3 pyessentials.py -B
```

El script mostrará el banner principal e iniciará la instalación en bloque de las dependencias requeridas sin intervención manual adicional.
