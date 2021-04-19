from flask import Flask
import json

from sources.get_company import SearchCompany
from sources.search_tag import SearchCompanyWithTag, TagManipulation

if __name__ == "__main__":
    with open("api_info.json") as f:
        api_info = json.load(f)

    app = Flask(__name__)
    app.debug = False

    app.add_url_rule("/search/company/name/<company>", view_func=SearchCompany.as_view("searchCompony"))
    app.add_url_rule("/search/company/tag/<tag>", view_func=SearchCompanyWithTag.as_view("searchCompanyWithTag"))
    app.add_url_rule("/tag", view_func=TagManipulation.as_view("tagManipulationPost"), methods=['POST',])
    app.add_url_rule("/tag/<company>/<tag>", view_func=TagManipulation.as_view("tagManipulationDelete"), methods=['DELETE'])

    app.run(
        host = api_info.get("host", 'localhost'),
        port = api_info.get("port", "5000"),
        threaded = True,
        debug= False
    )