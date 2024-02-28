import random

# Dictionary of questions and their corresponding answers
college_qa = {
    "What are the admission requirements?": ["Admission requirements vary by college and program. You can find specific requirements on the college's website or by contacting the admissions office.",
                                             "Admission requirements can differ based on the program you're interested in. It's best to check the college's website or contact the admissions office for detailed information."],
    "What programs does the college offer?": ["The college offers a wide range of programs including computer science, engineering, business, psychology, and many more. You can find a full list of programs on the college's website.",
                                              "There are plenty of programs to choose from, including computer science, engineering, business, psychology, and more. You can explore the complete list on the college's website."],
    "How much does tuition cost?": ["Tuition costs vary depending on factors such as residency status and program of study. You can find detailed information about tuition and fees on the college's website.",
                                    "The cost of tuition can vary based on your residency status and the program you're interested in. I recommend checking the college's website for the most accurate information."],
    "Are there any scholarships available?": ["Yes, the college offers scholarships to eligible students. You can find information about scholarship opportunities and how to apply on the college's website.",
                                              "There are indeed scholarships available for eligible students. You can explore the various scholarship opportunities and application processes on the college's website."],
    "What is the campus like?": ["The campus is known for its beautiful grounds and modern facilities. There are also plenty of amenities for students including dining options, recreational facilities, and student organizations.",
                                  "You'll find that the campus boasts beautiful grounds and modern facilities. There's a vibrant atmosphere with numerous amenities available to students, including dining options, recreational facilities, and various student organizations."],
    "How can I schedule a campus tour?": ["You can schedule a campus tour by contacting the admissions office or by visiting the college's website. Campus tours are a great way to get a feel for the campus and learn more about what the college has to offer.",
                                          "To schedule a campus tour, you can reach out to the admissions office directly or visit the college's website for more information. Campus tours provide a firsthand experience of the campus atmosphere and facilities."],
    "Is there on-campus housing available?": ["Yes, the college offers on-campus housing options for students. You can find information about housing options and how to apply on the college's website.",
                                               "Certainly! There are on-campus housing options available for students. You can explore the different housing options and application procedures on the college's website."],
    "What is the student-to-faculty ratio?": ["The student-to-faculty ratio varies depending on the size of the college and the specific program of study. Generally, the college strives to maintain small class sizes to ensure personalized attention for students.",
                                                "The student-to-faculty ratio can vary based on the college's size and the program you're interested in. However, the college prioritizes maintaining small class sizes to facilitate personalized interactions between students and faculty."],
    "How can I apply for financial aid?": ["To apply for financial aid, you will need to complete the Free Application for Federal Student Aid (FAFSA). You can find more information about the financial aid application process on the college's website or by contacting the financial aid office.",
                                             "Applying for financial aid involves completing the Free Application for Federal Student Aid (FAFSA). Detailed information about the financial aid application process is available on the college's website and through the financial aid office."],
    "Can I study abroad?": ["Yes, the college offers study abroad programs for students who are interested in gaining international experience. You can find more information about study abroad opportunities on the college's website.",
                              "Absolutely! The college provides opportunities for students to study abroad and gain valuable international experience. Explore the various study abroad programs and opportunities on the college's website."],
}

# Function to handle user queries
def answer_question(question):
    if question in college_qa:
        return random.choice(college_qa[question])
    else:
        return "I'm sorry, I don't have an answer to that question. Please ask another question about college."

# Main function to interact with the user
def main():
    print("Welcome to the College Q&A Chatbot!")
    print("Ask me anything about college.")

    while True:
        user_input = input("You: ").strip().capitalize()
        
        if user_input == "Exit":
            print("Exiting the chatbot. Goodbye!")
            break
        else:
            response = answer_question(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    main()
