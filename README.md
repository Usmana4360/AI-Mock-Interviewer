# AI Mock Interviewer Project

## Overview
The AI Mock Interviewer is a Streamlit-based application designed to help individuals prepare for job interviews in the field of data science. It combines state-of-the-art AI techniques to simulate an interview environment, generate professional questions, provide feedback on responses, and offer an interactive learning experience.

## Features
- **Interview Simulation**: Generate dynamic, role-specific questions based on user-provided job descriptions and resumes.
- **Feedback Mechanism**: AI-powered feedback on candidate responses for constructive improvement.
- **Resume Analysis**: Extract text from uploaded PDF resumes and summarize key content.
- **Audio Integration**: Convert interview questions and feedback into audio for a realistic interview experience.
- **Conversation History**: Downloadable JSON of the interview session for review.
- **Evaluation Metrics**: BLEU and ROUGE scores for interview response analysis.

---

## Project Structure


Conversation History: Downloadable JSON of the interview session for review.

Evaluation Metrics: BLEU and ROUGE scores for interview response analysis.


---

## Installation

### Prerequisites
- Python 3.8 or higher
- Streamlit
- Required Python libraries: `nltk`, `rouge`, `gTTS`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-mock-interviewer.git
   cd ai-mock-interviewer


   pip install -r requirements.txt

   streamlit run main.py

## How to Use
**Step 1:** Provide Details
Enter the Job Role and Job Description in the sidebar.
Upload your resume in PDF format.
**Step 2:** Start the Interview
Click Submit Details to initialize the session.
Press Start Interview to begin receiving AI-generated questions.
**Step 3:** Respond and Receive Feedback
Provide your response to the displayed question.
Get AI Feedback on your response.
Continue to the next question or end the interview.
**Step 4:** Download Results
View and download your interview session's history from the application.


## Technologies Used
**Frontend:** Streamlit
**Backend:** OpenAI GPT
**Audio Processing:** gTTS (Google Text-to-Speech)
**Data Visualization:** JSON download functionality

## Acknowledgments
Special thanks to my group members for their collaboration and to our mentors for their guidance and support throughout this project. This project is a testament to the power of teamwork and innovative thinking.

## Contact
Feel free to reach out or contribute to this project!

**Connect with me:**
- [LinkedIn](www.linkedin.com/in/muhammad-usmanhni/) - Muhammad Usman



