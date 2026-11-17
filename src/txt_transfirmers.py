from utils import to_mxn, clean_string

#Nesting - lsita de diccionarios
raw = [
    {"name": "           aNa      ", "active": True, "cash": "120.50"},
    {"name": "         LuIS           ", "active": False, "cash": "0"},
    {"name": "           MAra        ", "active": True, "cash": "99.99"},
]


def clean(row: dict) -> dict:
    """
    This function returns a formatted
    dicctionary
    """
    return{
        "name": clean_string(row["name"]),
        "active": bool(row["active"]),
        "cash_mxn": to_mxn(row["cash"], 20.0)
    }

#List comprenhension
clean_data = [clean(r) for r in raw if r["active"]]

print("\n\nlista original: \n", raw)
print("\n\nlista formateada: \n", clean_data)