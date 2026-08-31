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
        # Using slicing as in your solution: task[6:18:1]
        self.core_message = self.task[6:18:1]
        return self.core_message
    
    def reverse_first_word(self) -> str:
        """
        Reverse the first word of the core message.
        
        Returns:
            str: The reversed first word.
        """
        if self.core_message is None:
            self.extract_core_message()
        
        # Extract first word using slicing: task[6:12:1]
        self.first_word = self.core_message[:6]
        # Reverse it using [::-1]
        reversed_word = self.first_word[::-1]
        return reversed_word
    
    def replace_shifted_vowels(self) -> str:
        """
        Replace shifted vowels in the second word.
        
        Returns:
            str: The second word with vowels replaced.
        """
        if self.core_message is None:
            self.extract_core_message()
        
        # Extract second word using slicing: task[13:18:1]
        # or task[14:18:1] depending on position
        self.second_word = self.core_message[6:11]
        return self.second_word
    
    def decode_message(self) -> str:
        """
        Decode the complete message.
        
        Steps:
            1. Extract core message
            2. Reverse first word
            3. Keep second word as is (no vowels to change)
            4. Combine both words
        
        Returns:
            str: The decoded message.
        """
        # Step 1: Extract core message
        core = self.extract_core_message()
        print(core)  # Output: mocleW EPGTQ
        
        # Step 2: Reverse first word (mocleW -> Welcome)
        first_reversed = self.reverse_first_word()
        
        # Step 3: Extract second word (EPGTQ)
        second = self.replace_shifted_vowels()
        
        # Step 4: Combine both words
        self.decoded_message = f"{first_reversed} {second}"
        
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
        
        # Step 1: Extract core
        core = self.extract_core_message()
        print(f"Step 1 - Core Message: {core}")
        
        # Step 2: Show first word extraction
        first = self.task[6:12:1]
        print(f"Step 2 - First word (slicing): {first}")
        print(f"Step 3 - First word reversed: {first[::-1]}")
        
        # Step 3: Show second word extraction
        second = self.task[13:18:1]
        print(f"Step 4 - Second word (slicing): {second}")
        
        # Step 4: Final result
        final = self.decode_message()
        print("-" * 50)
        print(f" Final Decoded Message: {final}")
        print("=" * 50)
if __name__ == "__main__":
    """
    Test the MessageDecoder class.
    """
    
    print("TESTING MESSAGE DECODER")
    print("=" * 60)
    
    # Test with the given task
    task = '####@mocleW EPGTQ!!!6789'
    decoder = MessageDecoder(task)
    decoder.display_results()
    
    print("\n" + "=" * 60)
    print("Test completed!")