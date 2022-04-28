from flask import Flask, render_template
import utils

app = Flask(__name__)

data = utils.load_candidates_from_json("candidates.json")

@app.route("/")
def list_candidates():
    """Главная страница со списком кандидатов"""

    return render_template("list.html", candidates=data)

@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """Страница кандидата по id"""
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)

@app.route("/search/<string:candidate_name>")
def list_candidates_by_name(candidate_name):
    """Страница кандидатов по имени"""
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count=len(candidates))

@app.route("/skill/<string:skill_name>")
def list_candidates_by_skill(skill_name):
    """Страница кандидатов по навыку"""
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skills.html", candidates=candidates, count=len(candidates), s=skill_name)

app.run()