from transformers import pipeline

trans = pipeline("translation_English_to_German")
output = trans("Hi")