"""
main.py
Main file for testing the EmailProcessor class.
"""

from email_check import EmailProcessor


def test_valid_email():
    """Test with a valid email."""
    print("\nTEST CASE 1: Valid Email")
    print("-" * 50)
    processor = EmailProcessor("Amit_ml@gmail.edu")
    processor.display_results()


def test_invalid_email_no_at():
    """Test with invalid email (no @ symbol)."""
    print("\n\nTEST CASE 2: Invalid Email (No @)")
    print("-" * 50)
    processor = EmailProcessor("Amit_mlgmail.edu")
    processor.display_results()


def test_invalid_email_multiple_at():
    """Test with invalid email (multiple @ symbols)."""
    print("\n\nTEST CASE 3: Invalid Email (Multiple @)")
    print("-" * 50)
    processor = EmailProcessor("Amit@ml@gmail.edu")
    processor.display_results()


def test_invalid_email_no_dot():
    """Test with invalid email (no dot after @)."""
    print("\n\nTEST CASE 4: Invalid Email (No dot after @)")
    print("-" * 50)
    processor = EmailProcessor("Amit_ml@gmailedu")
    processor.display_results()


def test_commercial_domain():
    """Test with .com commercial domain."""
    print("\n\nTEST CASE 5: Commercial Domain (.com)")
    print("-" * 50)
    processor = EmailProcessor("user@company.com")
    processor.display_results()


def test_other_domain():
    """Test with .org domain (Other Domain)."""
    print("\n\nTEST CASE 6: Other Domain (.org)")
    print("-" * 50)
    processor = EmailProcessor("user@organization.org")
    processor.display_results()


def test_individual_methods():
    """Test individual methods separately."""
    print("\n\nTEST CASE 7: Individual Method Testing")
    print("-" * 50)
    processor = EmailProcessor("test.user@university.edu")
    
    print(f"Email: {processor.email}")
    print(f"Valid: {processor.validate_email()}")
    print(f"Username: {processor.extract_username()}")
    print(f"Domain: {processor.extract_domain()}")
    print(f"Domain Type: {processor.check_domain_ending()}")


def test_user_input():
    """Test with user input."""
    print("\n\nTEST CASE 8: User Input")
    print("-" * 50)
    
    # Get email from user
    user_email = input("Enter an email address to test: ")
    
    # Process the email
    processor = EmailProcessor(user_email)
    processor.display_results()


def run_all_tests():
    """Run all test cases."""
    print("STARTING ALL TESTS")
    print("=" * 60)
    
    test_valid_email()
    test_invalid_email_no_at()
    test_invalid_email_multiple_at()
    test_invalid_email_no_dot()
    test_commercial_domain()
    test_other_domain()
    test_individual_methods()
    
    print("\n" + "=" * 60)
    print("All tests completed!")


if __name__ == "__main__":
    """
    When running this file directly, execute the tests.
    """
    
    # Option 1: Run all automatic tests
    run_all_tests()
    
    # Option 2: Run test with user input (uncomment the line below)
    # test_user_input()
    
    # Option 3: Run a specific test (uncomment the line you want)
    # test_valid_email()
    # test_commercial_domain()