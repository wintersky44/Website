import streamlit as st

st.title("Hi, i'm V")

st.subheader("About me",divider = "gray")

st.markdown("""           

I’m a 22 year old. My interests include data science and ML, philosophy,
movies and tv shows, reading wikipedia, and browsing social media.
            

Some topics in philosophy which interest me are free will, consciousness, meta-ethics, ethics, existentialism, and metaphysics.

I have spent a significant amount of my time reading about the free will and moral responsibility debates.
My favorite a priori arguments against free will include Galen Strawson's argument of infinite regress, and Nietzsche's appeal
to the nature of causa sui. I also like Derk Perebooms work on free will-- his hard incompatibilist position and manipulation arguments.

I'm interested in the hard problem of consciousness, i.e, the question of how a first person, subjective 
experience can arise from physical matter.
            
I like Albert Camus' absurdist philosophy, as I believe there is no ultimate meaning to it all, but we can still live happily.

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


