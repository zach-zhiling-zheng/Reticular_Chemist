import pandas as pd
import re

def extract_info(pattern, text):
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        print(f"Failed to find information matching pattern: {pattern}")
        return None

def append_information(df, output_text, choice, human_feedback):
    # Extract information from the text using regex
    summary = extract_info('Output Summary:(.*?)(Current Stage and Iteration:|$)', output_text)
    iteration = extract_info('Current Stage and Iteration:(.*?)(Status Evaluation:|$)', output_text)
    status_evaluation = extract_info('Status Evaluation:(.*?)(Task Choice 1:|$)', output_text)
    task_choice_1 = extract_info('Task Choice 1:(.*?)(Task Choice 2:|$)', output_text)
    task_choice_2 = extract_info('Task Choice 2:(.*?)(Task Choice 3:|$)', output_text)
    task_choice_3 = extract_info('Task Choice 3:(.*?)(Task Choice [4-9]:|$)', output_text)
    
    # If any information could not be extracted, stop the function
    if any(info is None for info in [summary, iteration, status_evaluation, task_choice_1, task_choice_2, task_choice_3]):
        return df

    # Construct the next prompt based on the provided template and extracted information
    last_task = ''
    if choice == 1:
        last_task = task_choice_1
    elif choice == 2:
        last_task = task_choice_2
    elif choice == 3:
        last_task = task_choice_3
    else:
        print('Invalid choice value.')
        return df

    next_prompt = f"""
You are an AI reticular chemist assisting a human apprentice in a research project to develop a novel aluminum MOF using 4,4’,4’’-(2,4,6-trimethylbenzene-1,3,5-triyl)tribenzoic acid (BTB-CH3) as the linker.
The BTB-CH3 is a BTB linker derivative featuring a central phenyl ring linked to three additional phenyl rings and central ring is substituted with three methyl groups, while each of the flanking rings bears one carboxylic acid groups. The project is structured into five stages:

1) Synthesis of Organic Linker.
2) High-throughput screening of the MOF and optimization of the synthetic outcomes via PXRD.
3) Activation and Determination of Permanent Porosity.
4) Detailed Structural Analysis and Characterization of the MOF for single crystal structure, chemical composition, phase purity, and chemical and thermal stability.
5) Reproducibility Check and Final Validation


Below is an example of work summary of another project using another BTB linker derivative (BTB-oF), and it is suggested that you make similar attempts:

...
Similar Work Summary: Our research project aimed at synthesizing a novel Aluminum Metal Organic Framework (MOF), termed MOF-521-oF, using the 4-[3,5-Bis(4-carboxy-3-fluorophenyl)phenyl]-2-fluorobenzoic acid (BTB-oF) linker, and has seen significant progress over the course of five defined stages.

In the first stage, we concentrated on the synthesis of the BTB-oF linker. The apprentice demonstrated meticulous attention to detail in adhering to the prescribed procedure from the literature, which involves a palladium-catalyzed Suzuki–Miyaura cross-coupling reaction to form an ester derivative, followed by saponification and acidification. resulting in a successful synthesis. Validation of the linker was performed using 1H NMR spectroscopy, which yielded chemical shifts. By comparing these experimental shifts with the predicted ones using ChemDraw's NMR prediction tool, a high degree of correlation was identified, including the correct number of hydrogens determined post-integration. These findings confirmed the successful synthesis of the BTB-oF linker.

In the second stage, we shifted focus to the high-throughput screening of the MOF and optimization of synthetic conditions. Initial trials didn't yield the anticipated MOF structure, necessitating adjustments of BTB:Al and formic acid to water ratios. The optimal synthetic conditions emerged as a BTB:Al ratio of 3:4, a formic acid to water ratio of 4:1, and a reaction temperature of 120°C. However, a trade-off was observed between temperature and crystallinity as products at higher temperatures (130°C and 140°C) resulted in a mixture of single crystals and powders. Furthermore, a reaction time at 120°C between 72 and 96 hours produced the highest quality and quantity of crystals, as indicated by similar intensity and PXRD peaks.

In the third stage, the MOF was activated through methanol solvent exchange and vacuum drying. Nitrogen gas sorption analysis conducted at 77 K confirmed the microporosity of the MOF with a specific surface area of 1562 m² g-1, total pore volume of 0.564 cm^3/g, and an average pore width of 10.7 Å. Minimal hysteresis seen in the hysteresis analysis emphasized the stability and verified the microporous nature of our MOF.

The fourth stage involved detailed characterization of our MOF. A CHNS elemental analysis confirmed the chemical composition of our MOF, while a thermogravimetric analysis (TGA) showcased good thermal stability up to 300°C. Chemical stability tests displayed stability in DMF, methanol, and ethanol, however, the MOF displayed potential instability in water. Further 1H NMR spectroscopy after water exposure revealed a formate peak at ~8.3 ppm, implying hydrolysis. A single-crystal X-ray diffraction (SCXRD) analysis verified our MOF as a novel framework with unique structural features, including the positions of formate groups and water molecules. Moreover, pH stability tests showed significant losses in peak intensity for our MOF after exposure to water at varying pH levels, reinforcing the potential water instability issues.

Finally, in the fifth stage, we aimed at verifying the reproducibility of our process. The entire procedure was replicated, and the consistency of the results with earlier reported data confirmed the reproducibility of our protocols.

...


In each interaction, you'll be provided with the similar work current project summary, the most recent task suggestion, and the feedback from the human apprentice.  With these inputs, you should generate the following:

Output Summary: Construct an updated summary that primarily draw from the previous output summary, adding only one or two sentences regarding the latest task and its outcomes based on human feedback, and another one sentence discussing the status of the current stage. 
The summary should tells the story of the project so far, summarizing both successes and failures from all completed stages and tasks. 
Keep in mind that it is important to maintain the vital details from each stage. The summary part should not exceed 100 sentences. If it does, you should condense earlier information.

Current Stage and Iteration: Indicate this with a numerical pair (e.g., 2-6), where the first number refers to the current stage and the second to the iteration within this stage. You should only advance to the next stage when the apprentice explicitly states, "I'm ready to move to the next stage." Upon this declaration, you can immediately update the stage and iteration pair in your output to reflect progress (e.g., from 3-6 to 4-1). Othewiese, you will add one to the iteration number (e.g. from 3-6 to 3-7).

Output Status Evaluation: Explain the reason behind the results reported by the human apprentice based on your most recent task suggestion. This should be a short (one or two sentence) analysis. Consider following the successful attempts described in the similar work summary example when encountering parallel challenges in comparable situations, as the method may be generalizable. Using this reasoning, explain how you come up with the three task choices for the step for the current stage. 

Output Task Choices: Offer three task options that the apprentice can choose from for the next step, each consisting of 10 to 20 sentences and should be presented in a detailed, step-by-step manner to instruct the human what to do next. The first sentence should give a summary of the step, followed by the procedural details. If the apprentice's feedback implies the completion of a stage, one of your choices can be encouraging the apprentice to state, "I'm ready to move to the next stage." Always remember to only suggest tasks relevant to the current stage and avoid proposing tasks related to upcoming stages. The provided Similar Work Summary example should be read and understood in terms of both successes and failures from a project utilizing different linkers. If the situation is similar, you can consider give task choice in light of the similar work summary.
Here are the inputs:
...
Current Summary: {summary}
Last Iteration: {iteration}
Latest Task: {last_task}
Human Feedback: {human_feedback}
...
    
I need you to only respond in the format as described below :
...
Output Summary:  <updated summary>
Current Stage and Iteration: <X-X>
Status Evaluation : <reasoning>
Task Choice 1: <next task choice 1>
Task Choice 2: <alternative next task choice>
Task Choice 3: <alternative next task choice>
...

    """
    # Append the new row to the DataFrame
    new_row = pd.DataFrame({
        "Summary": [summary], 
        "Iteration": [iteration], 
        "Status Evaluation": [status_evaluation], 
        "Choice 1": [task_choice_1], 
        "Choice 2": [task_choice_2], 
        "Choice 3": [task_choice_3], 
        "Choice Selected": [choice],
        "Human Feedback": [human_feedback],
        "Next Prompt": [next_prompt],
    })
    
    print(next_prompt)
    
    # Check if iteration already exists in the dataframe
    if iteration in df['Iteration'].values:
        # If exists, drop that row
        df = df[df['Iteration'] != iteration]
        print("-------------------------------------------------------")
        print(f"Information regarding iteration {iteration} is updated")

    # Append the new row to the DataFrame
    new_row = pd.DataFrame({
        "Summary": [summary], 
        "Iteration": [iteration], 
        "Status Evaluation": [status_evaluation], 
        "Choice 1": [task_choice_1], 
        "Choice 2": [task_choice_2], 
        "Choice 3": [task_choice_3], 
        "Choice Selected": [choice],
        "Human Feedback": [human_feedback],
        "Next Prompt": [next_prompt],
    })

    df = pd.concat([df, new_row], ignore_index=True)
    
    return df



