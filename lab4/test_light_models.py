from transformers import pipeline
import time

# Run this script with `python3 test_light_models.py`

# Test sentences
test_sentences = [
  "I really enjoyed this movie, it was fantastic!",
  "मैं आज बहुत खुश हूं",  
  "This product is terrible, would not recommend.",
  "बहुत बढ़िया खाना था", 
  "The weather is quite pleasant today."
]

def test_sentiment_model():
  start_time = time.time()
  pipeline_sentiment = pipeline(
      "sentiment-analysis",
      model="distilbert-base-uncased-finetuned-sst-2-english",
      device=-1
  )
  print("Sentiment Analysis Light model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_sentiment(text)[0]
      # print(f"Result for '{text}': {result}")
  print("Sentiment Analysis Light pipeline time: ", time.time() - start_time)

def test_language_classification():
  start_time = time.time()
  id2label = {
      'LABEL_4': 'en', 
      'LABEL_7': 'hi',
  }
  
  pipeline_lang = pipeline(
      "text-classification",
      model="niharrp9/distilbert-base-multilingual-cased-finetuned-language-identification",
      device=-1
  )
  print("Language Classification Light model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_lang(text, top_k=1, truncation=True)[0]
      lang_code = id2label.get(result['label'], result['label'])
      # print(f"Result for '{text}': {{'language': '{lang_code}', 'score': {result['score']:.4f}}}")
  print("Language Classification Light pipeline time: ", time.time() - start_time)

def test_translation():
  start_time = time.time()
  pipeline_trans = pipeline(
      "translation",
      model="Helsinki-NLP/opus-mt-mul-en",
      device=-1
  )
  print("Translation Light model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_trans(text)[0]
      # print(f"Result for '{text}': {result}")
  print("Translation Light pipeline time: ", time.time() - start_time)

if __name__ == "__main__":
  test_sentiment_model()
  test_language_classification()
  test_translation()