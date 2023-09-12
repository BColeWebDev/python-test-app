from flask import Flask, request, Response
import json
from utils import Sortation, Filtering, Pagination
app = Flask(__name__)


@app.route('/all')
def testing():
    page = request.args.get("page")
    pageDisplay = request.args.get("pageDisplay")
    sort = request.args.get("sort")
    filters = request.args.get("filters")
    print(page)
    print(sort)
    print(pageDisplay)
    print(filters)

    f = open("workouts.json", "r")
    workouts = json.load(f)
    if page == None or pageDisplay == None:
        return {"err": "Page Number or Page Limit Missing"}, 400

    if sort != None:
        workouts = Sortation(sort, workouts)
    if (filters != None):
        workouts = Filtering(filters, workouts)
    if (page != None or pageDisplay != None):
        workouts = Pagination(int(page), int(pageDisplay), workouts)

    results = {
        "items": workouts,
        "page": int(page),
        "pageDisplay": int(pageDisplay),
    }
    return results
