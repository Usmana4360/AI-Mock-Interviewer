import json
import pandas as pd
import nltk
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge



results_path = "/home/murtaza/PycharmProjects/tools_interview_project/results/"
# Load JSON file 1
with open(results_path+"conversation_history1.json", "r") as file1:
    data1 = json.load(file1)

# Load JSON file 2
with open(results_path+"conversation_history2.json", "r") as file2:
    data2 = json.load(file2)

def filter_json(data):
    keys_to_keep = ["Resume Summary", "Resume Feedback", "AI - Question","Feedback"]
    filtered_data = []
    for entry in data:
        filtered_entry = {}
        for key, value in entry.items():
            if key in keys_to_keep:
                filtered_entry[key] = value
                filtered_data.append(filtered_entry)

    return filtered_data


filtered_data1 = filter_json(data1)
filtered_data2 = filter_json(data2)

# print(filtered_data1)

def compute_bleu(reference, hypothesis):
    reference_tokens = [reference.split()]  # Reference needs to be a list of tokens
    hypothesis_tokens = hypothesis.split()
    score = sentence_bleu(reference_tokens, hypothesis_tokens)
    return score

bleu_scores = []
for entry1, entry2 in zip(filtered_data1, filtered_data2):
    for key in entry1.keys():
        score = compute_bleu(entry1[key], entry2[key])
        bleu_scores.append({key: score})

rouge = Rouge()

def compute_rouge(reference, hypothesis):
    return rouge.get_scores(hypothesis, reference, avg=True)
def compute_self_bleu(data):
    """
    Compute Self-BLEU for a list of strings to measure diversity.
    """
    diversity_scores = []
    for i, entry1 in enumerate(data):
        for j, entry2 in enumerate(data):
            if i != j:
                score = compute_bleu(entry1, entry2)
                diversity_scores.append(score)
    return sum(diversity_scores) / len(diversity_scores) if diversity_scores else 0


rouge_scores = []
for entry1, entry2 in zip(filtered_data1, filtered_data2):
    for key in entry1.keys():
        scores = compute_rouge(entry1[key], entry2[key])
        rouge_scores.append({key: scores})




ai_questions1 = [entry["AI - Question"] for entry in filtered_data1 if "AI - Question" in entry]
feedbacks1 = [entry["Feedback"] for entry in filtered_data1 if "Feedback" in entry]

ai_questions2 = [entry["AI - Question"] for entry in filtered_data2 if "AI - Question" in entry]
feedbacks2 = [entry["Feedback"] for entry in filtered_data2 if "Feedback" in entry]



questions_self_bleu_scores1 = compute_self_bleu(ai_questions1)
questions_self_bleu_scores2 = compute_self_bleu(ai_questions2)

feedback_self_bleu_scores1 = compute_self_bleu(feedbacks1)
feedback_self_bleu_scores2 = compute_self_bleu(feedbacks2)

# print("Blue Score: ",bleu_scores)
# print("Rouge score: ",rouge_scores)
# print("Questions Self Bleu: ",questions_self_bleu_scores1)
# print("Questions Self Bleu: ",questions_self_bleu_scores2)
# print("Feedback Self Bleu: ",feedback_self_bleu_scores1)
# print("Feedback Self Bleu: ",feedback_self_bleu_scores1)


# Flatten the BLEU and ROUGE results into a DataFrame for readability
bleu_data = []
for entry in bleu_scores:
    for key, value in entry.items():
        bleu_data.append({"Metric": key, "Score": value})

rouge_data = []
for entry in rouge_scores:
    for key, values in entry.items():
        for rouge_type, metrics in values.items():
            rouge_data.append({"Metric": f"{key} - {rouge_type}",
                               "Recall": metrics['r'],
                               "Precision": metrics['p'],
                               "F-Score": metrics['f']})

# Create DataFrame for BLEU and ROUGE scores
bleu_df = pd.DataFrame(bleu_data)
rouge_df = pd.DataFrame(rouge_data)

# Display BLEU and ROUGE data in tabular form
print("BLEU Scores:")
print(bleu_df)

print("\nROUGE Scores:")
print(rouge_df)

# Display Self-BLEU scores directly
print("\nQuestions Self BLEU Scores:")
print("Questions-1 Self Bleu: ", questions_self_bleu_scores1)
print("Questions-2 Self Bleu: ", questions_self_bleu_scores2)

print("\nFeedback Self BLEU Scores:")
print("Feedback-1 Self Bleu: ", feedback_self_bleu_scores1)
print("Feedback-2 Self Bleu: ", feedback_self_bleu_scores2)
