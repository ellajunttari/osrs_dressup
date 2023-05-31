"""from osrsbox import items_api

all_db_items = items_api.load()

for i in range(10):
    print(all_db_items[i].wiki_url)

val = input("Name an item: ")
for x in all_db_items:
    if x.name == val:
        print(f"Item link: {x.wiki_url}")
#print(all_db_items[])
#print(all_db_items[0])
"""

from flask import Flask, request, Response, render_template


app = Flask(__name__)


@app.route("/")
def index():
    html = render_template( "jinja.html")
    return html

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)