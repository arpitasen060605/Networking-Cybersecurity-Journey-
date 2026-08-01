import dns.resolver

def check_dns(domain):
    records = {
        "A": [],
        "MX": [],
        "NS": [],
        "TXT": []
    }

    for record_type in records.keys():
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for answer in answers:
                records[record_type].append(str(answer))
        except Exception as e:
            records[record_type] = [f"No {record_type} record found"]

    return {
        "domain": domain,
        "a_records": records["A"],
        "mx_records": records["MX"],
        "ns_records": records["NS"],
        "txt_records": records["TXT"]
    }

if __name__ == "__main__":
    print(check_dns("google.com"))