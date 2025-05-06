import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

job_description = st.text_area("Enter Job Description", "")
if st.button('Get Recommendations'):
    if job_description:
        response = requests.post(
            'https://shl-backend-nw.onrender.com/recommend/',
            json={'query': job_description}  # <-- ensure 'query' not 'job_description'
        )

        if response.status_code == 200:
            recommendations = response.json()

            # Handle message if no relevant assessments found
            if isinstance(recommendations, dict) and 'message' in recommendations:
                st.warning(recommendations['message'])
            else:
                st.write("Top Recommended Assessments:")
                for rec in recommendations:
                    st.markdown(f"**{rec['Assessment Name']}**")
                    st.write(f"URL: {rec['URL']}")
                    st.write(f"Remote Testing: {rec['Remote Testing Support']}")
                    st.write(f"Adaptive/IRT: {rec['Adaptive/IRT Support']}")
                    st.write(f"Duration: {rec['Duration (minutes)']} minutes")
                    st.write(f"Test Type: {rec['Test Type']}")
                    # Optional: show score
                    if 'Score' in rec:
                        st.write(f"Match Score: {rec['Score']}")
                    st.write("---")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a job description.")
