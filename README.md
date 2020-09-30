<h1>reinforcement learning test</h1>

This repository contains the source code / images which demonstrate me learning to understand the basics of tensorflow 2 syntax and how reinforcement learning works in a basic example. In this assignment i have created an agent which can be trained to beat Cartpole-V0 (https://gym.openai.com/envs/CartPole-v0/ (Links to an external site.)) with a perfect score when trained.


<h2> instructions for running locally </h2>
To test this code you are required to have conda installed (https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

after this open an anaconda prompt and create a environment with the dependencies from the yml file (conda env create --name tf2-env -f conda-dependencies.yml) (CUDA toolkit requires a nvidia GPU, without it you can still run this code but it will be done on the CPU)

when this is done type conda activate tf2-env to enter the environment, next run python test.py to start training the agent and when it is finished it will try to complete the challenge with a perfect score, this will be printed in the console.
