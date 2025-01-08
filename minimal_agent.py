goal = ""
memory = []
while True:
    observation = sense()
    action = plan(goal, observation, memory)
    outcome = act(action)
    memory.append(observation, outcome)
    goal = update_goal(goal, outcome)