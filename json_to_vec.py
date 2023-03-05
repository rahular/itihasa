import json
import faiss
import numpy as np
import pandas as pd

from tqdm import tqdm
from openai.embeddings_utils import get_embedding

index_path = "res/index.bin"


def get_df(book):
    # there must be a better way to do this, but I'm a Pandas noob
    df = pd.DataFrame(
        columns=["book", "volume", "parva", "cnum", "chapter", "description", "shloka", "sn", "en"]
    )
    with open(f"res/{book}.json", "r") as f:
        data = json.load(f)
    for vol in tqdm(data.keys(), desc="Volumes", leave=False):
        prev_parva = None
        for cnum, chapter in tqdm(enumerate(data[vol]), desc="Chapters", leave=False):
            cname = chapter["chapter"]
            parva = chapter.get("parva", prev_parva)
            desc = chapter.get("description", None)
            prev_parva = parva if parva else prev_parva
            for idx, (s, e) in enumerate(zip(chapter["sn"], chapter["en"])):
                df.loc[len(df)] = {
                    "book": book,
                    "volume": vol,
                    "parva": parva,
                    "cnum": cnum+1,
                    "chapter": cname,
                    "description": desc,
                    "shloka": idx+1,
                    "sn": s,
                    "en": e,
                }
    return df


def create_index(df):
    df["embedding"] = df.en.apply(lambda x: get_embedding(x, engine="text-embedding-ada-002"))
    df["embedding"] = df.embedding.apply(lambda x: np.array(x))
    embs = np.stack(df["embedding"], axis=0)
    index = faiss.IndexFlatIP(embs.shape[1])
    index.add(embs)
    faiss.write_index(index, index_path)


def main():
    print("Getting embeddings for Ramayana...")
    rdf = get_df("ramayana")
    print("Getting embeddings for Mahabharata...")
    mdf = get_df("mahabharata")
    
    df = pd.concat([rdf, mdf])
    df = df.where(pd.notnull(df), None)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # just in case
    df.to_csv("res/combined.csv", index=False)

    # print("Creating index...")
    # create_index(df)


if __name__ == "__main__":
    main()
