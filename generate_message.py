import streamlit as st
import openai

openai.api_key = st.secrets["mykey"]

# Define neutral product features, benefits, pain points, and desires
product_features = ["Voice control", "Touch screen interface", "Smart inventory management", "Recipe suggestions"]
product_benefits = ["Convenience", "Reduced food waste", "Personalized cooking assistance", "Energy efficiency", "Longer food freshness"]
target_audience = ["Busy families", "Health-conscious individuals", "Tech enthusiasts", "Cooking aficionados", "Home chefs"]
pain_points = ["Limited kitchen space", "Difficulty meal planning", "Time constraints", "Food spoilage concerns"]
desires = ["Simplified cooking", "Healthier eating", "Optimized organization", "Culinary inspiration"]
channels = ["Instagram", "Facebook", "Twitter", "Email"]
tones = ["Casual", "Informative", "Enthusiastic", "Humorous", "Inspirational"]

# Function to generate marketing copy
def generate_copy(product_name, product_features, product_benefits, target_audience, pain_points, desires, channel, tone):
    prompt = f"""
    You're a marketing copywriter. Write a {channel} post caption and image description to promote the {product_name}, a new smart refrigerator.

    **Target audience:** {target_audience}

    **Highlight:**
    * Key features: {', '.join(product_features)}
    * Benefits: {', '.join(product_benefits)}
    * Address these pain points: {', '.join(pain_points)}
    * Appeal to these desires: {', '.join(desires)}

    **Tone:** {tone}

    **Image description:** A photo of the {product_name} in a modern kitchen setting, with the door open to showcase the organized interior and a user interacting with it.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing copywriter."},
            {"role": "user", "content": prompt}
        ]
    )
    copy = response['choices'][0]['message']['content']
    caption, image_description = copy.split("\n\n")
    return caption, image_description

# Streamlit UI
st.title("Smart Fridge Pro Marketing Copy Generator")

product_name = st.text_input("Product Name:", value="Smart Fridge Pro")
selected_features = st.multiselect("Product Features:", product_features)
selected_benefits = st.multiselect("Product Benefits:", product_benefits)
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)
selected_channel = st.selectbox("Channel:", channels)
selected_tone = st.selectbox("Tone:", tones)

if st.button("Generate Marketing Copy"):
    caption, image_description = generate_copy(product_name, selected_features, selected_benefits, selected_audience, selected_pain_points, selected_desires, selected_channel, selected_tone)
    st.subheader("Caption:")
    st.write(caption)
    st.subheader("Image Description:")
    st.write(image_description)
