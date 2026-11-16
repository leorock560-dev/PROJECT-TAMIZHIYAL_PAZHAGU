import unicodedata
import classification

class TamilGrammarCorrector:
    def __init__(self):
        self._init_data()

    def _normalize(self, text):
        return unicodedata.normalize('NFC', text) if text else text

    def _init_data(self):
        self.subjects = {
            'நான்': ('first', 'singular'),
            'நாங்கள்': ('first', 'plural'),
            'நாம்': ('first', 'plural'),
            'நீ': ('second', 'singular'),
            'நீங்கள்': ('second', 'plural'),
            'அவன்': ('third', 'singular_m'),
            'இவன்': ('third', 'singular_m'),
            'அவள்': ('third', 'singular_f'),
            'இவள்': ('third', 'singular_f'),
            'அவர்': ('third', 'singular_h'),
            'இவர்': ('third', 'singular_h'),
            'அவர்கள்': ('third', 'plural'),
            'இவர்கள்': ('third', 'plural'),
        }
        self.suffixes = [
            ('கிறேன்', 'first', 'singular'),
            ('கிறாய்', 'second', 'singular'),
            ('கிறான்', 'third', 'singular_m'),
            ('கிறாள்', 'third', 'singular_f'),
            ('கிறார்', 'third', 'singular_h'),
            ('கிறோம்', 'first', 'plural'),
            ('கிறீர்கள்', 'second', 'plural'),
            ('கிறார்கள்', 'third', 'plural'),
            ('ேன்', 'first', 'singular'),
            ('ாய்', 'second', 'singular'),
            ('ான்', 'third', 'singular_m'),
            ('ாள்', 'third', 'singular_f'),
            ('ார்', 'third', 'singular_h'),
            ('ோம்', 'first', 'plural'),
            ('ீர்கள்', 'second', 'plural'),
            ('ார்கள்', 'third', 'plural'),
        ]
        self.suffixes.sort(key=lambda x: -len(x[0]))
        self.suffix_map = {}
        for suf, p, n in self.suffixes:
            tense = 'present' if 'கிற' in suf else 'past'
            self.suffix_map[(p, n, tense)] = suf
        self.stems = {
            'பேசின': 'பேசு', 'பேசுகி': 'பேசு',
            'படித்த': 'படி', 'படிக்கி': 'படி',
            'அழுத': 'அழு', 'அழுகி': 'அழு',
            'விளையாடின': 'விளையாடு', 'விளையாடுகி': 'விளையாடு',
            'கேட்ட': 'கேள்', 'கேட்கி': 'கேள்',
            'சாப்பிட்ட': 'சாப்பிடு', 'சாப்பிடுகி': 'சாப்பிடு',
            'எழுதின': 'எழுது', 'எழுதுகி': 'எழுது',
            'நடந்த': 'நட', 'நடக்கி': 'நட',
            'பாடின': 'பாடு', 'பாடுகி': 'பாடு',
            'எழுந்த': 'எழு', 'எழுகி': 'எழு',
            'சிரித்த': 'சிரி', 'சிரிக்கி': 'சிரி',
            'பார்த்த': 'பார்', 'பார்க்கி': 'பார்',
            'குடித்த': 'குடி', 'குடிக்கி': 'குடி',
            'தூங்கின': 'தூங்கு', 'தூங்குகி': 'தூங்கு',
            'போன': 'போ', 'போகி': 'போ',
            'ஓடின': 'ஓடு', 'ஓடுகி': 'ஓடு',
        }
        self.spelling_map = {
            'பேசிணேன்': 'பேசினேன்', 'பேசிணான்': 'பேசினான்', 'பேசிணாள்': 'பேசினாள்',
            'பேசிணோம்': 'பேசினோம்', 'பேசிணார்கள்': 'பேசினார்கள்',
            'படிச்சேன்': 'படித்தேன்', 'படிச்சான்': 'படித்தான்', 'படிச்சாள்': 'படித்தாள்',
            'படிச்சோம்': 'படித்தோம்', 'படிச்சார்கள்': 'படித்தார்கள்',
            'அழுந்தேன்': 'அழுதேன்', 'அழுந்தான்': 'அழுதான்', 'அழுந்தாள்': 'அழுதாள்',
            'விளையாடிணேன்': 'விளையாடினேன்', 'விளையாடிணான்': 'விளையாடினான்', 'விளையாடிணாள்': 'விளையாடினாள்',
            'சிரிச்சேன்': 'சிரித்தேன்', 'சிரிச்சான்': 'சிரித்தான்', 'சிரிச்சாள்': 'சிரித்தாள்',
            'பாடிணேன்': 'பாடினேன்', 'பாடிணான்': 'பாடினான்', 'பாடிணாள்': 'பாடினாள்',
            'பாடிணோம்': 'பாடினோம்', 'பாடிணார்கள்': 'பாடினார்கள்',
            'எழுதிணேன்': 'எழுதினேன்', 'எழுதிணான்': 'எழுதினான்', 'எழுதிணாள்': 'எழுதினாள்',
            'ஓடிணேன்': 'ஓடினேன்', 'ஓடிணான்': 'ஓடினான்', 'ஓடிணாள்': 'ஓடினாள்',
            'தூங்கிணேன்': 'தூங்கினேன்', 'தூங்கிணான்': 'தூங்கினான்', 'தூங்கிணாள்': 'தூங்கினாள்',
            'குடிச்சேன்': 'குடித்தேன்', 'குடிச்சான்': 'குடித்தான்', 'குடிச்சாள்': 'குடித்தாள்',
            'பேசுறேன்': 'பேசுகிறேன்', 'பேசுறான்': 'பேசுகிறான்', 'பேசுறாள்': 'பேசுகிறாள்',
            'படிக்கிறேன்': 'படிக்கிறேன்', 
            'படிக்கிறான்': 'படிக்கிறான்',
            'ஓடுறேன்': 'ஓடுகிறேன்', 'ஓடுறான்': 'ஓடுகிறான்', 'ஓடுறாள்': 'ஓடுகிறாள்',
            'சிரிக்கிறேன்': 'சிரிக்கிறேன்',
        }

        self.pronoun_map = {
            'நீங்': 'நீங்கள்', 'நீகள்': 'நீங்கள்', 'நீங்க': 'நீங்கள்',
            'அவன்கள்': 'அவர்கள்', 'அவள்கள்': 'அவர்கள்',
            'இவன்கள்': 'இவர்கள்', 'இவள்கள்': 'இவர்கள்',
            'நான்கள்': 'நாங்கள்', 'நாம்கள்': 'நாங்கள்',
            'தாங்கள்': 'நீங்கள்',
        }


        self.case_map = {
            'அய்': 'ஐ',
            'ஐய்': 'ஐ',
            'கு': 'க்கு',
            'இல்': 'இல்',     
            'இருந்து': 'இருந்து',
            'விட்டு': 'விட்டு',
            'உடன்': 'உடன்',
            'காக': 'க்காக',
            'ஆல்': 'ஆல்',
            'ஐது': 'ஐ',
            'அது': 'அது',
            'கு': 'க்கு',
        }

        # Time adverbs for tense detection
        self.past_indicators = ['நேற்று', 'நேற்றைக்கு', 'முன்', 'முன்னால்', 'முன்பு',
                                'கடந்த', 'சற்றுமுன்', 'அப்போது', 'பின்னால்', 'பின்',
                                'பின்பு', 'அன்று', 'முதல்']
        self.present_indicators = ['இப்போது', 'இப்பொழுது', 'தற்போது', 'தற்சமயம்',
                                   'இன்று', 'அடுத்த', 'நாளை', 'இனி', 'இப்ப']
        self.future_indicators = ['நாளை', 'நாளைக்கு', 'இனிமேல்', 'அடுத்த', 'வரும்']

        # Extra/filler words to remove
        self.extra_words = {'தான்', 'ஏ', 'டா', 'டி', 'தா', 'தானே', 'என்பது', 'ஆகும்', 'என்று',
                            'ஓ', 'டா', 'டி', 'தான்'}

        # Missing word patterns: (pattern, missing_word, position)
        # If the sentence matches a pattern, insert the missing word
        self.missing_word_patterns = [
            # Object without accusative case marker
            (r'\b(அவன்|அவள்|நான்|நீ|அது)\s+(பார்|செய்|கொடு|எடு|வா)', r'\1ஐ \2'),
            # Postposition missing after noun
            (r'\b(வீடு|பள்ளி|கடை|நகர்|ஊர்)\s+(செல்|வா|போ)', r'\1க்கு \2'),
            (r'\b(வீடு|பள்ளி|கடை)\s+(இரு|உள்)', r'\1இல் \2'),
        ]



    def _match_suffix(self, verb):
        """Return (person, number, suffix_string, base) or None."""
        verb = self._normalize(verb)
        for suffix_str, person, number in self.suffixes:
            if verb.endswith(suffix_str):
                return (person, number, suffix_str, verb[:-len(suffix_str)])
        return None

    def _get_subject_info(self, word):
        key = self._normalize(word)
        return self.subjects.get(key, (None, None))

    def _get_tense(self, verb):
        return 'present' if 'கிற' in verb else 'past'

    def _correct_verb(self, verb, target_person, target_number):
        """Rebuild verb with correct suffix for target person/number."""
        verb = self._normalize(verb)
        tense = self._get_tense(verb)
        match = self._match_suffix(verb)
        if match is None:
            return verb

        _, _, suffix, base = match
        correct_suffix = self.suffix_map.get((target_person, target_number, tense))
        if correct_suffix is None:
            return verb

        # Find best stem from dictionary
        best_stem = base
        for known_stem in sorted(self.stems.keys(), key=len, reverse=True):
            if base.endswith(known_stem) or known_stem.endswith(base):
                best_stem = known_stem
                break
            if known_stem in base:
                best_stem = known_stem
                break

        return best_stem + correct_suffix

    def correct_spelling_error(self, sentence):
        """Fix common spelling mistakes in verbs and words."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        result = []

        for word in words:
            # Direct match in spelling map
            if word in self.spelling_map:
                result.append(self.spelling_map[word])
            else:
                result.append(word)

        return ' '.join(result)



    def correct_number_agreement(self, sentence):
        """Fix plural subject + singular verb."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        if len(words) < 2:
            return sentence

        subject = words[0]
        verb = words[-1]

        sub_person, sub_number = self._get_subject_info(subject)
        if sub_person is None:
            return sentence

        vmatch = self._match_suffix(verb)
        if vmatch is None:
            return sentence

        v_person, v_number, _, _ = vmatch

        if sub_number == 'plural' and v_number != 'plural':
            if subject in ('நாம்', 'நாங்கள்'):
                target = ('first', 'plural')
            else:
                target = ('third', 'plural')
            words[-1] = self._correct_verb(verb, target[0], target[1])
            return ' '.join(words)

        return sentence


    def correct_subject_verb_agreement(self, sentence):
        """Fix person mismatch between subject and verb."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        if len(words) < 2:
            return sentence

        subject = words[0]
        verb = words[-1]

        sub_person, sub_number = self._get_subject_info(subject)
        if sub_person is None:
            return sentence

        vmatch = self._match_suffix(verb)
        if vmatch is None:
            return sentence

        v_person, v_number, _, _ = vmatch

        if sub_person != v_person:
            words[-1] = self._correct_verb(verb, sub_person, sub_number)
            return ' '.join(words)

        if sub_number == 'plural' and v_number != 'plural':
            return self.correct_number_agreement(sentence)

        return sentence

    def correct_gender_agreement(self, sentence):
        """Fix gender mismatch in third person."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        if len(words) < 2:
            return sentence

        subject = words[0]
        verb = words[-1]

        sub_person, sub_number = self._get_subject_info(subject)
        if sub_person is None:
            return sentence

        vmatch = self._match_suffix(verb)
        if vmatch is None:
            return sentence

        v_person, v_number, _, _ = vmatch

        if sub_person != 'third' or v_person != 'third':
            return sentence

        # Number mismatch
        if sub_number == 'plural' and v_number != 'plural':
            return self.correct_number_agreement(sentence)
        if sub_number != 'plural' and v_number == 'plural':
            words[-1] = self._correct_verb(verb, sub_person, sub_number)
            return ' '.join(words)

        genders = {'singular_m', 'singular_f'}
        if sub_number in genders and v_number in genders and sub_number != v_number:
            words[-1] = self._correct_verb(verb, sub_person, sub_number)
            return ' '.join(words)

        return sentence

    def correct_tense_error(self, sentence):
        """Fix tense based on time adverbs in the sentence."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        if len(words) < 2:
            return sentence

        verb = words[-1]
        vmatch = self._match_suffix(verb)
        if vmatch is None:
            return sentence

        v_person, v_number, _, _ = vmatch
        current_tense = self._get_tense(verb)

        has_past = any(ind in sentence for ind in self.past_indicators)
        has_present = any(ind in sentence for ind in self.present_indicators)
        has_future = any(ind in sentence for ind in self.future_indicators)

        if has_past and current_tense == 'present':
            target_suffix = self.suffix_map.get((v_person, v_number, 'past'))
            if target_suffix:
                _, _, _, base = vmatch
                words[-1] = base + target_suffix
                return ' '.join(words)

        elif has_present and current_tense != 'present':
            target_suffix = self.suffix_map.get((v_person, v_number, 'present'))
            if target_suffix:
                _, _, _, base = vmatch
                words[-1] = base + target_suffix
                return ' '.join(words)

        elif has_future and current_tense == 'present':
            pass

        return sentence

    def correct_pronoun_error(self, sentence):
        """Fix incorrect pronoun forms."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        if len(words) < 1:
            return sentence

        if words[0] in self.pronoun_map:
            words[0] = self.pronoun_map[words[0]]
            return ' '.join(words)

        for i in range(1, len(words)):
            if words[i] in self.pronoun_map:
                words[i] = self.pronoun_map[words[i]]

        return ' '.join(words)


    def correct_case_marker_error(self, sentence):
        """Fix wrong case markers/postpositions on nouns and pronouns."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        result = []

        for word in words:
            replaced = False
        
            for wrong in sorted(self.case_map.keys(), key=len, reverse=True):
                if len(word) <= len(wrong):
                    continue
                    
            
                word_end = word[-len(wrong):]
                
                
                match = True
                for i in range(len(wrong)):
                    if word_end[i] != wrong[i]:
                        match = False
                        break
                
                if match:
                    base = word[:-len(wrong)]
                    correct = self.case_map[wrong]
                    result.append(base + correct)
                    replaced = True
                    break
                    
            if not replaced:
                result.append(word)

        return ' '.join(result)


    def correct_missing_word(self, sentence):
        """Add missing case markers or postpositions."""
        sentence = self._normalize(sentence)
        words = sentence.split()

        transitive_verbs = ['பார்', 'செய்', 'கொடு', 'எடு', 'வா', 'அனுப்பு', 'எழுது']
        if len(words) >= 2:
            for i in range(len(words) - 1):
                word = words[i]
                next_word = words[i + 1]
                case_markers_end = ('ஐ', 'க்', 'இல்', 'இருந்து', 'உடன்', 'க்கு', 'ஆல்')
                if not word.endswith(case_markers_end):
                    sub_info = self._get_subject_info(word)
                    if sub_info[0] is not None and word != words[0]:
                        
                        next_root = next_word
                        vmatch = self._match_suffix(next_word)
                        if vmatch:
                            _, _, _, next_root = vmatch
                        if next_root in transitive_verbs:
                            words[i] = word + 'ஐ'
                            return ' '.join(words)

        
        directional_verbs = ['செல்', 'வா', 'போ', 'வரு']
        if len(words) >= 2:
            for i in range(len(words) - 1):
                word = words[i]
                next_word = words[i + 1]
                next_root = next_word
                vmatch = self._match_suffix(next_word)
                if vmatch:
                    _, _, _, next_root = vmatch
                if next_root in directional_verbs and not word.endswith(('க்கு', 'இல்', 'ஐ')):
                    if self._get_subject_info(word)[0] is None:
                        words[i] = word + 'க்கு'
                        return ' '.join(words)

        return sentence

    def correct_extra_word(self, sentence):
        """Remove filler/extra words."""
        sentence = self._normalize(sentence)
        words = sentence.split()
        result = [w for w in words if w not in self.extra_words]

        if not result:
            return sentence

        return ' '.join(result)


    def correct_no_error(self, sentence):
        """Pass-through for correct sentences."""
        return sentence

    def correct(self, sentence, error_type):
        """Call with sentence and error_type string."""
        sentence = self._normalize(sentence)

        handlers = {
            'spelling_error': self.correct_spelling_error,
            'number_agreement': self.correct_number_agreement,
            'subject_verb_agreement': self.correct_subject_verb_agreement,
            'gender_agreement': self.correct_gender_agreement,
            'tense_error': self.correct_tense_error,
            'pronoun_error': self.correct_pronoun_error,
            'case_marker_error': self.correct_case_marker_error,
            'missing_word': self.correct_missing_word,
            'extra_word': self.correct_extra_word,
            'no_error': self.correct_no_error,
        }

        handler = handlers.get(error_type)
        if handler is None:
            raise ValueError(f"Unknown error type: {error_type}")

        return handler(sentence)


    def run_tests(self):
        test_cases = [
            ('நான் பேசிணேன்', 'spelling_error', 'நான் பேசினேன்'),
            ('அவன் பேசிணான்', 'spelling_error', 'அவன் பேசினான்'),
            ('அவள் பேசிணாள்', 'spelling_error', 'அவள் பேசினாள்'),
            ('நான் படிச்சேன்', 'spelling_error', 'நான் படித்தேன்'),
            ('அவன் படிச்சான்', 'spelling_error', 'அவன் படித்தான்'),
            ('நான் சிரிச்சேன்', 'spelling_error', 'நான் சிரித்தேன்'),

            
            ('நாங்கள் பேசினேன்', 'number_agreement', 'நாங்கள் பேசினோம்'),
            ('அவர்கள் படித்தாள்', 'number_agreement', 'அவர்கள் படித்தார்கள்'),
            ('நாம் எழுந்தேன்', 'number_agreement', 'நாம் எழுந்தோம்'),
            ('அவர்கள் சிரித்தான்', 'number_agreement', 'அவர்கள் சிரித்தார்கள்'),
            ('அவர்கள் அழுதான்', 'number_agreement', 'அவர்கள் அழுதார்கள்'),
            ('நாங்கள் ஓடுகிறேன்', 'number_agreement', 'நாங்கள் ஓடுகிறோம்'),
            ('நாங்கள் அழுதேன்', 'number_agreement', 'நாங்கள் அழுதோம்'),
            ('நாங்கள் விளையாடினேன்', 'number_agreement', 'நாங்கள் விளையாடினோம்'),
            ('நாங்கள் கேட்டேன்', 'number_agreement', 'நாங்கள் கேட்டோம்'),
            ('நாம் கேட்டேன்', 'number_agreement', 'நாம் கேட்டோம்'),
            ('நாங்கள் பாடுகிறேன்', 'number_agreement', 'நாங்கள் பாடுகிறோம்'),
            ('நாங்கள் பேசுகிறேன்', 'number_agreement', 'நாங்கள் பேசுகிறோம்'),
            ('நாம் சாப்பிட்டேன்', 'number_agreement', 'நாம் சாப்பிட்டோம்'),
            ('நாங்கள் அழுகிறேன்', 'number_agreement', 'நாங்கள் அழுகிறோம்'),
            ('அவர்கள் எழுதினான்', 'number_agreement', 'அவர்கள் எழுதினார்கள்'),
            ('அவர்கள் நடந்தான்', 'number_agreement', 'அவர்கள் நடந்தார்கள்'),
            ('அவர்கள் பாடினாள்', 'number_agreement', 'அவர்கள் பாடினார்கள்'),
            ('அவர்கள் எழுந்தான்', 'number_agreement', 'அவர்கள் எழுந்தார்கள்'),
            ('அவர்கள் விளையாடினான்', 'number_agreement', 'அவர்கள் விளையாடினார்கள்'),
            ('அவர்கள் சிரித்தாள்', 'number_agreement', 'அவர்கள் சிரித்தார்கள்'),
            ('நாங்கள் நடந்தேன்', 'number_agreement', 'நாங்கள் நடந்தோம்'),

            
            ('நான் பேசினாள்', 'subject_verb_agreement', 'நான் பேசினேன்'),
            ('நான் ஓடுகிறாள்', 'subject_verb_agreement', 'நான் ஓடுகிறேன்'),
            ('நான் விளையாடினார்கள்', 'subject_verb_agreement', 'நான் விளையாடினேன்'),
            ('நான் படிக்கிறான்', 'subject_verb_agreement', 'நான் படிக்கிறேன்'),
            ('நான் பார்த்தார்கள்', 'subject_verb_agreement', 'நான் பார்த்தேன்'),
            ('நான் சிரித்தார்கள்', 'subject_verb_agreement', 'நான் சிரித்தேன்'),
            ('நான் குடித்தார்கள்', 'subject_verb_agreement', 'நான் குடித்தேன்'),
            ('நான் அழுதான்', 'subject_verb_agreement', 'நான் அழுதேன்'),
            ('நான் நடந்தான்', 'subject_verb_agreement', 'நான் நடந்தேன்'),
            ('நான் தூங்குகிறாள்', 'subject_verb_agreement', 'நான் தூங்குகிறேன்'),
            ('நான் சாப்பிட்டாள்', 'subject_verb_agreement', 'நான் சாப்பிட்டேன்'),
            ('நான் படிக்கிறாள்', 'subject_verb_agreement', 'நான் படிக்கிறேன்'),
            ('நான் அழுகிறாள்', 'subject_verb_agreement', 'நான் அழுகிறேன்'),
            ('நான் போகிறாள்', 'subject_verb_agreement', 'நான் போகிறேன்'),
            ('நான் அழுதார்கள்', 'subject_verb_agreement', 'நான் அழுதேன்'),
            ('நான் சிரித்தாள்', 'subject_verb_agreement', 'நான் சிரித்தேன்'),

            
            ('அவன் பாடினாள்', 'gender_agreement', 'அவன் பாடினான்'),
            ('அவள் பேசினான்', 'gender_agreement', 'அவள் பேசினாள்'),
            ('அவன் சிரித்தாள்', 'gender_agreement', 'அவன் சிரித்தான்'),
            ('அவள் எழுதினான்', 'gender_agreement', 'அவள் எழுதினாள்'),

        
            ('நேற்று பேசுகிறான்', 'tense_error', 'நேற்று பேசினான்'),
            ('அப்போது ஓடுகிறேன்', 'tense_error', 'அப்போது ஓடினேன்'),

            
            ('நான்கள் வந்தோம்', 'pronoun_error', 'நாங்கள் வந்தோம்'),
            ('அவன்கள் வந்தார்கள்', 'pronoun_error', 'அவர்கள் வந்தார்கள்'),

            
            ('நான் தான் வந்தேன்', 'extra_word', 'நான் வந்தேன்'),
            ('அவன் தானே பேசினான்', 'extra_word', 'அவன் பேசினான்'),

            
            ('நான் பேசினேன்', 'no_error', 'நான் பேசினேன்'),
            ('அவன் பேசினான்', 'no_error', 'அவன் பேசினான்'),
            ('அவள் பேசினாள்', 'no_error', 'அவள் பேசினாள்'),
            ('நாங்கள் பேசினோம்', 'no_error', 'நாங்கள் பேசினோம்'),
            ('அவர்கள் பேசினார்கள்', 'no_error', 'அவர்கள் பேசினார்கள்'),

            
            ('நான் சினிமா வந்தேன்', 'case_marker_error', 'நான் சினிமாவிற்கு வந்தேன்'),
        ]

        correct = 0
        total = len(test_cases)
        print("=" * 60)
        print("TAMIL GRAMMAR CORRECTOR — ALL MODULES")
        print("=" * 60)
        for sent, etype, expected in test_cases:
            result = self.correct(sent, etype)
            ok = result == expected
            if ok:
                correct += 1
            sym = '✓' if ok else '✗'
            print(f"{sym} [{etype:25s}] '{sent}' -> '{result}'")
            if not ok:
                print(f"  {' ' * 28}Expected: '{expected}'")
        print()
        print("=" * 60)
        print(f"RESULTS: {correct}/{total} correct ({100*correct/total:.1f}%)")
        print("=" * 60)

Explanations = {

    "subject_verb_agreement":
    "The subject and verb forms do not agree.",

    "gender_agreement":
    "The gender of the subject does not match the verb form.",

    "number_agreement":
    "The subject and verb differ in number.",

    "tense_error":
    "The tense used is incorrect.",

    "case_marker_error":
    "A required Tamil case marker is missing or incorrect.",

    "pronoun_error":
    "An incorrect pronoun form is used.",

    "spelling_error":
    "The sentence contains a spelling mistake.",

    "missing_word":
    "A required word is missing from the sentence.",

    "extra_word":
    "The sentence contains an unnecessary word.",

    "no_error":
    "The sentence is grammatically correct."
}
c = TamilGrammarCorrector()
if __name__ == "__main__":
     c.run_tests()
classifier=classification.classify
def correct_sentence(sent):
    err_type=classifier([sent])[0]
    print(err_type)
    return c.correct(sent,err_type), err_type, Explanations[err_type]
sentence="அவன் சினிமா வந்தாள்"
print(correct_sentence(sentence))