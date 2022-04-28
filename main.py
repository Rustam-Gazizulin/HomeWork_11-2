class Candidates:

    def __init__(self, list_candidates, candidate_id, candidate_name, candidate_skill):
        self.list_candidates = list_candidates
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.candidate_skill = candidate_skill

    def __repr__(self):
        return f'{self.list_candidates}\n{self.candidate_id}\n{self.candidate_name}\n{self.candidate_skill}'

    def load_candidates_from_json(self):
        '''возвращает список всех кандидатов'''
        with open("data/candidates.json", "r", encoding="utf-8") as file:
            

        pass

    def get_candidate(self):
        pass

    def get_candidates_by_name(self):
        pass

    def get_candidates_by_skill(self):
        pass