# Itihāsa

**Update (March 20, 2023)**: You can now do semantic search on the corpus using this script.

- To use the script, get a key from OpenAI ([link](https://platform.openai.com/account/api-keys)) and add it to your environment `export OPENAI_API_KEY="<yourkey>"`.

----

Itihāsa is a Sanskrit-English translation corpus containing 93,000 Sanskrit shlokas and their English translations extracted from M. N. Dutt's seminal works on The Rāmāyana and The Mahābhārata. The paper which introduced this dataset can be found [here](https://aclanthology.org/2021.wat-1.22/). 

The `data` folder contains the randomized train, development, and test sets. The original extracted data can be found [here](https://github.com/rahular/itihasa/tree/gh-pages/res) in JSON format. If you just want to browse the data, you can go [here](http://rahular.com/itihasa/).

### Citation
If you found this dataset to be useful, please consider citing the paper as follows:
```
@inproceedings{aralikatte-etal-2021-itihasa,
    title = "Itihasa: A large-scale corpus for {S}anskrit to {E}nglish translation",
    author = "Aralikatte, Rahul  and
      de Lhoneux, Miryam  and
      Kunchukuttan, Anoop  and
      S{\o}gaard, Anders",
    booktitle = "Proceedings of the 8th Workshop on Asian Translation (WAT2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.wat-1.22",
    pages = "191--197",
    abstract = "This work introduces Itihasa, a large-scale translation dataset containing 93,000 pairs of Sanskrit shlokas and their English translations. The shlokas are extracted from two Indian epics viz., The Ramayana and The Mahabharata. We first describe the motivation behind the curation of such a dataset and follow up with empirical analysis to bring out its nuances. We then benchmark the performance of standard translation models on this corpus and show that even state-of-the-art transformer architectures perform poorly, emphasizing the complexity of the dataset.",
}
```
