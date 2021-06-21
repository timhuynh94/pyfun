# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]


def numUniqueEmails(emails):
    uniqueEmails = []
    for email in emails:
        email = email[0:email.index('@')].replace('.', '') + email[email.index('@'):len(email)]
        if "+" in email:
            email = email[0:email.index('+')] + email[email.index('@'):len(email)]
        if email not in uniqueEmails:
            uniqueEmails.append(email)
    print(len(uniqueEmails))


numUniqueEmails(emails)
