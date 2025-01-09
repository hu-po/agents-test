goal = ""
memory = []
env = Environment()
while True:
    observation = sense(env)
    action = plan(goal, observation, memory)
    outcome = act(env, action)
    memory.append(observation, outcome)
    goal = update_goal(goal, outcome)