import pandas as pd

df = pd.read_csv("verb_dataset.csv")

verbs = {}

for _, row in df.iterrows():
    verbs[row["english_verb"].lower()] = {
        "root": row["tamil_root"],
        "past": row["past_stem"],
        "present": row["present_stem"],
        "future": row["future_stem"]
    }

# Subject suffixes
suffixes = {
    "first-singular": {
        "past": "ேன்",
        "present": "ேன்",
        "future": "ேன்"
    },

    "first-plural": {
        "past": "ோம்",
        "present": "ோம்",
        "future": "ோம்"
    },

    "second-singular": {
        "past": "ாய்",
        "present": "ாய்",
        "future": "ாய்"
    },

    "second-plural": {
        "past": "ீர்கள்",
        "present": "ீர்கள்",
        "future": "ீர்கள்"
    },

    "male": {
        "past": "ான்",
        "present": "ான்",
        "future": "ான்"
    },

    "female": {
        "past": "ாள்",
        "present": "ாள்",
        "future": "ாள்"
    },

    "third-singular": {
        "past": "து",
        "present": "து",
        "future": "ும்"
    },

    "third-plural": {
        "past": "னர்",
        "present": "னர்",
        "future": "ர்"
    }
}

def conjugate(english_verb):
    english_verb = english_verb.lower()

    if english_verb not in verbs:
        return "Verb not found"

    verb = verbs[english_verb]

    result = {
        "root": verb["root"],
        "past": {},
        "present": {},
        "future": {}
    }

    for subject in suffixes:

        result["past"][subject] = (
            verb["past"] +
            suffixes[subject]["past"]
        )

        result["present"][subject] = (
            verb["present"] +
            suffixes[subject]["present"]
        )

        result["future"][subject] = (
            verb["future"] +
            suffixes[subject]["future"]
        )

    return result


# Example
output = conjugate("go")


