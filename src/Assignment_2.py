import argparse
import os
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from collections import Counter
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

# Empty lists
polarity = []
entities = []
entity_count = []

# importing data
def import_data():
    filepath = os.path.join("..",
                            "fake_or_real_news.csv")
    data = pd.read_csv(filepath)
    del data["Unnamed: 0"]
    return data
                            
# Choosing real or fake news and running nlp
def label_split(data, label):
    label_news_df = data[data["label"] == label]
                            
    for headline in label_news_df["title"]:
        doc = nlp(headline)
        score = doc._.blob.polarity
        polarity.append(score)
    
    for ents in label_news_df["title"]:
        doc = nlp(ents)
        tmp_list = []
        for entity in doc.ents:
            if entity.label_ == "GPE":
                entity_count.append(entity.text)
                tmp_list.append(entity.text)
        entities.append(tmp_list)
    
    df_label = pd.DataFrame(label_news_df)
    df_label["Sentiment"] = polarity 
    df_label["Named Entities"] = entities
    
    return df_label
                            
def output_data(df_label, output, label):
    if output == None:
         outpath = os.path.join("..", "out", label+"_news_output.csv")
        df_label.to_csv(outpath, index=False)
    else:
        outpath = os.path.join(output, label+"_news_output.csv")
        df_label.to_csv(outpath, index=False)
                            
def entity_counter(top, label):
    if top == None:
        pass
    else:
        top_ent = Counter(entity_count).most_common(int(top))
        print(f"\nTop {top} entities in the {label} dataset:\n{top_ent}")
    
# Parsing
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--label", required = True, help="The user defined data")
    ap.add_argument("-o", "--output", required = False, help="The user defined output folder")
    ap.add_argument("-t", "--top", required = False, help="User defined list of counted values")
    args = vars(ap.parse_args())
    return args

# Defining main
def main():
    args = parse_args()
    data = import_data()
    df_label = label_split(data, args["label"])
    output_data(df_label, args["output"], args["label"])
    entity_counter(args["top"], args["label"])
                            
# Running main
if __name__ == "__main__":
    main()
