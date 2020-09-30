<h1>reinforcement learning test</h1>

To test this code you are required to have conda installed (https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

after this open an anaconda prompt and create a environment with the dependencies from the yml file (conda env create --name tf2-env -f conda-dependencies.yml) (CUDA toolkit requires a nvidia GPU, without it you can still run this code but it will be done on the CPU)

when this is done type conda activate tf2-env to enter the environment, next run python test.py to start training the agent and when it is finished it will try to complete the challenge with a perfect score, this will be printed in the console.
