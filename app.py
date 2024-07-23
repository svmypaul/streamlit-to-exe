import os
import threading
import webview
import subprocess
import sys
from pathlib import Path

def on_closed():
    streamlit_process.terminate()
    print('pywebview window is closed')

def on_closing():
    print('pywebview window is closing')

def on_shown():
    global streamlit_process
    script_path = Path(__file__).parent / "app_new.py"
    streamlit_path = Path(__file__).parent / 'streamlit.exe'  # Adjust this path as necessary
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    streamlit_process = subprocess.Popen([streamlit_path, 'run', script_path, '--server.headless', 'true'],
                                         startupinfo=startupinfo)
    print('pywebview window shown')

def on_minimized():
    print('pywebview window minimized')

def on_restored():
    print('pywebview window restored')

def on_maximized():
    print('pywebview window maximized')

def on_resized(width, height):
    print(
        'pywebview window is resized. new dimensions are {width} x {height}'.format(
            width=width, height=height
        )
    )

def on_loaded(window):
    print('DOM is ready')
    window.events.loaded -= on_loaded
    window.load_url('http://localhost:8501')

if __name__ == '__main__':
    window = webview.create_window(
        'Simple browser', 'http://localhost:8501', confirm_close=True
    )

    window.events.closed += on_closed
    window.events.closing += on_closing
    window.events.shown += on_shown
    window.events.loaded += on_loaded
    window.events.minimized += on_minimized
    window.events.maximized += on_maximized
    window.events.restored += on_restored
    window.events.resized += on_resized

    webview.start()
