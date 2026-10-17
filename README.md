<div align="center">

![Banner](./banner.png)

# pyessentials - Library Meta-Installer for Python

</div>

## 📋 Table of Contents / Indice

[🇬🇧 English](#-english-guide) | [🇪🇸 Español](#-guía-en-español)

**English Content:**

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Prerequisites](#-prerequisites)
- [🚀 Usage](#-usage)
- [🖥️ Interactive Menu](#️-interactive-menu)
- [📌 Available Arguments](#-available-arguments)
- [🎯 Quick Example](#-quick-example)

  

**Contenido en Español:**
- [📖 Descripción general](#-Overview)
- [✨ Características](#-caracteristicas)
- [🛠️ Requisitos previos](#-requisitos-previos)
- [🚀 Uso](#-uso)
- [🖥️ Menú Interactivo](#️-menú-interactivo)
- [📌 Argumentos Disponibles](#-argumentos-disponibles)
- [🎯 Ejemplo](#-ejemplo)

---

## 🇬🇧 English Guide

## 📖 Overview

**pyessentials** is a command-line utility designed to simplify your Python development workflow. It allows you to bulk-install groups of libraries and APIs organized into specialized development domains ("programming campuses"), adapting automatically to your active operating system.

**pyessentials** es una herramienta de línea de comandos diseñada para simplificar la configuración del entorno de desarrollo de Python. Permite instalar de forma masiva grupos de librerías y APIs organizadas por categorías especializadas ("campus de programación"), adaptándose automáticamente al sistema operativo detectado.


## ✨ Features

*   **Modular Installation:** Choose the exact category of libraries you need based on your study field or project target.
*   **Interactive Menu:** Run the script with no arguments to get a numbered menu of every campus, then drill into a category to see its full package list.
*   **Individual Package Selection:** Inside a category you can install a single library, a custom set (e.g. `1,3,5`), or the whole category with `0`, giving you full control instead of a forced bulk install.
*   **Cross-Platform Support:** Automatically detects whether you are running on Windows (using `pip`) or Linux/macOS (using `pip3`).
*   **Safe & Optimized Execution:** Leverages structural list unpacking using the `*` operator to feed external subprocess arguments reliably.
*   **Sleek Terminal Output:** Features a distinctive ASCII banner and native interactive hyperlinks using ANSI escape sequences directly in the shell.



## 🛠️ Prerequisites

*   **Python 3.x** installed and configured on your operating system.
*   The **pip** or **pip3** package manager added correctly to your system's environment variables (`PATH`).
*   Using a virtual environment (venv) is highly recommended to avoid package conflicts.



## 🚀 Usage

To execute the meta-installer, open a terminal window in the directory where the script is located and pass the flag corresponding to your desired category.

### Basic Syntax

**On Windows Systems:**
```bash
python pyessentials.py [Argument]
