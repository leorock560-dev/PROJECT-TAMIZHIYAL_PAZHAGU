import pandas as pd
data=pd.read_csv("grammar_corrector.csv")
X=data['error_type']
x_set=set(X)
print(x_set)

#{'tense_error', 'number_agreement', 'subject_verb_agreement', 'no_error', 'case_marker_error', 'extra_word', 'gender_agreement', 'missing_word', 'spelling_error', 'pronoun_error'}//