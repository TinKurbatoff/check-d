import whois

D_ZONE = "com"


with open("all_domains_3.txt", "r") as f:
    domains = f.read()
domains = domains.split("\n")
# domains = ["7baa.com", 'aabb.com', 'z7u.com']  # Test domains

for x, domain in enumerate(domains[::-1]):
    try:
        domain_name = f"{domain}.{D_ZONE}"
        # print(f"Sanity check: {domain}.{D_ZONE}")
        w = whois.whois(domain_name)
        #  w.expiration_date  # dates converted to datetime object
        if isinstance(w.expiration_date, list):
            result = f"{x}. {domain_name} Expiration: {w.expiration_date[0]:%Y-%m-%d %H:%M}"
        else:
            result = f"{x}. {domain_name} Expiration: {w.expiration_date:%Y-%m-%d %H:%M}"
        print(result)    
        with open("taken_domains_3.txt", "a") as f:
            f.write(f"{result}\n")    
    except Exception as e:
        error_first_line = str(e).split("\n")[0]
        result = f"[ERROR] ({x}) {error_first_line}"
        print(result)
        with open("found_domains_3.txt", "a") as f:
            f.write(f"{result}\n")    
