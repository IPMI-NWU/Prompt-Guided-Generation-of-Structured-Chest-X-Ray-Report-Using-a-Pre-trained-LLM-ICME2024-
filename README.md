# Prompt-Guided Generation of Structured Chest X-Ray Report Using a Pre-trained LLM (ICME2024)

## arXiv
https://arxiv.org/pdf/2404.11209

## Abstract

Medical report generation automates radiology de-seriptions from images,easing the burden on physicians andminimizing errors, However, current methods lack structuredoutputs and physician interactivity for clear, clinically relevantreports, Our method introduces a prompt-guided approach togenerate structured chest X-ray reports using a pre-trained largelanguage model CLM, First, we identify anatomical regionsin chest X-rays to generate focused sentences that center onkey visual elements, thereby establishing a structured reportfoundation with anatomy-based sentences, We also convert thedetected anatomy into textual prompts conveying anatomicalcomprehension to the LM, Additionally,the clinical contextprompts guide the LM to emphasize interactivity and clinicalrequirements. By integrating anatomy-focused sentences andanatomy/clinical prompts, the pre-trained LLM can generatestructured chest Xray reports tailored to prompted anatomicalregions and clinical contexts. We evaluate using language gen-eration and clinical effectiveness metrics, demonstrating strongperformance.

## Method

![image info](./figures/1.png) *Figure 1. In the architecture overview,the proes includes identifying and extracing amatomical reion features, generating reion descriptions, and ultimatelyintegrating anatomical prompts with clinical context prompts to produce a structured report.*

## Quantitative Results

![image info](./figures/2.png) *Table 1. COMPARISON RESULTS ON MIMIC-CXR SHOW THAT THE NUMBERS IN BOLD REPRESENT THE BEST RESULTS PER COLUMN.*

![image info](./figures/3.png) *Table 2. SIX PROMINENT REGIONS ARE IDENTIFIED AS FOLLOWS: RIGHT LUNG(RL), LEFT LUNG (LL), SPINE (SP), MEDIASTINUM (MED), CARDIACSILHOUETTE(CS),AND ABDOMEN (AB).*

![image info](./figures/4.png) *Table 3. RESULTS FROM SENTENCE DETECTION AND ABNORMALITY DETECTION.*

## Qualitative Results

<p align="center">
  <img src="figures/5.png" alt="Full report generation">
</p>
<p align="left">Figure 4. We represented the detected anatomical regions, the corresponding generated sentenes, and the semantically matched reference sentences using the same color, while also highlighting the clinical context.</p>

## Setup

1. Create conda environment, install dependencies. See [requirements.txt](requirements.txt) for the list of dependencies.
2. Install Java 1.8.0 (required for pycocoevalcap library, see https://pypi.org/project/pycocoevalcap/). On Ubuntu, you can install Java 1.8.0 with "**sudo apt install openjdk-8-jdk**".
3. In [path_datasets_and_weights.py](src/path_datasets_and_weights.py), specify the paths to the various datasets (Chest ImaGenome, MIMIC-CXR, MIMIC-CXR-JPG), CheXbert weights, and folders in which the runs are saved. Follow the instructions of the doc string of path_datasets_and_weights.py.

## Create train, val and test csv files

After the setup, run "**python [create_dataset.py](src/dataset/create_dataset.py)**" to create train, val and test csv files, in which each row contains specific information about a single image. See doc string of create_dataset.py for more details.

As a side note - we cannot provide you these files directly (i.e. you have to create these csv files yourself), since they contain patient information from Chest ImaGenome/MIMIC-CXR, to which only credentialed users with training in handling human participant data should have access (for privacy reasons).

## Inference

To generate reports for a list of images, run "**python [generate_reports_for_images.py](src/full_model/generate_reports_for_images.py)**". Specify the model checkpoint, the list of image paths and the path to the txt file with the generated reports in the main function.

## Citation

```
@article{Li2024PromptGuidedGO,
  title={Prompt-Guided Generation of Structured Chest X-Ray Report Using a Pre-trained LLM},
  author={Hongzhao Li and Hongyu Wang and Xia Sun and Hua He and Jun Feng},
  journal={2024 IEEE International Conference on Multimedia and Expo (ICME)},
  year={2024}
}
```