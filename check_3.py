import whois

D_ZONE = "com"


# Read all domain names variants
with open("all_domains_3.txt", "r") as f:
    domains = f.read()
domains = domains.split("\n")

# find the last domain script was interrupted
with open("taken_domains_3.txt", "r") as f:
    tested_domains = f.read()
tested_domains = domains.split("\n")[-1]
tested_domain_idx = int(tested_domains.split(".")[0])

# domains = ["7baa.com", 'aabb.com', 'z7u.com']  # Test domains
domains.append("non-existing-domain")  # #  Append non_exiting domain for test

for x, domain in enumerate(domains[::-1]):
    try:
        if x <= tested_domain_idx:
            # # skip tested
            continue
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
        with open("found_domains_3.txt", "a") as f:
            # append controlling message for test
            f.write(f"[MONITOR] tested:{x} domains. The most resent: {domain_name}\n")    
    except Exception as e:
        error_first_line = str(e).split("\n")[0]
        result = f"[ERROR] ({x}) {error_first_line}"
        print(result)
        with open("found_domains_3.txt", "a") as f:
            f.write(f"{result}\n")    
