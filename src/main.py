from initialization_with_logger import *
import streamlit as st

# Streamlit app setup
st.title("AI Mock Interviewer 💼")

# Sidebar inputs
st.sidebar.text_input("Enter Job Role", placeholder="e.g., Data Scientist", key="job_role")
st.sidebar.text_area("Enter Job Description", placeholder="Provide job description here...", height=150, key="job_description")
resume_pdf = st.sidebar.file_uploader("Upload Resume (PDF only)", type=["pdf"], key="resume_pdf")

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []
    logger.debug("Session state 'conversation_history' initialized.")


if "response_input" not in st.session_state:
    st.session_state["response_input"] = ""
    logger.debug("Session state 'response_input' initialized.")

if "current_question" not in st.session_state:
    st.session_state["current_question"] = ""
    logger.debug("Session state 'current_question' initialized.")

if "interview_start" not in st.session_state:
    st.session_state["interview_start"] = False
    logger.debug("Session state 'interview_start' initialized.")

if "details_submitted" not in st.session_state:
    st.session_state["details_submitted"] = False
    logger.debug("Session state 'details_submitted' initialized.")


if "response_received" not in st.session_state:
    st.session_state["response_received"] = False
    logger.debug("Session state 'response_received' initialized.")

if "question_asked" not in st.session_state:
    st.session_state["question_asked"] = False
    logger.debug("Session state 'question_asked' initialized.")

if "interview_concluded" not in st.session_state:
    st.session_state["interview_concluded"] = False
    logger.debug("Session state 'interview_concluded' initialized.")

if not st.session_state["interview_start"]:

    if st.sidebar.button("Submit Details") or st.session_state["details_submitted"] :

        if st.session_state.get("resume_pdf"):
            resume_text = extract_text_from_pdf(st.session_state["resume_pdf"])
            st.session_state["resume_text"] = resume_text

        if all(key in st.session_state for key in ["job_role", "job_description", "resume_text"]):
            st.session_state["details_submitted"] = True
            st.session_state["resume_summary"] = summarize_resume(st.session_state["resume_text"])
            st.session_state["resume_feedback"] = resume_feedback(st.session_state['resume_summary'],
                                                                  st.session_state['job_role'],
                                                                  st.session_state["job_description"])
            display_submitted_details()
        else:
            st.session_state["details_submitted"] = False
            st.sidebar.error("Please provide Job Role, Job Description, and Resume first.")


    if st.session_state["details_submitted"] and not st.session_state["interview_start"]:
        # Start interview, first question
        if st.button("Start Interview"):
            st.session_state["interview_start"] = True
            get_first_question() #takes question in st.session_state["current_question"]
            st.rerun()

if st.session_state["interview_start"] and not st.session_state["interview_concluded"]:
    display_submitted_details()
    st.subheader("Question")
    ask_question(st.session_state["current_question"])

    if  st.session_state["question_asked"] and not st.session_state["response_received"]:
        get_user_response()

        if st.button("Submit Response"):
            if not st.session_state["response_input"]:
                st.error("Please enter a response.")
            else:
                st.session_state["response_feedback"] = get_response_feedback(st.session_state["response_input"])
                st.subheader("Feedback")
                play_text_as_audio(st.session_state["response_feedback"])
                st.write(st.session_state["response_feedback"])
                st.session_state["response_received"] = True
                update_conversation_history_st("AI - Question", st.session_state["current_question"])
                update_conversation_history_st("Candidate - Response", st.session_state["response_input"])
                update_conversation_history_st("Feedback", st.session_state["response_feedback"])

    if st.session_state["question_asked"] and st.session_state["response_received"]:
        if st.button("Next Question"):
            get_next_question()
            st.session_state["question_asked"] = False
            st.session_state["response_received"] = False
            st.rerun()
    # Display conversation history
    with st.expander("Conversation History"):
        if "conversation_history" in st.session_state:
            for turn in st.session_state["conversation_history"]:
                for speaker, message in turn.items():
                    st.write(f"**{speaker}:** {message}")


    if st.button("End Interview"):
        conclude_interview()
        st.rerun()

if st.session_state["interview_concluded"]:
    st.header("Good Luck for Your Actual Interview")
    download_conversation_history()



