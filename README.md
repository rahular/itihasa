# Itihāsa

**Update (March 20, 2023)**: You can now do semantic search on the corpus using [this](https://github.com/rahular/itihasa/blob/gh-pages/cli_search.py) script (Uses OpenAI embeddings and FAISS). 

----

Itihāsa is a Sanskrit-English translation corpus containing 93,000 Sanskrit shlokas and their English translations extracted from M. N. Dutt's seminal works on The Rāmāyana and The Mahābhārata. The paper which introduced this dataset can be found [here](https://aclanthology.org/2021.wat-1.22/). 

The `data` folder contains the randomized train, development, and test sets. The original extracted data can be found [here](https://github.com/rahular/itihasa/tree/gh-pages/res) in JSON format. If you just want to browse the data, you can go [here](http://rahular.com/itihasa/).

### Usage

Itihāsa can now be used directly from [Huggingface Datasets](https://huggingface.co/datasets/rahular/itihasa)
```
>> from datasets import load_dataset
>> dataset = load_dataset("rahular/itihasa")
>> dataset
DatasetDict({
    train: Dataset({
        features: ['translation'],
        num_rows: 75162
    })
    validation: Dataset({
        features: ['translation'],
        num_rows: 6149
    })
    test: Dataset({
        features: ['translation'],
        num_rows: 11722
    })
})

>> dataset['train'][0]
{'translation': {'en': 'The ascetic Vālmīki asked Nārada, the best of sages and foremost of those conversant with words, ever engaged in austerities and Vedic studies.',
  'sn': 'ॐ तपः स्वाध्यायनिरतं तपस्वी वाग्विदां वरम्। नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुङ्गवम्॥'}}
```

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
