# NER_models
LLM models for NER tasks

**IOB-1** :-

_json2IOB.py_ file is converting json file of my annotations to IOB format. But, it has only 'I' and 'B' tags with my labels. the text that has 'o' tag isn't present in the output conll file

_process.py_ converts all the HTML docs into IOB format and encodes each word with 'O' and dumps it into 'processed.iob' file. - all the words are encoded with 'O'

Need to find a way to merge conll and iob file to get IOB format. 

**IOB_tagging** :- 

converts json file to IOB format. 

gives output in a text file. 

**t-ner notebook** :-

code to load the train, test and validation datasets, as well as the 'label2id' dictionary.

fine-tuned "roberta-base" for 2 epochs. 

attached below is the ss for the metrics after training for 2 epochs.


![image](https://github.com/user-attachments/assets/ff57c5e4-242b-4c50-896f-49b961e20f8a)




**t-ner repo** :- https://github.com/asahi417/tner
