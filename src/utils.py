"""
    Utilidades de limpieza y conversion
"""

def to_mxn(value, rate = 18.58):
    """
        This function converts value (USD)
        to MXN via tasa
    """
    return float(value)*float(rate)

def clean_string(name: str) -> str:
    """
        This function cleans name
    """
    return " ".join(name.strip().title().split())