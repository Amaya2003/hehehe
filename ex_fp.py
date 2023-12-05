class FinancialPlanningExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "low_savings": {
                "criteria": lambda data: int(data.get("savings", 0)) < 50000,
                "recommendation": "Prioritize building an emergency fund before considering investments."
            },
            "low_income": {
                "criteria": lambda data: int(data.get("annual_income", 0)) < 500000,
                "recommendation": "Explore opportunities for increasing income or additional sources of revenue."
            },
            "high_income": {
                "criteria": lambda data: int(data.get("annual_income", 0)) >= 1000000,
                "recommendation": "You've achieved a commendable income and savings balance! Consider a customized investment strategy with professional advice for wealth management."
            },
            "high_savings": {
                "criteria": lambda data: int(data.get("savings", 0)) >= 500000,
                "recommendation": "Congratulations on building a substantial savings balance! Consider diversifying investments to maximize growth."
            },
            "low_debt": {
                "criteria": lambda data: int(data.get("total_debt", 0)) < 200000,
                "recommendation": "Continue managing debts responsibly and consider savings."
            },
            "moderate_debt": {
                "criteria": lambda data: 200000 <= int(data.get("total_debt", 0)) < 500000,
                "recommendation": "Focus on a balanced approach to debt repayment and savings."
            },
            "high_debt": {
                "criteria": lambda data: int(data.get("total_debt", 0)) >= 500000,
                "recommendation": "Prioritize paying off high-interest debts to reduce financial burden."
            },
            "low_retirement_savings": {
                "criteria": lambda data: int(data.get("retirement_savings", 0)) < 1000000,
                "recommendation": "Consider increasing contributions to retirement accounts."
            },
            "moderate_retirement_savings": {
                "criteria": lambda data: 1000000 <= int(data.get("retirement_savings", 0)) < 3000000,
                "recommendation": "Maintain contributions to retirement accounts and consider diversification."
            },
            "high_retirement_savings": {
                "criteria": lambda data: int(data.get("retirement_savings", 0)) >= 3000000,
                "recommendation": "Explore additional investment opportunities for retirement."
            },
            "moderate_income": {
                "criteria": lambda data: 500000 <= int(data.get("annual_income", 0)) < 1000000,
                "recommendation": "Maintain a balanced approach to savings and investments. Consider exploring diversified investment options for potential growth."
            },
            "moderate_savings": {
                "criteria": lambda data: 50000 <= int(data.get("savings", 0)) < 500000,
                "recommendation": "Prioritize building an emergency fund before considering investments."
            },
        }

    def get_recommendation(self, financial_data):
        recommendations = []
        for category, data in self.knowledge_base.items():
            met_criteria = data["criteria"](financial_data)
            if met_criteria:
                recommendations.append(data["recommendation"])
        return recommendations if recommendations else ["No specific recommendation at the moment."]

def main():
    expert_system = FinancialPlanningExpertSystem()
    print("Financial Planning Expert System")
    print("Enter your financial details to receive recommendations (e.g., annual_income, savings, total_debt, retirement_savings).")
    print("Enter 'exit' to quit.")
    while True:
        user_input = input("Financial Data: ").strip().lower()
        if user_input == 'exit':
            break
        financial_data = {k.strip(): v.strip() for k, v in (item.split('=') for item in user_input.split(','))}
        recommendations = expert_system.get_recommendation(financial_data)
        print("Recommendations:")
        for recommendation in recommendations:
            print("-", recommendation)

if __name__ == "__main__":
    main()











# Class Definition:

# class MedicalDiagnosisExpertSystem:: Defines the class MedicalDiagnosisExpertSystem, which encapsulates the expert system for medical diagnosis.
# Initialization Method (__init__):

# def __init__(self):: This method initializes the expert system.
# self.knowledge_base: This attribute stores the knowledge base as a dictionary containing medical conditions (keys) and their associated symptoms and diagnoses (values).
# Knowledge Base:

# The knowledge_base dictionary contains various medical conditions as keys, each associated with a nested dictionary.
# For each medical condition, there's a nested dictionary with:
# "symptoms" as a key: Lists specific symptoms associated with the medical condition.
# "diagnosis" as a key: Indicates the diagnosis or medical issue corresponding to those symptoms.
# Example Entries:

# Each entry in the knowledge_base dictionary represents a medical condition along with its associated symptoms and diagnosis.
# For instance:
# "fever" has symptoms such as "high body temperature," "headache," and "fatigue," and it's diagnosed as "Flu."
# "cough" has symptoms like "persistent cough" and "shortness of breath," diagnosed as "Respiratory infection."
# Similarly, other entries represent different medical conditions, their symptoms, and corresponding diagnoses.







# Method Signature:

# def get_diagnosis(self, symptoms):: Defines a method named get_diagnosis that takes symptoms as an argument along with self, referring to the instance of the class.
# Functionality:

# for condition, data in self.knowledge_base.items():: Iterates through each condition (medical issue) in the knowledge_base dictionary along with its associated data (symptoms and diagnosis).

# if all(symptom in data["symptoms"] for symptom in symptoms)::

# Checks if all the symptoms provided as input are present in the list of symptoms associated with the current medical condition.
# The all() function checks if every element in the iterable (in this case, symptoms) meets the condition specified (i.e., if it's in the list of symptoms for that condition).
# return data["diagnosis"]:

# If all the provided symptoms match those associated with a particular medical condition, the method returns the diagnosis corresponding to that condition.
# Handling Unknown Conditions:

# return "Unknown": If no condition matches the provided symptoms, or if the symptoms provided do not match any known conditions in the knowledge base, the method returns "Unknown".






# expert_system = MedicalDiagnosisExpertSystem(): Creates an instance of the MedicalDiagnosisExpertSystem class, initializing the medical diagnosis expert system.

# print("Medical Diagnosis Expert System") and print("Enter your symptoms (comma-separated) or type 'exit' to quit."): Display introductory messages to inform users about the system and how to input symptoms or exit.

# while True:: Starts an infinite loop to continuously interact with the user until the user decides to exit.

# user_input = input("Symptoms: ").strip().lower(): Prompts the user to input symptoms, which are then converted to lowercase and stripped of leading/trailing spaces.

# if user_input == 'exit': break: Checks if the user wants to exit. If the user inputs 'exit', the loop breaks, and the program ends.

# symptoms = [symptom.strip() for symptom in user_input.split(',')]: Splits the user input (which is a comma-separated string of symptoms) into a list of individual symptoms. Each symptom is stripped of any extra spaces.

# diagnosis = expert_system.get_diagnosis(symptoms): Uses the get_diagnosis() method from the MedicalDiagnosisExpertSystem class to obtain a diagnosis based on the provided symptoms.

# print("Diagnosis:", diagnosis): Prints the diagnosis obtained from the expert system based on the input symptoms.