import pandas as pd
import numpy as np
import subject_module
import trans_4_sb
import gender_identifier
import verb_module

transliterator=trans_4_sb.predict_word
Gender_identifier=gender_identifier.gen_id
Conjucate=verb_module.conjugate
data=pd.read_csv("objects_dataset.csv")
print(Gender_identifier("rishi"))
subject_list=subject_module.subject
data=data.set_index("english")
def sentence_builder(subject,objects,verb,tense):
    if subject in subject_list:
        Subject=subject_list[subject]["tamil"]
        subject_type=subject_list[subject]["type"]
    else:
        subject_type='male' if Gender_identifier(subject)==1 else 'female'
        Subject=transliterator(subject)
    if objects in data.index:    
        Object=data.loc[objects,"tamil"]
    else:
        Object=transliterator(objects)    
    Verb_list=Conjucate(verb)
    Verb=Verb_list[tense][subject_type]
    return f"{Subject} {Object} {Verb}"
print(sentence_builder("rishi","school","go","past"))