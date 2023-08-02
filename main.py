import streamlit as st
import base64


def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Devendra Parihars's Portfolio",
        #data symbol
        page_icon="📊",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/dev.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Resume-Devendra_Parihar.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Devendra Parihar👋</div>""", unsafe_allow_html=True)

    # # Profile image
    # st.write(f"""
    # <div class="container">
    #     <div class="box">
    #         <div class="spin-container">
    #             <div class="shape">
    #                 <div class="bd">
    #                     <img src="{img}" alt="Devendra Parihar">
    #                 </div>
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # """, 
    # unsafe_allow_html=True)

    # Alternative image (static and rounded) 
    st.write(f"""
    <div style="display: flex; justify-content: center;">
       <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Data Scientist and Machine Learning </div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/dev523", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/devendra-parihar", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/devparihar5", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Twitter": ["https://twitter.com/Devendr74154261", "https://cdn-icons-png.flaticon.com/512/733/733579.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 **Data Scientist** @ [Kainskep](https://www.kainskep.com/) 
             
    - 🎓 **B.Tech** in Artificial Intelligence and Data Science from [Govt. Engineering College Bikaner](https://www.ecb.ac.in/) (2020-2024)

    - 🛩️ prev: AI/ML Developer Intern in 2-3 startups

    - ❤️ I am passionate about **Data Science, Machine Learning/Deep Learning, Computer Vision, Optimization**, and more!
    
    - 🤖 I enojoy developing projects such as [Check on github](https://github.com/devparihar5) and participating at platforms like [Kaggle](https://www.kaggle.com/dev523) 📈

    - 📫 How to reach me: devendraparihar340@kainskep.com
    
    - 🏠 Jodhpur, Rajasthan, India
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Devndra's_cv.pdf",
        mime="application/pdf",
    )

    st.write("##")

if __name__ == "__main__":
    home()