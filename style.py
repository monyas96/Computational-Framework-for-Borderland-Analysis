import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        /* GLOBAL FONT AND BACKGROUND */
        html, body, [class*="css"]  {
            font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
            background-color: #f8f9fa;
            color: #22223b;
        }

        /* MAIN TITLE */
        .stTitle {
            font-size: 2.8rem !important;
            font-weight: 900 !important;
            color: #1D3557 !important;
            letter-spacing: -1px;
            margin-bottom: 0.5rem;
        }

        /* HEADERS */
        h1, h2, h3, h4, .stHeader, .stSubheader {
            color: #1D3557 !important;
            font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
        }
        h1 { font-size: 2.2rem !important; }
        h2 { font-size: 1.6rem !important; }
        h3 { font-size: 1.2rem !important; }
        h4 { font-size: 1.1rem !important; }

        /* SIDEBAR */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa !important;
            border-right: 1px solid #e3effa;
            padding: 1.5rem 1rem 1.5rem 1.5rem;
        }
        .st-emotion-cache-1v0mbdj > div > div {
            padding: 10px 18px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-weight: 500;
            font-size: 17px;
            color: #1D3557;
            background: #f8f9fa;
            transition: background 0.2s;
        }
        .st-emotion-cache-1v0mbdj > div > div:hover {
            background-color: #e3effa;
            color: #102542;
        }
        .st-emotion-cache-1v0mbdj > div > div[aria-checked="true"] {
            background-color: #1D3557;
            color: #fff;
        }

        /* INFO BOXES */
        .stAlert, .stInfo, .stSuccess, .stWarning, .stError {
            background-color: #e3effa !important;
            color: #1D3557 !important;
            border-radius: 10px !important;
            border: 1px solid #b6d0f7 !important;
            font-size: 1.1rem !important;
        }

        /* EXPANDERS */
        .stExpander {
            background: #f8f9fa !important;
            border-radius: 12px !important;
            border: 1px solid #e3effa !important;
            margin-bottom: 1.2rem !important;
        }
        .stExpanderHeader {
            font-weight: 700 !important;
            color: #1D3557 !important;
            font-size: 1.1rem !important;
        }

        /* BUTTONS */
        .stButton > button {
            background-color: #1D3557 !important;
            color: #fff !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            padding: 0.5rem 1.5rem !important;
            border: none !important;
            margin-bottom: 0.5rem;
            transition: background 0.2s;
        }
        .stButton > button:hover {
            background-color: #457b9d !important;
            color: #fff !important;
        }

        /* MARKDOWN TEXT */
        .stMarkdown p {
            font-size: 1.13rem !important;
            line-height: 1.7 !important;
            color: #22223b !important;
        }
        .stMarkdown ul, .stMarkdown ol {
            margin-left: 1.2em !important;
        }

        /* DIVIDERS */
        hr {
            margin: 2rem 0;
            border: none;
            border-top: 1px solid #e3effa;
        }

        /* BANNER IMAGE */
        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 1.5rem;
            border-radius: 8px;
        }

        /* FOOTER */
        footer {
            font-size: 15px;
            color: #6c757d;
            text-align: center;
            margin-top: 3rem;
            letter-spacing: 0.2px;
        }
        </style>
    """, unsafe_allow_html=True) 