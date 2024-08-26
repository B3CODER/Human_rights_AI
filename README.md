# Human Rights Query Classification and Summary Translation System

## Introduction

Human rights are fundamental entitlements that belong to every individual by virtue of their humanity. These rights include the right to life, freedom, and equality, and are crucial for ensuring dignity, justice, and equality across all societies. This project harnesses artificial intelligence (AI) to make human rights information more accessible and actionable by classifying queries, retrieving relevant summaries, and providing translations.

AI technologies have the potential to transform the way we understand and advocate for human rights. By using advanced natural language processing (NLP) models, this project aims to:

- **Enhance Access**: Provide users with easy access to information about various human rights issues.
- **Improve Awareness**: Raise awareness about specific human rights topics by offering detailed summaries and related cases.
- **Support Advocacy**: Empower activists and organizations by providing tools to efficiently retrieve and translate human rights information.

## Human Rights Categories

Our system addresses several critical human rights categories:

### Physical Integrity Rights
- **Protection from Disappearances**: Safeguarding individuals from being unlawfully abducted or disappearing.
- **Protection from Extrajudicial Killings**: Preventing killings carried out without legal process.
- **Protection from Political Imprisonment**: Shielding individuals from imprisonment for political reasons.
- **Protection from Torture**: Ensuring freedom from cruel, inhuman, or degrading treatment.
- **Protection from Mass Atrocity**: Guarding against large-scale violence or abuses.

### Empowerment Rights
- **Rights of Assembly and Association**: Guaranteeing the freedom to gather and form groups.
- **Freedom of Foreign Movement**: Allowing unrestricted travel across borders.
- **Freedom of Domestic Movement**: Ensuring the ability to move freely within one's own country.
- **Free Speech and Press**: Upholding the right to express ideas and information freely.
- **Electoral Self-Determination**: Ensuring the right to participate in democratic elections.
- **Religious Freedom**: Protecting the right to practice any religion or none at all.
- **Women’s Economic Rights**: Guaranteeing equal economic opportunities for women.
- **Women’s Political Rights**: Ensuring women’s participation in political processes.
- **Women’s Social Rights**: Safeguarding women’s rights in law and practice.

### Worker Rights
- **Right to Unionize**: Protecting the right to form and join unions.
- **Collective Bargaining**: Supporting negotiations between workers and employers.
- **Limitation on Working Hours**: Regulating the length of work hours.
- **Protection from Forced Labour**: Prohibiting involuntary work under threat or coercion.
- **Protection from Child Labour**: Preventing the exploitation of children in the workforce.
- **Minimum Wage**: Ensuring fair compensation for work performed.
- **Occupational Safety and Health**: Safeguarding workers' health and safety.
- **Protection from Human Trafficking**: Preventing trafficking and exploitation of individuals.

### Justice Rights
- **Independent Judiciary**: Ensuring the judiciary operates free from external influence.
- **Fair Trial**: Guaranteeing a just legal process for all individuals.
- **Human Rights NGO Freedom**: Supporting the ability of NGOs to operate freely and advocate for human rights.

### Human Rights Indices
- **Overall Human Rights Score**: An aggregate measure of human rights conditions.
- **Physical Integrity Rights**: Index assessing protection against violations of physical integrity.
- **Repression Index**: Measurement of government repression and control.
- **Civil and Political Rights**: Index evaluating the state of civil liberties and political freedoms.
- **Worker Rights**: Index assessing the respect and implementation of worker rights.

## Project Overview

The dataset used for this project is `Human_Rights_AI.csv`, which includes queries and corresponding categories related to human rights. Our initial focus is on worker rights, with the following aspects being considered:

1. **Right to Unionize**
2. **Collective Bargaining**
3. **Limitation on Working Hours**
4. **Protection from Forced Labour**

### Objectives

- **Query Classification**: Utilize a BERT-based model to classify human rights queries into relevant categories.
- **Summary Retrieval**: Extract and display summaries related to classified categories.
- **Case Retrieval**: Provide access to detailed cases related to the human rights categories.
- **Translation**: Translate summaries into various languages using Hugging Face's translation model.

## Work Done

1. **Data Preparation**: Processed and formatted the dataset `Human_Rights_AI.csv` to include queries and categories related to human rights.
2. **Model Training**: Fine-tuned a BERT-based model on the dataset to classify queries into specific human rights categories.
3. **Summary Retrieval**: Developed functionality to extract and display summaries related to classified categories.
4. **Case Retrieval**: Implemented a feature to retrieve and print relevant case studies related to each category, allowing users to delve deeper into specific issues.
5. **Translation**: Integrated Hugging Face's translation model to offer multilingual support, enabling users to access summaries in various languages.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the Data**:
    - Ensure `Human_Rights_AI.csv` and `summaries.zip` are in the project directory.
    - Extract `summaries.zip` into a directory named `summaries`.

## Usage

### Training the Model

To train the model, run:
```bash
python main.py --train
