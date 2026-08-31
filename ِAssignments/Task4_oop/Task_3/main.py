from message_decoder import MessageDecoder
def test_decoder():
    """Test the message decoder with the given task."""
    print("STARTING MESSAGE DECODER TEST - TASK 3")
    print("=" * 60)
    
    # Given task
    task = '&&**$gnirtS PLIO!!@1234'
    
    # Create decoder object
    decoder = MessageDecoder(task)
    
    # Display step by step
    decoder.display_step_by_step()
    
    print("\n")
    
    # Display results
    decoder.display_results()
    
    print("\n" + "=" * 60)
    print("Test completed!")


def test_individual_methods():
    """Test individual methods separately."""
    print("\nINDIVIDUAL METHOD TESTING")
    print("=" * 60)
    
    task = '&&**$gnirtS PLIO!!@1234'
    decoder = MessageDecoder(task)
    
    # Test each method
    print(f"Original Task: {task}")
    print(f"Core Message: {decoder.extract_core_message()}")
    print(f"First Word Reversed: {decoder.reverse_first_word()}")
    print(f"Second Word with Vowels Replaced: {decoder.replace_shifted_vowels()}")
    print(f"Final Decoded Message: {decoder.decode_message()}")
    
    print("=" * 60)


def test_different_vowels():
    """Test with different vowel replacements."""
    print("\nTESTING DIFFERENT VOWEL REPLACEMENTS")
    print("=" * 60)
    
    # Test with different words containing vowels
    test_cases = [
        ('&&**$gnirtS PLIO!!@1234', 'String PLEU'),
        ('**#@Hello WIRLD!!99', 'Hello WERLD'),  # I->E
        ('##$World PLONE!!88', 'World PLUNE'),   # O->U
    ]
    
    for task, expected in test_cases:
        decoder = MessageDecoder(task)
        result = decoder.decode_message()
        print(f"Task: {task}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"✅ Passed: {result == expected}")
        print("-" * 40)


if __name__ == "__main__":
    """
    Run tests.
    """
    
    # Option 1: Run the main test
    test_decoder()
    
    # Option 2: Run individual methods test (uncomment below)
    # test_individual_methods()
    
    # Option 3: Test different vowel replacements (uncomment below)
    # test_different_vowels()