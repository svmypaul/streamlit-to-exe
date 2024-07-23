# streamlit to exe
 convert streamlit webapp to exe using webview python libary
'''
pyinstaller --onefile --noconsole --add-data "app_new.py;." --add-data "streamlit.exe;." app.py
'''
