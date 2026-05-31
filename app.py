import streamlit as st

st.title("Hi, i'm V")

st.subheader("about me",divider = "gray")

st.markdown("""           

i’m a 22 year old from New Castle, DE. My interests include data science, ML, philosophy,
movies and tv shows, social media, and everything else.

i’m currently working on data science projects and i like turning my 
models and data analysis into web apps and dashboards using streamlit.

i’m interested in the discussions surrounding free will and moral responsibility,
i mostly lean towards the impossibility of basic desert moral responsibility, 
supported by Galen Strawson’s infinite regress argument. i also like Derk Perebooms hard incompatibilist
position, especially his manipulation arguments.

i’m an anti realist on all sorts of things, including personal identity, gender, morality, objective truth, etc. 
i believe in the hard problem of consciousness, i.e, the question of how a first person, subjective 
experience can arise from physical matter.

""")

st.subheader("my socials",divider = "gray")

col1, col2, col3, col4, col5, col6 = st.columns(6) 

with col1:
    st.image("https://images.icon-icons.com/3685/PNG/512/github_logo_icon_229278.png", width = 30)
    st.link_button("GitHub",'https://github.com/wintersky44')
with col2:
    st.image("https://images.squarespace-cdn.com/content/v1/54a5505fe4b0d132f64e0e9b/1591957981477-VQJU5KFVSWHKCK5NIBLJ/Pinterest-Logo-1x1.png", width = 30)
    st.link_button("Pinterest","https://pin.it/4TyXAUw84")

with col3:
    st.image("https://a.ltrbxd.com/logos/letterboxd-decal-dots-pos-rgb-500px.png", width = 30)
    st.link_button("Letterboxd", "https://boxd.it/7ZQuN")

with col4:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Reddit_Logo_Icon.svg/250px-Reddit_Logo_Icon.svg.png", width = 30)
    st.link_button("Reddit", "https://www.reddit.com/user/cftvkjhbkf/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button")

with col5:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Youtube_Music_icon.svg/3840px-Youtube_Music_icon.svg.png", width = 30)
    st.link_button("YT music", "https://music.youtube.com/@abc123-e1h?si=kfyjkz34sLDTsyqg") 


