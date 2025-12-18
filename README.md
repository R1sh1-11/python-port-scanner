# Multi-Threaded Port Scanner

A fast network scanner written in Python. It utilizes **multi-threading** to scan ports concurrently, making it significantly faster than traditional scanners.

## Features
* **Multi-Threaded:** Uses 100 concurrent worker threads.
* **Queue-Based:** Efficient task management preventing race conditions.
* **Standard Library:** No external `pip install` required (Uses `socket`, `threading`, `queue`).
* **Clean Output:** Reports only open ports.

## Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/r1sh1-11/python-port-scanner.git](https://github.com/r1sh1-11/python-port-scanner.git)
    cd python-port-scanner
    ```

2.  **Run the scanner**
    ```bash
    python fast_scanner.py
    ```

3.  **Enter Target**
    * Enter a URL (for example: `scanme.nmap.org`) in the target variable.

## Disclaimer
This tool was made simply for **educational purposes only**. Do not port scan random networks unless you wanna be IP banned. 🙏