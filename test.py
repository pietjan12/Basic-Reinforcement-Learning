import gym
import model
import agent

env = gym.make('CartPole-v0')
model = model.Model(num_actions=env.action_space.n)

obs = env.reset()

#fetch agent class
agent = agent.Agent(model)

#train agent
rewards_history = agent.train(env)
print("Finished training, testing...")
#test fully trained agent
print("%d out of 200" % agent.test(env)) # score out of 200