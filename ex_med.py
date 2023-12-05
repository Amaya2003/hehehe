class MedicalDiagnosisExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "fever": {
                "symptoms": ["high body temperature", "headache", "fatigue"],
                "diagnosis": "Flu",
            },
            "cough": {
                "symptoms": ["persistent cough", "shortness of breath"],
                "diagnosis": "Respiratory infection",
            },
            "stomach_pain": {
                "symptoms": ["abdominal discomfort", "nausea", "vomiting"],
                "diagnosis": "Gastritis",
            },
            "back_pain": {
                "symptoms": ["lower back discomfort", "difficulty in movement"],
                "diagnosis": "Muscle strain",
            },
            "headache": {
                "symptoms": ["throbbing head pain", "sensitivity to light or sound"],
                "diagnosis": "Migraine",
            },
            "chest_pain": {
                "symptoms": ["sharp chest pain", "breathlessness"],
                "diagnosis": "Heart-related issues",
            },
            "fatigue": {
                "symptoms": ["extreme tiredness", "weakness"],
                "diagnosis": "Chronic fatigue syndrome",
            },
 
        }

    def get_diagnosis(self, symptoms):
        for condition, data in self.knowledge_base.items():
            if all(symptom in data["symptoms"] for symptom in symptoms):
                return data["diagnosis"]
        return "Unknown"


def main():
    expert_system = MedicalDiagnosisExpertSystem()
    print("Medical Diagnosis Expert System")
    print("Enter your symptoms (comma-separated) or type 'exit' to quit.")
    while True:
        user_input = input("Symptoms: ").strip().lower()
        if user_input == 'exit':
            break
        symptoms = [symptom.strip() for symptom in user_input.split(',')]
        diagnosis = expert_system.get_diagnosis(symptoms)
        print("Diagnosis:", diagnosis)


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