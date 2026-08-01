import whois

def check_whois(domain):
    result = whois.whois(domain)

    creation_date = result.creation_date
    if isinstance(creation_date, list):
        creation_date = creation_date[0]

    expiration_date = result.expiration_date
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]

    return {
        "domain": result.domain_name,
        "registrar": result.registrar,
        "creation_date": str(creation_date),
        "expiration_date": str(expiration_date),
        "name_servers": result.name_servers,
        "country": result.country,
        "emails": result.emails
    }

if __name__ == "__main__":
    print(check_whois("google.com"))