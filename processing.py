import huggingface_hub
import transformers
from transformers import pipeline
import conversational

def what_type_of_message(message):
    classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")
    labels = ["Conversation", "Classification", "Masking", "Translation"]
    output = classifier(message, labels, multi_label=False)
    return output['labels'][0]


def message_conversation(message):
    return conversational.conversation(message)

def message_masking(message):
    maskfiller = pipeline("fill-mask", model = "distilroberta-base")
    output = maskfiller(message)
    return output[0]["sequence"]