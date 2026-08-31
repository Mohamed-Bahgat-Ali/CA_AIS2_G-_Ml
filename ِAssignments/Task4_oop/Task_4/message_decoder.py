"""
message_decoder.py
Module containing the MessageDecoder class for decoding encoded messages.
"""


class MessageDecoder:
    """
    MessageDecoder class handles decoding of encoded messages.
    
    This class provides functionality to:
        - Extract the core message from encoded string
        - Reverse the first word
        - Replace shifted vowels in the second word
    
    Attributes:
        task (str): The encoded message to be decoded.
    """
    
    def __init__(self, task: str):
        """
        Initialize the MessageDecoder with an encoded message.
        
        Args:
            task (str): The encoded message to decode.
        """
        self.task = task
        self.core_message = None
        self.first_word = None
        self.second_word = None
        self.decoded_message = None
    
    def extract_core_message(self) -> str:
        """
        Extract the core part of the message using slicing.
        
        Returns:
            str: The core message without symbols and numbers.
        """
        # Extract from position 6 to 24 (yalpstcejorp EPUVT)
        self.core_message = self.task[6:24:1]
        return self.core_message
    
    def reverse_first_word(self) -> str:
        """
        Reverse the first word of the core message.
        
        Returns:
            str: The reversed first word.
        """
        if self.core_message is None:
            self.extract_core_message()
        
        # Extract first word (yalpstcejorp) using slicing
        self.first_word = self.core_message[:13]
        # Reverse it using [::-1]
        reversed_word = self.first_word[::-1]
        return reversed_word
    
    def replace_shifted_vowels(self) -> str:
        """
        Replace shifted vowels in the second word.
        
        Rules:
            - E -> A
            - U -> O
        
        Returns:
            str: The second word with vowels replaced.
        """
        if self.core_message is None:
            self.extract_core_message()
        
        # Extract second word (EPUVT)
        self.second_word = self.core_message[14:19]
        
        # Replace vowels: E->A, U->O
        replaced_word = self.second_word.replace('E', 'A').replace('U', 'O')
        return replaced_word
    
    def decode_message(self) -> str:
        """
        Decode the complete message.
        
        Steps:
            1. Extract core message
            2. Reverse first word (yalpstcejorp -> projectplay)
            3. Replace vowels in second word (EPUVT -> APOVT)
            4. Combine both words
        
        Returns:
            str: The decoded message.
        """
        # Step 1: Extract core message
        core = self.extract_core_message()
        print(f"Step 1 - Core Message: {core}")
        
        # Step 2: Reverse first word (yalpstcejorp -> projectplay)
        first_reversed = self.reverse_first_word()
        print(f"Step 2 - First word reversed: {first_reversed}")
        
        # Step 3: Replace vowels in second word (EPUVT -> APOVT)
        second_replaced = self.replace_shifted_vowels()
        print(f"Step 3 - Second word with vowels replaced: {second_replaced}")
        
        # Step 4: Combine both words
        self.decoded_message = f"{first_reversed} {second_replaced}"
        
        return self.decoded_message
    
    def display_results(self) -> None:
        """
        Display the decoding process step by step.
        """
        print("=" * 50)
        print("MESSAGE DECODER RESULTS")
        print("=" * 50)
        print(f"Original Task: {self.task}")
        print("-" * 50)
        
        # Show each step
        result = self.decode_message()
        
        print("-" * 50)
        print(f" Final Decoded Message: {result}")
        print("=" * 50)
    
    def display_step_by_step(self) -> None:
        """
        Display decoding step by step as in your solution style.
        """
        print("=" * 60)
        
        print("=" * 60)
        
        task = self.task
        
        # Step 1: Extract core using slicing
        print(f"Original: {task}")
        core = task[6:24:1]
        print(f"Step 1: task[6:24:1] -> {core}")
        print(f"Expected: yalpstcejorp EPUVT")
        print()
        
        # Step 2: Extract first and second word
        x = task[6:19:1]   # yalpstcejorp
        y = task[20:25:1]  # EPUVT
        print(f"Step 2: x = task[6:19:1] -> {x}")
        print(f"        y = task[20:25:1] -> {y}")
        print(f"        print(x[::-1], y) -> {x[::-1]} {y}")
        print(f"Expected: projectplay EPUVT")
        print()
        
        # Step 3: Replace vowels in second word
        y_replaced = y.replace('E', 'A').replace('U', 'O')
        print(f"Step 3: Replace vowels in '{y}'")
        print(f"        E -> A, U -> O")
        print(f"        {y} -> {y_replaced}")
        print(f"Expected: APOVT")
        print()
        
        # Step 4: Final result
        final = f"{x[::-1]} {y_replaced}"
        print(f"Step 4: Combine: {x[::-1]} + {y_replaced}")
        print(f"Final Decoded Message: {final}")
        print(f"Expected: projectplay APOVT")
        print("=" * 60)



if __name__ == "__main__":
    """
    Test the MessageDecoder class.
    """
    
    print("TESTING MESSAGE DECODER - TASK 4")
    print("=" * 60)
    
    # Test with the given task
    task = '#$$$@!yalpstcejorp EPUVT****9887'
    decoder = MessageDecoder(task)
    
    # Show step by step
    decoder.display_step_by_step()
    
    print("\n")
    
    # Show detailed results
    decoder.display_results()
    
    print("\n" + "=" * 60)
    print("Test completed!")