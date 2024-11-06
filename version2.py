import streamlit as st # type: ignore

if "slider" not in st.session_state:
    st.session_state.slider = 25
if "slider2" not in st.session_state:
    st.session_state.slider2 = 25  
    
    # Default value for the second slider
# if "min_value" not in st.session_state:
#     st.session_state.min_value = 25  # Default minimum value

slider2 = st.session_state.slider2

min_value = st.slider("set min", 0, 50, 25)
st.session_state.slider = st.slider("slider", min_value, 100, st.session_state.slider, key="key1")

if st.session_state.slider2 < min_value:
    st.session_state.slider2 = min_value
    
def update_slider():
    st.session_state.slider2 = slider2

st.session_state.slider2 = st.slider("Slider2", min_value, 100, slider2, key="key2", on_change=update_slider())

st.button("click")