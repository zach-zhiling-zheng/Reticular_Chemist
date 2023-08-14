# GPT-4 Reticular Chemist

<img src="./docs/images/logo.png" width="15%" height="15%">

## Requirements and Usage

The script runs on the Python stack and requires the following packages: 

    pandas
    re

The script helps to generate the input prompt that is then given to GPT-4 via the interface on https://chat.openai.com. 

## Data

The data used in the interactive prompting strategy at each step of the process is given in the [Excel Sheet](./data/prompt-input-and-GPT-4-output.xlsx) present in  the [data](./data/) folder. The Excel Sheet has the following headers:


| MOF |	Summary |	Iteration |	Status Evaluation |	Choice 1 |	Choice 2 |	Choice 3 |	Choice Selected |	Human Feedback |	Next Prompt |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |


Add more details about what the different columns mean, etc. (which columns correspond to the output from GPT and which ones correspond to the input provided to GPT)

## Citation

More details about the GPT-4 Reticular Chemist are given in the following preprint:

> *GPT-4 Reticular Chemist for MOF Discovery* <br/>
> Zhiling Zheng, Zichao Rong, Nakul Rampal, Christian Borgs, Jennifer T. Chayes, Omar M. Yaghi <br/>
> https://arxiv.org/abs/2306.14915 <br/>

## References

For GPT-4: 

> GPT-4 Technical Report <br/>
> OpenAI <br/>
> https://arxiv.org/abs/2303.08774 <br/>

For Pandas:

> pandas-dev/pandas: Pandas (version: latest) <br/>
> The pandas development team <br/>
> https://doi.org/10.5281/zenodo.3509134 <br/>
