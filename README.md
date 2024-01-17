## Code Challenges

This is a collection of code challenges proposed by the following sites:

[beecrow](https://www.beecrowd.com.br/)
[HarckerRank](https://hackerrank.com/)
[Codewars](https://www.codewars.com/)

The goal of this repository is to collect and study the optimal ways to solve the 
proposed code challenges.

Each challenge have the following structure:
- A .md file, describing the challenge
- A `solution.py` file, with my solution and comments
- a `sample_test.py` file, with custom tests for the implemented solution

If you are interested in code-challenges, I suggest that you only look into the code
included on this repository after you have completed the challenge yourself.

### Environment

A Conda environment.yml file was provided to install any needed packages.

To install Anaconda, follow the instructions on the official [Conda website](https://conda.io/projects/conda/en/latest/user-guide/install/)

I suggest using minicoda to use the environment.

#### Using this repository

Installation Instructions
**1. Clone the Repository:**

```bash
git clone https://github.com/phbrgnomo/code-challenges
cd code-challenges
```

**2. Create and Activate Conda Environment:**


```bash
conda env create --file requirements.yml
conda activate code-challenges
```

**3. Run the Application:**

After entering the chosen challenge folder

To run the solution:
```bash
python solution.py
```

If you want to try to implement your own solution, just delete or rename the `solution.py` file, and then run the test script to check if your implementation is correct.

```bash
python sample_test.py
```


**Additional Notes:**
Make sure to activate your Conda environment before running any scripts or using the application.

If you encounter any issues, refer to the Conda documentation for troubleshooting and advanced usage.