"""
main.py
Main file for testing the MessageDecoder class.
"""

from massage_encoder import MessageDecoder


def test_decoder():
    """Test the message decoder with the given task."""
    print("STARTING MESSAGE DECODER TEST")
    print("=" * 60)
    
    # Given task
    task = '####@mocleW EPGTQ!!!6789'
    
    # Create decoder object
    decoder = MessageDecoder(task)
    
    # Display results
    decoder.display_results()
    
    print("\n" + "=" * 60)
    print("Test completed!")


def test_step_by_step():
    """Test step by step as in your solution."""
    print("\nSTEP BY STEP TEST (Your Solution Style)")
    print("=" * 60)
    
    task = '####@mocleW EPGTQ!!!6789'
    
    # Step 1: Extract core message
    print(f"Original: {task}")
    core = task[6:18:1]
    print(f"Step 1: task[6:18:1] -> {core}")
    print(f"Expected: mocleW EPGTQ")
    
    # Step 2: Extract first and second word
    x = task[6:12:1]
    y = task[13:18:1]
    print(f"Step 2: x = task[6:12:1] -> {x}")
    print(f"        y = task[13:18:1] -> {y}")
    print(f"        print(x[::-1], y) -> {x[::-1]} {y}")
    print(f"Expected: Welcome EPGTQ")
    
    # Step 3: Alternative slicing for second word
    x = task[6:12:1]
    y = task[14:18:1]
    print(f"Step 3: x = task[6:12:1] -> {x}")
    print(f"        y = task[14:18:1] -> {y}")
    print(f"        print(x[::-1], y) -> {x[::-1]} {y}")
    print(f"Expected: Welcome PGTO")
    
    # Step 4: Final result
    decoder = MessageDecoder(task)
    final = decoder.decode_message()
    print(f"Step 4: Final Message -> {final}")
    print(f"Expected: Welcome PGTO")
    
    print("=" * 60)


if __name__ == "__main__":
    """
    Run tests.
    """
    
    # Option 1: Run the main test
    test_decoder()
    
    # Option 2: Run step by step test (uncomment below)
    # test_step_by_step()