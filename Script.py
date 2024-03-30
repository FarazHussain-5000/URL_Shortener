from flask import Flask, render_template, request, redirect
import string
import random
import secrets
import webbrowser

App = Flask(__name__)

# Dictionary To Store (Shortened_URL : Original_URL) As (Key :Value) Pairs.
URL_Dict = {}

def Open_Browser_Window():
    webbrowser.open_new_tab('http://127.0.0.1:5000/Home')

def Generate_Short_URLs():
    Characters = string.ascii_letters + string.digits
    Generated_Characters = [secrets.choice(Characters) for i in range(9)]
    Short_URL = ''.join(i for i in Generated_Characters)
    return Short_URL

@App.route('/Home')
def Index():
    return render_template('Index.html')

@App.route('/ShortenedURL', methods=['POST'])
def Shorten_URL():
    Original_URL = request.form['URL']
    Short_URL = Generate_Short_URLs()
    URL_Dict[Short_URL] = Original_URL
    return render_template('Shortener.html', Short_URL=Short_URL)

@App.route('/<Short_URL>')
def Redirect(Short_URL):
    Original_URL = URL_Dict.get(Short_URL)
    if Original_URL:
        return redirect(Original_URL)
    else:
        return "URL Not Found", 404

@App.route('/Display_Generated_URLs')
def Display_Generated_URLs():
    NumShortenedURLs = len(URL_Dict.items())
    return render_template('DisplayURLs.html', URL_Dict=URL_Dict, NumShortenedURLs=NumShortenedURLs)

if __name__ == '__main__':
    Open_Browser_Window()
    App.run(debug=True)