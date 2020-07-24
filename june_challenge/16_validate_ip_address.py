class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validate_IPv4_regex(chunks):
            return re.match(r'(' + IPv4_chunk_pattern + ')', chunk)
    
        # validating single IPv6 chunk using Regular Expression
        def validate_IPv6_regex(chunk):
            return re.match(r'(' + IPv6_chunk_pattern + ')', chunk)
        
        IPv4_chunk_pattern = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
        IPv6_chunk_pattern = "^([0-9a-fA-F]{1,4})$"

        if IP.count('.') == 3:
            for chunk in IP.split("."):
                if not validate_IPv4_regex(chunk):
                    return "Neither"
            return "IPv4"
        elif IP.count(':') == 7:
            for chunk in IP.split(":"):
                if not validate_IPv6_regex(chunk):
                    return "Neither"
            return "IPv6"

        return "Neither"
