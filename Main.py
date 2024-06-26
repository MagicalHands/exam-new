
from tensorflow import keras
from Feature_Extractor import extract_features
import streamlit as st 
from API import get_prediction

# path to trained model
#model_path = r"/workspace/exam-new/models/Malicious_URL_Prediction.h5"
model_path = r"models/Malicious_URL_Prediction.h5"

# input url 123
#url = "www.tesla.com/"

def main():
    
    st.title("CyberKavach")
    page_bg_img = """
    <style>
    .stApp {
        background-image: url("https://www.graphus.ai/wp-content/uploads/2022/12/Cyber-Security-Ransomware-Email-Phishing-Encrypted-Technology-Digital-Information-Protected-Secured-3-copy.jpg");

        background-size: cover;
        }
        </style>
        """
        
    st.markdown(page_bg_img, unsafe_allow_html=True)


    html_temp = """
    <div style="background-color:#36517e ;padding:10px">
    <h2 style="color:black;text-align:center;">Phishing URL Detector </h2>
    </div>
    """

    #st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown(f"""<h1 style="color:white;font-size:30px;">Enter Suspicious URL</h1>
    """, unsafe_allow_html=True)
    

    url = st.text_input(" ", "Type Here")
    st.markdown(
    """
    <style>
    textarea {
        font-size: 1rem !important;
    }
    input {
        font-size: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    
    safe_html="""  
      <div style="background-color:#00ff95;padding:30px >
       <h1 style="color:black;text-align:center;"> Your url is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:rgb(0, 0, 0) ;text-align:center;"> Your url is unsafe</h2>
       </div>
    """

    if st.button("Predict"):
        output=get_prediction(url,model_path)
        # st.success('The probability of url being malicious is {}'.format(output))
        
    

        if output > 17:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()
