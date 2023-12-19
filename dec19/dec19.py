import re

lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

empty = lines.index('')


class Rule:
    def __init__(self, cat, cmp, value, next) -> None:
        self.cat = cat
        self.cmp = cmp
        self.value = value
        self.next = next


def get_next(part: dict[str, int], wf_rules: list[Rule]):
    for rule in wf_rules:
        if rule.cat == None and rule.cmp == None and rule.value == None:
            return rule.next

        if rule.cmp == "<":
            if part[rule.cat] < rule.value:
                return rule.next
        elif part[rule.cat] > rule.value:
            return rule.next


workflows: dict[str, list[Rule]] = {}
parts: list[Rule] = []

for i in range(empty):
    match = re.findall(r'(.*){(.*)}', lines[i])[0]
    wf_name = match[0]

    workflows[wf_name] = []

    rules_strings = match[1].split(',')

    for j in range(len(rules_strings)):
        if j == len(rules_strings) - 1:
            workflows[wf_name].append(Rule(None, None, None, rules_strings[j]))
        else:
            match = re.findall(r'(x|m|a|s)(<|>)(.*):(.*)', rules_strings[j])[0]
            workflows[wf_name].append(
                Rule(match[0], match[1], int(match[2]), match[3]))

for i in range(empty+1, len(lines)):
    match = re.findall(r'{x=(.*),m=(.*),a=(.*),s=(.*)}', lines[i])[0]
    parts.append({"x": int(match[0]), "m": int(
        match[1]), "a": int(match[2]), "s": int((match[3]))})

accepted = []

for part in parts:

    current_wf = "in"
    flag = False

    while not flag:
        next = get_next(part, workflows[current_wf])

        if next == "A":
            accepted.append(part)
            flag = True
        elif next == "R":
            flag = True
        else:
            current_wf = next

ans = 0
for part in accepted:
    ans += sum(part.values())

print(ans)
