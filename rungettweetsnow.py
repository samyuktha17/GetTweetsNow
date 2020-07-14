from flask import Flask, request, render_template, send_file
from source_tweets import *
import json

app = Flask(__name__)

@app.route('/')  
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def retfile():
    aname = request.form['aname'] #app name/dev name
    cak = request.form['cak'] # consumer access key
    cask = request.form['cask'] # consumer access secret key
    etype = request.form['etype'] # extraction type
    hashtag = request.form['hashtag'] # hashtag filter
    keywords = request.form['keywords'] # keyword filter
    fdate = request.form['fdate'] # from date
    tdate = request.form['tdate'] # to date
    ftime = request.form['ftime'] # from time
    ttime = request.form['ttime'] # to time
    #print(aname, cak, cask, etype)
    rs = get_file(aname, cak, cask, etype, hashtag, keywords, fdate, tdate, ftime, ttime)
    
    # json dump
    with open('C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\data.json','a',encoding = 'utf-8') as f:
        for tweet in rs.stream():
            # print('{0}: {1}'.format(str(n), tweet['created_at']))
            json.dump(tweet, f)
            f.write('\n')

    print('done')
    # at this point I have my file 
    #app.config['FILE'] = 'C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\data.json'
    #return send_file(app.config['FILE'], as_attachment = True)
    return send_file('C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\data.json', as_attachment = True)
    #return render_template('ret.html')

if __name__ == '__main__':
    app.run()
