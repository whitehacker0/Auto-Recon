import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_phone(phone_number): 
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, "en")
        provider = carrier.name_for_number(parsed_number, "en")
        
        return {
            "Phone Number": phone_number,
            "Country": country if country else "Unknown",
            "Carrier": provider if provider else "Unknown"
        }
    except phonenumbers.NumberParseException:
        return {"Error": "Invalid phone number format."}

if __name__ == "__main__":
    phone_number = input("Enter phone number (with country code): ").strip()
    result = lookup_phone(phone_number)
    print("\n🔍 Phone Lookup Results:")
    for key, value in result.items():
        print(f"{key}: {value}")
