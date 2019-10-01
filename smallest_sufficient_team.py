"""
https://leetcode.com/problems/smallest-sufficient-team/
[
    1 1 0 1 0 0
    1 0 0 1 0 0
    0 1 1 0 0 0
    0 1 0 0 1 0
    0 0 1 0 1 1
    0 0 0 1 1 1
]
"""

def skill_sum(person, skill_map):
    return sum([skill_map[skill] for skill in person])


def find_team(skills, people):
    # TODO
    return []


def smallestSufficientTeam(req_skills, people):
    if not req_skills:
        return []

    skill_map = {}
    skills_sum = (1 << len(req_skills)) - 1
    for index, skill in enumerate(req_skills):
        skill_map[skill] = 1 << index

    people = [skill_sum(person, skill_map) for person in people]
    team = find_team(skills_sum, people)

    return team


if __name__ == '__main__':
    cases = [
        [(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]), [0,2]],
        [(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]), [1,2]],
    ]

    for case in cases:
        result = set(smallestSufficientTeam(*case[0]))
        expected = set(case[1])
        print("PASS" if result == expected else "FAIL")
