



workflows, ratings = open('sample').read().strip().split('\n\n')

# print(f"{workflows=}")
# print(f"{ratings=}")

# Define a function to extract a list of dictionaries from the ratings string
def extract_parts(ratings):
    parts = []
    for part_str in ratings.split('\n'):
        if part_str:
            part = {}
            for attribute_str in part_str.strip('{}').split(','):
                attribute, value = attribute_str.split('=')
                part[attribute] = int(value)
            parts.append(part)
    return parts

parts = extract_parts(ratings)
print(parts)

# Define a function to convert the string representation to a dictionary
def parse_workflows(workflow_str):
    workflows = {}
    for workflow_rule in workflow_str.split():
        workflow_name, rule_str = workflow_rule.split('{')
        rules = {}
        for rule in rule_str.strip('}').split(','):
            condition, next_workflow = rule.split(':')
            rules[condition] = next_workflow
        workflows[workflow_name] = rules
    return workflows

# Convert the string representation to a dictionary
workflows = parse_workflows(workflows)


def process_part(part, current_workflow):
    current_workflow

    if current_workflow == 'A':
        return sum(part.values())
    elif current_workflow == 'R':
        return 0
    else:
        for attribute, next_workflow in workflows[current_workflow].items():
            if attribute == 'condition':
                continue
            if attribute in part:
                if part[attribute] < int(next_workflow):
                    return process_part(part, next_workflow)
                else:
                    break
        return process_part(part, workflows[current_workflow]['condition'])



def sort_parts(parts):
    total_rating = 0
    for part in parts:
        if process_part(part, 'in'):
            total_rating += sum(part)
    return total_rating

print("part1:" , sort_parts(parts))
