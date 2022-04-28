import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""

    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return {'name': 'Ушел на обед и не вернулся:))'}  # уведомление на случай неверного id


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json("candidates.json")
    list_candidate_by_name = []

    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            list_candidate_by_name.append(candidate)

    return list_candidate_by_name




def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""

    candidates = load_candidates_from_json("candidates.json")
    list_candidate_by_skill = []

    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            list_candidate_by_skill.append(candidate)

    return list_candidate_by_skill






