"""
email_processor.py
Module containing the EmailProcessor class for email validation and processing.
"""


class EmailProcessor:
    """
    EmailProcessor class handles validation and processing of email addresses.
    
    This class provides functionality to:
        - Validate email format
        - Extract username and domain
        - Determine domain type (.com, .edu, or other)
    
    Attributes:
        email (str): The email address to be processed.
    """
    
    def __init__(self, email: str):
        """
        Initialize the EmailProcessor with an email address.
        
        Args:
            email (str): The email address to process.
        """
        self.email = email
        self.username = None
        self.domain = None
    
    def validate_email(self) -> bool:
        """
        Validate the email format.
        
        Rules:
            - Must contain exactly one "@" symbol
            - Must contain at least one "." after the "@" symbol
        
        Returns:
            bool: True if email is valid, False otherwise.
        """
        # Check for exactly one @ symbol
        at_count = self.email.count('@')
        if at_count != 1:
            return False
        
        # Check for at least one dot after @
        at_index = self.email.index('@')
        if '.' not in self.email[at_index:]:
            return False
        
        return True
    
    def extract_username(self) -> str:
        """
        Extract the username (part before '@').
        
        Returns:
            str: The username portion of the email.
        """
        if self.username is None:
            self.username = self.email.split('@')[0]
        return self.username
    
    def extract_domain(self) -> str:
        """
        Extract the domain (part between '@' and last '.').
        
        Returns:
            str: The domain portion of the email.
        """
        if self.domain is None:
            at_index = self.email.index('@')
            last_dot_index = self.email.rindex('.')
            self.domain = self.email[at_index + 1:last_dot_index]
        return self.domain
    
    def check_domain_ending(self) -> str:
        """
        Determine the type of domain based on its ending.
        
        Returns:
            str: 'Commercial Domain' if ends with .com,
                 'Educational Domain' if ends with .edu,
                 'Other Domain' otherwise.
        """
        if self.email.endswith('.com'):
            return "Commercial Domain"
        elif self.email.endswith('.edu'):
            return "Educational Domain"
        else:
            return "Other Domain"
    
    def process_email(self) -> dict:
        """
        Process the complete email: validate, extract, and classify.
        
        Returns:
            dict: Dictionary containing:
                - validation: bool or str
                - username: str
                - domain: str
                - domain_type: str
        """
        result = {
            'validation': None,
            'username': None,
            'domain': None,
            'domain_type': None
        }
        
        # Step 1: Validate email
        if not self.validate_email():
            result['validation'] = "Invalid email"
            return result
        else:
            result['validation'] = True
        
        # Step 2: Extract username
        result['username'] = self.extract_username()
        
        # Step 3: Extract domain
        result['domain'] = self.extract_domain()
        
        # Step 4: Check domain type
        result['domain_type'] = self.check_domain_ending()
        
        return result
    
    def display_results(self) -> None:
        """
        Display the email processing results in a readable format.
        """
        result = self.process_email()
        
        print("=" * 50)
        print("EMAIL PROCESSING RESULTS")
        print("=" * 50)
        print(f"Input Email: {self.email}")
        print("-" * 50)
        
        if result['validation'] == "Invalid email":
            print("Status: Invalid email format!")
            print("Hint: Email must contain exactly one '@' and at least one '.' after '@'")
        else:
            print("Status: Valid email")
            print(f"Username: {result['username']}")
            print(f"Domain: {result['domain']}")
            print(f"Domain Type: {result['domain_type']}")
        
        print("=" * 50)