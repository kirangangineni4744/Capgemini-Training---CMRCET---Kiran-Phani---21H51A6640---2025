def check_loan_eligibility(salary, age, credit_score):
    if age < 18:
        return "Rejected: Applicant must be at least 18 years old."
    if age > 60:
        return "Rejected: Applicant must be under 60 years old."
    if salary < 25000:
        return "Rejected: Minimum salary requirement is ₹20,000."
    if credit_score < 650:
        return "Rejected: Credit score must be at least 650."
    return "Approved: Loan eligibility criteria met."

salary = float(input("Enter your monthly salary: ₹"))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))

result = check_loan_eligibility(salary, age, credit_score)
print(result)
