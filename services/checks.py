import re

class Checks:
    """
    Class to check different fields
    """
    
    def isValidEmail(self, email):
        """
        Check if email is valid

        Parameters
        ----------
        email : str
            User email

        Returns
        -------
        bool
            True if email is valid, False otherwise
        """
        # Regular expression for validating an Email
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Check if email is valid
        return bool(re.fullmatch(email_regex, email))
    

    def isValidLayer(self, href, list_href_regex):
        """
        Check if href layer is valid

        Parameters
        ----------
        layer : str
            Href layer
        layer_regex : str
            Href layer regex

        Returns
        -------
        bool
            True if href layer is valid, False otherwise
        """
        # Check if href matches any of the patterns
        for href_regex in list_href_regex:
            # Compile regex pattern for href
            pattern = re.compile(rf".*{href_regex}.*")
            # Check if href matches pattern
            if bool(re.fullmatch(pattern, href)):
                return True
        
        # If href does not match any of the patterns
        return False