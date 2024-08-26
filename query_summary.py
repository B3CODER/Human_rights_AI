import csv
import re
from transformers import pipeline

def load_summaries(directory):
    summaries = {}
    categories = [
        "Right to Unionize and Collective Bargaining",
        "Limitation on Working Hours",
        "Protection from Forced Labor",     
        "Minimum Wage",
        # "Protection from Child Labor",
        # "Occupational Safety and Health",
        # "Protection from Human Trafficking"
    ]
    
    for category in categories:
        try:
            file_path = f"{directory}/{category.replace(' ', '_').replace('&', 'and')}.txt"
            with open(file_path, 'r') as file:
                summaries[category] = file.read()
        except FileNotFoundError:
            summaries[category] = "Summary not available."
    
    return summaries


def preprocess_query(query):
    query = query.lower()  
    query = re.sub(r'[^\w\s]', '', query)  
    query = query.strip()  
    return query

def classify_query(query):
    keywords = {
        "Right to Unionize and Collective Bargaining": ["union", "collective bargaining", "right to join", "trade union"],
        "Limitation on Working Hours": ["working hours", "work time", "overtime", "work week", "hour limit"],
        "Protection from Forced Labor": ["forced labor", "slavery", "bonded labor", "human trafficking"],
        "Minimum Wage": ["minimum wage", "pay rate", "salary", "wage floor"],
        # "Protection from Child Labor": ["child labor", "minimum age", "underage work", "child employment"],
        # "Occupational Safety and Health": ["safety", "health", "workplace hazards", "protective equipment"],
        # "Protection from Human Trafficking": ["human trafficking", "exploitation", "illegal trade", "trafficking victims"]
    }
    
    for category, keyword_list in keywords.items():
        if any(keyword in query for keyword in keyword_list):
            return category
    return None

# Function to translate text using Hugging Face transformers
def translate_summary(summary, target_language):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_language}"
    translator = pipeline("translation_en_to_" + target_language, model=model_name)
    translation = translator(summary, max_length=512)[0]['translation_text']
    return translation

# Main function
def main():
    summaries_directory = 'summaries'  # Directory containing the summary text files
    summaries = load_summaries(summaries_directory)
    
    query = input("Enter your query: ")
    processed_query = preprocess_query(query)
    category = classify_query(processed_query)
    
    if category:
        summary = summaries.get(category, "Summary not available.")
        print(f"\nSummary for category '{category}':\n")
        print(summary)
        

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
