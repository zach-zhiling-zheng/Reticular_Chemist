# GPT-4 Reticular Chemist

<img src="./docs/images/logo-v2.png" width="17%" height="17%">

Credits: This image was generated with the assistance of AI

## Requirements and Usage

The script runs on the Python stack and requires the following packages: 

    pandas
    re

The script helps to generate the input prompt that is then given to GPT-4 via the interface on https://chat.openai.com. 

The script contains three main functions:

1. **```extract_info(pattern, text)```**: This function uses regex patterns (_```variable: pattern```_) to extract specific parts of information from an output generated by GPT-4 (_```variable: text```_).

2. **```append_information(df, output_text, choice, human_feedback)```**: This function is used to append new information into a Pandas DataFrame (_```variable: df```_) based on the user's chosen task (_```variable: choice```_) and their feedback (_```variable: human_feedback```_). It also constructs the next AI prompt for the user. 

3. **```generate_long_term_memory(df)```**: This function generates a long-term memory prompt string that includes stage-wise summaries.

## Data

The data used in the interactive prompting strategy at each step of the process is given in the [Excel Sheet](./data/prompt-input-and-GPT-4-output.xlsx) present in  the [data](./data/) folder. The Excel Sheet has the following headers:


| MOF |	Summary |	Iteration |	Status Evaluation |	Choice 1 |	Choice 2 |	Choice 3 |	Choice Selected |	Human Feedback |	Next Prompt |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |


The first 7 columns of the datasheet correspond to the *output* from GPT-4, while the next 3 columns correspond to the *input* provided to GPT-4. 

## License 

The input prompt generation script is distributed under the MIT open source license (see [`LICENSE.txt`](LICENSE.txt))


## Citation

More details about the GPT-4 Reticular Chemist are given in the following preprint:

> *GPT-4 Reticular Chemist for MOF Discovery* <br/>
> Zhiling Zheng[^1], Zichao Rong[^1], Nakul Rampal, Christian Borgs, Jennifer T. Chayes, Omar M. Yaghi[^2] <br/>
> https://arxiv.org/abs/2306.14915 <br/>

[^1]: Contributed equally
[^2]: Corresponding author (email: yaghi@berkeley.edu)


## Contributing

If you have any questions/comments/feedback, please feel free to reach out to any of the authors.

In addition, if you have any new feature requests or if you find any bugs, please open a new [issue](https://github.com/zach-zhiling-zheng/Reticular_Chemist/issues).

## Acknowledgements

We acknowledge the financial support from the following sources:
1. Defense Advanced Research Projects Agency (DARPA) under contract HR0011-21-C-0020 
2. Bakar Institute of Digital Materials for the Planet (BIDMaP)
3. NIH (Grant S10-RR027172)
4. Kavli ENSI Graduate Student Fellowship

## References

For GPT-4: 

> GPT-4 Technical Report <br/>
> OpenAI <br/>
> https://arxiv.org/abs/2303.08774 <br/>

For Pandas:

> pandas-dev/pandas: Pandas (version: latest) <br/>
> The pandas development team <br/>
> https://doi.org/10.5281/zenodo.3509134 <br/>


