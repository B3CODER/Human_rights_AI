import os
import re
from transformers import pipeline

def load_files(directory):
    summaries = {}
    cases = {}
    
    # Load summaries
    summary_files = [
        "Right_to_Unionize_and_Collective_Bargaining.txt",
        "Limitation_on_Working_Hours.txt",
        "Protection_from_Forced_Labor.txt",
        "Minimum_Wage.txt"
    ]
    
    for summary_file in summary_files:
        category = summary_file.replace('.txt', '')
        file_path = os.path.join(directory, summary_file)
        print(f"Loading summary from: {file_path}")
        try:
            with open(file_path, 'r') as file:
                summaries[category] = file.read()
        except FileNotFoundError:
            summaries[category] = "Summary not available."
        
        # Load cases
        case_dir = os.path.join(directory, category, "cases")
        case_files = []
        print(f"Loading cases from: {case_dir}")
        if os.path.exists(case_dir):
            for filename in os.listdir(case_dir):
                if filename.endswith(".txt"):
                    case_file_path = os.path.join(case_dir, filename)
                    with open(case_file_path, 'r') as case_file:
                        case_files.append((filename, case_file.read()))
            cases[category] = case_files
        else:
            cases[category] = []
    
    return summaries, cases

def preprocess_query(query):
    query = query.lower()  
    query = re.sub(r'[^\w\s]', '', query)  
    query = query.strip()  
    return query

def classify_query(query):
    keywords = {
        "Right_to_Unionize_and_Collective_Bargaining": ["union", "collective bargaining", "right to join", "trade union"],
        "Limitation_on_Working_Hours": ["working hours", "work time", "overtime", "work week", "hour limit"],
        "Protection_from_Forced_Labor": ["forced labor", "slavery", "bonded labor", "human trafficking"],
        "Minimum_Wage": ["minimum wage", "pay rate", "salary", "wage floor"]
    }
    
    for category, keyword_list in keywords.items():
        if any(keyword in query for keyword in keyword_list):
            return category
    return None

def translate_summary(summary, target_language):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
    translator = pipeline("translation_en_to_" + target_language, model=model_name)
    translation = translator(summary, max_length=512)[0]['translation_text']
    return translation

def main():
    summaries_directory = 'summaries'  # Directory containing the summary and case files
    summaries, cases = load_files(summaries_directory)
    
    query = input("Enter your query: ")
    processed_query = preprocess_query(query)
    print(f"Processed query: {processed_query}")  # Debugging print
    category = classify_query(processed_query)
    print(f"Classified category: {category}")  # Debugging print
    
    if category:
        summary = summaries.get(category, "Summary not available.")
        print(f"\nSummary for category '{category}':\n")
        print(summary)
        
        # Ask user if they want to see related cases
        show_cases = input("\nDo you want to see related case files? (yes/no): ").strip().lower()
        if show_cases == "yes":
            case_files = cases.get(category, [])
            if case_files:
                print(f"\nCase files for category '{category}':\n")
                for filename, content in case_files:
                    print(f"\n{filename}:\n{content}")
            else:
                print("No case files available for this category.")
        
        # Ask user if they want to translate the summary
        translate = input("\nDo you want to translate this summary? (yes/no): ").strip().lower()
        if translate == "yes":
            language_mapping = {
                "french": "fr",
                "german": "de",
                "spanish": "es",
                "hindi": "hi",
                "japanese": "ja"
            }
            print("Supported languages: French, German, Spanish, Hindi, Japanese")
            selected_language = input("Enter the language you want to translate to: ").strip().lower()
            target_language = language_mapping.get(selected_language)
            
            if target_language:
                translated_summary = translate_summary(summary, target_language)
                print(f"\nTranslated Summary in {selected_language.capitalize()}:\n")
                print(translated_summary)
            else:
                print("Sorry, the selected language is not supported.")
    else:
        print("Could not classify the query into a known category.")

if __name__ == "__main__":
    main()
