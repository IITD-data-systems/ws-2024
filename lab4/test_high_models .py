from transformers import pipeline
import time

# Run this script with `python3 test_heavy_models.py`

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
      model="cardiffnlp/twitter-roberta-base-sentiment",
      device=-1
  )
  print("Sentiment Analysis Heavy model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_sentiment(text)[0]
      # print(f"Result for '{text}': {result}")
  print("Sentiment Analysis Heavy pipeline time: ", time.time() - start_time)

def test_language_classification():
  start_time = time.time()
  pipeline_lang = pipeline(
      "text-classification",
      model="papluca/xlm-roberta-base-language-detection",
      device=-1
  )
  print("Language Classification Heavy model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_lang(text, top_k=1, truncation=True)[0]
      # print(f"Result for '{text}': {result}")
  print("Language Classification Heavy pipeline time: ", time.time() - start_time)

def test_translation():
  start_time = time.time()
  pipeline_trans = pipeline(
      "translation",
      model="facebook/nllb-200-distilled-600M",
      device=-1
  )
  print("Translation Heavy model loading time: ", time.time() - start_time)

  start_time = time.time()
  for text in test_sentences:
      result = pipeline_trans(text, src_lang="hin_Deva", tgt_lang="eng_Latn", max_length=128)[0]
      # print(f"Result for '{text}': {result}")
  print("Translation Heavy pipeline time: ", time.time() - start_time)

if __name__ == "__main__":
  test_sentiment_model()
  test_language_classification()
  test_translation()