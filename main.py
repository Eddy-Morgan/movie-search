#######################################################################################################################
# Project first started on 29/05/2018 at 21:28                                                                        #
# Written by Black with love #DIY                                                                                     #
# Movies Search Engine #Series #Films                                                                                 #
# Locally made                                                                                                        #
#                                                                                                                     #
#######################################################################################################################


from flask import Flask,render_template, request
from g_engine import search,scrape
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    results = {}
    
    return render_template('index.html', results=results)

@app.route('/search',methods=['GET'])
def generate_links():
    query = request.args.get('query')
    web_search = search(query)
    results = scrape(web_search)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True,port='5000')