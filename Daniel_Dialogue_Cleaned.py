import re

# Function to clean up text
def clean_text(text):
    # Remove unnecessary metadata (e.g., copyright notices, special characters)
    text = re.sub(r"(?i)copyright.*?\d{4}", "", text)  # Remove copyright mentions
    text = re.sub(r"\s+", " ", text).strip()  # Normalize whitespace
    text = re.sub(r"[^a-zA-Z0-9.,!?;:'\"()\\-]", " ", text)  # Remove unwanted symbols
    return text

# Function to generate additional synthetic questions for data augmentation
def augment_with_synthetic_questions(dialogue_list):
    synthetic_prompts = [
        "What does this mean?", "Can you explain in more detail?", "Why is this important?", 
        "How does this relate to the Three Laws?", "What is your perspective on this?", 
        "What does this tell us about robots?"
    ]
    augmented_dialogue = []
    
    for pair in dialogue_list:
        input_text = clean_text(pair["input"])
        output_text = clean_text(pair["output"])
        
        # Ensure the cleaned data is valid
        if input_text and output_text:
            augmented_dialogue.append({"input": input_text, "output": output_text})
            
            # 25% chance to add a synthetic question
            if random.random() < 0.25:
                synthetic_question = random.choice(synthetic_prompts)
                augmented_dialogue.append({"input": synthetic_question, "output": output_text})
    
    return augmented_dialogue

# Step 1: Clean and Validate Dataset
cleaned_dataset = []
for entry in data:
    cleaned_entry = {
        "context": clean_text(entry["context"]),
        "dialogue": augment_with_synthetic_questions(entry["dialogue"])
    }
    cleaned_dataset.append(cleaned_entry)

# Step 2: Save cleaned and augmented dataset
cleaned_json_output_path = "/mnt/data/daneel_dialogue_cleaned.json"
with open(cleaned_json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(cleaned_dataset, json_file, indent=4)

# Provide download link
cleaned_json_output_path
