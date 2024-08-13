import random
import string
import time


class TheAlphabet:
    def __init__(self, lang: str, case: str, chars_excluded: str, start_string) -> None:
        self.alphabet_lower = string.ascii_lowercase
        # TODO: FIX LINE BELOW WITH MENU CHOICE
        #self.extra_chars = Settings.r_extra_chars()
        # TODO: FIX LINE BELOW WITH MENU CHOICE
        #self.alphabet_lower += self.extra_chars[lang]
        self.alphabet_lower += start_string
        
        self.case_versions = {"lower": self._case_lower, "UPPER": self._case_upper, "Both": self._case_insensitive, "Both In Order": self._combined}
        self.chars = self.case_versions[case]()
        self.chars = ''.join(c for c in self.chars if c not in chars_excluded)
        
        
    def _case_lower(self):
        return ''.join(self.alphabet_lower.lower())
    
    
    def _case_upper(self):
        return ''.join(self.alphabet_lower.upper())
    
    
    def _combined(self):
        lower = self._case_lower()
        upper = self._case_upper()
        combined = ''.join(sorted(''.join(pair) for pair in zip(upper, lower)))
        return combined
    
    
    def _case_insensitive(self):
        chars = list(self.alphabet_lower)
        uppercase_indices = random.sample(range(len(chars)), len(chars) // 2)
        for i in uppercase_indices:
            chars[i] = chars[i].upper()
            
        return ''.join(chars)
    
    
    def _case_insensitive_org(self):
        chars = [c for c in self.alphabet_lower.lower()]
        for i in range(len(chars)):
            if random.choice([True, False]):
                chars[i] = chars[i].upper()
            else:
                chars[i] = chars[i].lower()

        return ''.join(chars)
    

class LetterHandler():
    """Handles the chars used for the game
    """    
    
    def __init__(self, start_string: str, correct_counter_goal: int, time_limit: int, lang, repetitions, case: str, chars_excluded: str) -> None:
        """_summary_

        Args:
            start_string (str): The first chars to start with (For example the user name).
            correct_counter_goal (int): Times the user presses the right chars in row.
            time_limit (int): Time limit for adding a new char.
            lang (str): The alphabetic language used.
            repetitions (int): How many times each char should occur.
            case (str): UPPER, lower or Both cases.
            chars_excluded (str): Chars to be exluded from used chars.
        """        
        
        self.start_string = start_string
        
        self.correct_counter_goal = correct_counter_goal
        self.time_limit = time_limit
        self.lang = lang
        self.repetitions = repetitions if repetitions else 1
        self.case = case
        self.chars_excluded = chars_excluded
        
        self.last_time_letter_set = 0
        
        self.letter_in_use = ""
        self.correct_counter = 0
        
        # Make sure the start_string is not empty or too short.
        to_add = 4 - len(self.start_string)
        vowels = "aoieu"
        if self.start_string and to_add:
            for _ in range(to_add):
                self.start_string += vowels[0]
                vowels = vowels[1:]
        
        self.alphabet = TheAlphabet(lang, case, chars_excluded, "") # start_string
        
        # Needs to have all the chars
        self.letters_to_add = [] 
        self.available_letters = self.alphabet.chars

        # Add to list available list, only the chars which in start_string, keeping cases. 
        if self.start_string:
            self.available_letters = [*self.alphabet.chars * self.repetitions]
            [self.add_to_available_letters(c) for c in self.letters_to_add if c.lower() in self.start_string.lower()]
        else:
            if case == "Both In Order":
                self.available_letters = [*self.alphabet.chars]
            else:
                self.available_letters = [*sorted(self.alphabet.chars, key=sorted)]
            
            
    def get_rand_addition(self):
        rand = [c for c in self.alphabet.chars if c not in self.letter_in_use]
        
        return random.choice(rand)

    '''
    chatgpt times: 1
    '''
    def add_to_available_letters(self, char):
        """Adds a character to the available_letters list and removes any previously used character.

        Args:
            char (str): The character to add to the available_letters list.

        Raises:
            ValueError: If self.letters_to_add is empty and char is not in it.
        """
        try:
            if self.letter_in_use:
                self.available_letters.remove(self.letter_in_use)
        except:
            print("self.available_letters.remove(self.letter_in_use) failed")
            
            new_chars = [char] * self.repetitions
            self.available_letters.extend(new_chars)

        try: 
            if char in self.letters_to_add:
                self.letters_to_add.remove(char)
        except ValueError:
            print("self.letters_to_add is empty and cannot remove the character.")

    
    def set_letter_in_use(self):
        
        
        if not self.available_letters:
            ###print("not self.available_letters")
            return ""
        
        # Avoid taking the same letter again when getting new random
        if self.letter_in_use:
            if not self.letters_to_add:
                if self.letter_in_use in self.available_letters:
                    self.available_letters.remove(self.letter_in_use)
            
            
        temp = self.available_letters.copy()
        temp = list(filter(lambda x: x != self.letter_in_use, temp))

        if not temp:
            return ""
        
        try:
            if self.start_string:
                self.letter_in_use = random.choice(temp)
            else:
                self.letter_in_use = temp.pop(0)
        except Exception as e:
            print("self.letter_in_use = temp.pop(0)", e)
            
        self.last_time_letter_set = time.time()
        
        return self.letter_in_use
        
        
    def _within_max_time(self):
        if time.time() < (self.last_time_letter_set + self.time_limit):
            return True
        
        return False
    
    
    def check_add_letter_counter(self):
        self.correct_counter += 1
        
        if not self._within_max_time():
            self.correct_counter = 0
        
        if self.correct_counter >= self.correct_counter_goal:
            self.correct_counter = 0
            self._add_letter_if_any_left_to_add()
            # chat gpt wants a return True here
            
        
    def _add_letter_if_any_left_to_add(self):
        
        ###print("letters_to_add:", self.letters_to_add)
        ###print("available_letters:", self.available_letters)
        
        if self.letters_to_add:
            
            added = False

            random.shuffle(self.letters_to_add)
            
            for c in self.letters_to_add:
                if c.lower() in "aioue":
                    self.add_to_available_letters(c)
                    added = True
                    break
                
            for c in self.letters_to_add:
                if c.lower() in "nrtsdfhjklcvbm":
                    self.add_to_available_letters(c)
                    added = True
                    break
            
            if not added:
                new_letter = random.choice(self.letters_to_add)
                self.add_to_available_letters(new_letter)
                
        else: 
            pass
            ###print("self.letters_to_add is empty")
        