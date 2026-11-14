import streamlit as st


st.set_page_config(
    page_title="STUDENT REGISTRATION FORM",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
.stFormSubmitButton button {
    background-color: #2563eb;
    color: white;
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

if "submitted" not in st.session_state:
    st.session_state.submitted=False

if "student_name" not in st.session_state:
    st.session_state.student_name=""

if st.session_state.submitted:
    st.title("REGISTRATION COMPLETE!")
    st.success(
        f"Thanks for filling the form {st.session_state.student_name}!"

    )
else:
    st.title("🎓STUDENT REGISTRATION FORM")

    st.write("please fill this form")



    with st.form("registration",clear_on_submit=True):
        name = st.text_input("Full Name")

        email = st.text_input("Email")

        age = st.number_input("Age",min_value=12,max_value=20,placeholder="Age",step=1,value=None)

        gender = st.selectbox("Gender",["Male","Female"],index=None,placeholder="Gender")

        level = st.radio("Level",["Skilled","Unskilled"],index=None)

        

        with st.container(border=True):

            col1,col2 = st.columns([1,10])


            with col1:
                with st.popover("+"):
                    certificate = st.file_uploader(
                        "Upload your certificate",
                        type=["pdf","jpg","jpeg","png"],
                        key="certificate"
                    )
            with col2:
                additional_info=st.text_area(
                    "Additional information",
                    placeholder="write your message....",
                    label_visibility="collapsed",
                    height=65
                )
        with st.container(border=True):

    
            submitted = st.form_submit_button("Submit",use_container_width=True)
        

        

        

    if submitted:

        if not name.strip() or not email.strip() or "@" not in email:
            st.error("Put in that damn name or email")
        elif age is None:
           st.error("Please enter your age.")
        elif gender is None:
           st.error("Please select your gender.")
        elif level is None:
           st.error("Please select your level.")
        elif not additional_info.strip():
           st.error("Please enter additional information.")

        elif certificate is None:
            st.error("Please upload your certificate.")
        
        
        else:
           st.session_state.student_name = name.strip()
           st.session_state.submitted = True
           st.rerun()
    
