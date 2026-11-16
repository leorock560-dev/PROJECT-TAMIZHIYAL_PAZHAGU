## project credits - TAMIZHIYAL PAZHAGU
- done by 
   RISHIGANESH.S
   HARIKRISHNAN.P

   ANNA UNIVERSITY (BIT- campus),TRICHY-620024
  




# Tamizhiyal Pazhagu - Smart Tamil Learning Assistant

Tamizhiyal Pazhagu is an web based platform , offline Tamil language learning platform designed specifically to help beginners master Tamil through three interactive, rule-based tools. The project addresses the critical challenge of preserving Tamil—one of the world's oldest languages—by making it accessible and easy for learners worldwide to write, speak, and understand Tamil correctly.

The platform is built entirely on the user's laptop with zero external AI dependency, ensuring complete privacy, offline functionality, and instant processing without cloud services.



## The Problem We Solve

Tamil, one of the timeless,profound and majestic languages that connects millennia of heritage with modern expression, now it is facing a critical challenge: **many people worldwide struggle to use and write Tamil properly**. In our digitally connected world, users face three major problems:

1. **Tanglish Dependency:** Most people type Tamil in English phonetics (Tanglish) because they don't know Tamil keyboard layouts or proper Unicode, creating a barrier to authentic Tamil writing.

2. **Grammar Confusion:** When transitioning from spoken Tanglish to written Tamil, learners struggle with grammar rules, tense conjugation, gender agreement, and sentence structure.

3. **Lack of Interactive Learning:** Beginners need real-time feedback and guidance to build confidence in using Tamil, but traditional methods don't provide immediate, interactive help.

## Our Solution: Three Intelligent Tools


#### **Tool 1: Tanglish to Tamil Transliterator**
- **What it does:** Converts English phonetic text (Tanglish) into proper Tamil Unicode in real-time
- **Technology:** TensorFlow + Transliterator Library
- **How it works:** When a user types "Vanakkam Nanba" in English, the system instantly converts it to "வணக்கம் நண்பா" in Tamil Unicode
- **Learning benefit:** Users don't need to know Tamil keyboard layouts; they can type naturally in English and get authentic Tamil output

#### **Tool 2: Dialogue & Sentence Builder**
- **What it does:** Generates grammatically correct Tamil sentences based on user-selected linguistic inputs
- **Technology:** Rule-based system + Scikit-Learn (for gender identification and classification)
- **How it works:** 
  - User selects: Subject (boy, girl, man, woman) + Verb (eat, run, walk) + Tense (past, present, future)
  - System transliterates these inputs and applies grammar rules to generate a complete, correct Tamil sentence
  - Example: Subject "boy" → "பையன்" + Verb "eat" → "சாப்பிட" + Tense "past" → Generates: "பையன் சாப்பிட்டான்" (boy ate)
- **Learning benefit:** Hands-on practice in sentence construction; users learn proper gender agreement, tense conjugation, and sentence structure through experimentation

#### **Tool 3: Grammar Correction & Content Enhancement**
- **What it does:** Identifies and corrects grammatical errors in Tamil sentences with educational explanations
- **Technology:** Custom rule-based classification module (built from scratch)
- **How it works:**
  - User inputs a Tamil sentence (written or transliterated)
  - System analyzes it for errors: tense mistakes, sentence structure issues, spelling errors, verb conjugation problems, gender agreement violations
  - Provides corrected version + detailed explanation so learners understand WHY it was wrong
  - NOT just a replacement tool—it's an educational feedback system
- **Learning benefit:** Helps learners transitioning from Tanglish to proper Tamil understand their mistakes and improve gradually

---


## Technical Foundation

**Frontend:**
- HTML5 and CSS3 for a simple, responsive, beginner-friendly interface

**Backend:**
- Python with Flask/FastAPI for API and logic handling
- TensorFlow: Powers the transliteration engine
- Transliterator Library: Converts phonetic inputs to Tamil Unicode
- Scikit-Learn: Used for gender classification and machine learning components
- Custom Rule-Based Systems: Grammar correction and sentence building logic

## Features
    100% Offline
- All processing happens locally on your laptop
- No internet connection needed
- No external AI or cloud services
- Complete privacy—your data never leaves your machine
- Instant processing without network latency


## Who This Is For

- **School students** learning Tamil in curriculum
- **College learners** studying Tamil language
- **Individuals worldwide** wanting to preserve and learn their Tamil heritage
- **Beginners** struggling with Tamil grammar and typing
- **Anyone** transitioning from Tanglish to authentic Tamil Unicode
## Key Innovation


Unlike popular language learning apps that depend on cloud-based AI and internet connectivity, Tamizhiyal Pazhagu is completely self-contained. You run it on your own laptop with your own trained models and rule-based systems. This delivers:
- **Privacy:** No data sent to external servers
- **Speed:** Instant processing without waiting for cloud responses
- **Reliability:** Works offline, anytime, anywhere
- **Customization:** Rules can be modified and improved locally
- **No Costs:** Free, open-source, no subscriptions

## requirements 
- pip install flask
- pip install flask-cors
- pip installl numpy
- pip install pandas
- pip install scikit-learn
- pip install joblib
- pip install tensorflow
- pip install torch
- pip install transformers
- pip install regex

## installation steps
1. extract the folder
2. import in VScode 
3. install all the requirements as i mentioned above
4. to run backend open the file "backend.py" run it
5. In the terminal enter "python backend.py"
6. open the frontend file in vs code and click " go live " in the right bottom corner
7. the frontend page will be appear in the screen 



