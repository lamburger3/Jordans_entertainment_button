import webbrowser
import time

funurls = ["www.youtube.com", "www.reddit.com", "www.github.com"]

def open_tabs(url_list):
    for url in url_list:
        webbrowser.open_new_tab(url)
def main():
    time.sleep(1)
    open_tabs(funurls)
    
main()