def generate_long_term_memory(df):
    # Create a copy to avoid modifying the original DataFrame
    df_copy = df.copy()

    # Ensure 'Iteration' is of type str
    df_copy['Iteration'] = df_copy['Iteration'].astype(str)

    # Convert 'Iteration' column into two separate columns for 'Stage' and 'Iteration'
    df_copy[['Stage', 'Iteration']] = df_copy['Iteration'].str.split('-', expand=True)

    # Convert 'Stage' and 'Iteration' to int for proper sorting and comparison
    df_copy['Stage'] = df_copy['Stage'].astype(int)
    df_copy['Iteration'] = df_copy['Iteration'].astype(int)

    # Sort values by 'Stage' and 'Iteration' in ascending order
    df_copy = df_copy.sort_values(['Stage', 'Iteration'])

    # Group by 'Stage' and get the last 'Summary' of each group
    result_df = df_copy.groupby('Stage').last().reset_index()

    # Create output string
    memory = '\n'.join(f'Stage {row.Stage}-{row.Iteration}: {row.Summary}' for row in result_df.itertuples())
    
    
    prompt = """
You are an AI reticular chemist assisting a human apprentice in a research project to develop a novel aluminum MOF 
using BTB-CH3 as a linker. The project is structured into five stages:

1) Synthesis of Organic Linker.
2) High-throughput screening of the MOF and optimization of the synthetic outcomes via PXRD.
3) Activation and Determination of Permanent Porosity.
4) Detailed Structural Analysis and Characterization of the MOF for chemical composition, phase purity, and chemical and thermal stability.
5) Reproducibility Check and Final Validation

You have already collaborated with the human apprentice to complete a few stages, and at the end of each stage, you have written down a summary. Below, I will provide you with these summaries, and your job is to consolidate them into a comprehensive summary. This final summary should be as explicit as possible, detailing every success and failure at all stages. There is no word limit for the final summary. It will be used to instruct and inform another AI reticular chemist, who will guide another human apprentice to carry out a similar research project.

Input:
...



{}

...

Output:
""".format(memory)
    print(prompt)
    return prompt


