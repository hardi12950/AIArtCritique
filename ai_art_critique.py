import streamlit as st
from openai import OpenAI

def analyze_artwork_with_gpt4_vision(url_input):
        api_key = "sk-proj-JghKNqoMraSXoHi9yz9GT3BlbkFJYaM4RVnL9T3svNOsbui5"
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                        {
                                "role": "assistant",
                                "content": [
                                        {"type": "image_url",
                                         "image_url": {"url": url_input},
                                         },
                                ],
                        }
                ],
             max_tokens=300,   
        )
        return response.choices[0].message.content

st.title('AI Art Critique: Enhancing Artistic Understanding with GPT-4 Vision')

image_url = st.sidebar.text_input(label="Input URL of the artwork to comment as critique:")
submit_button = st.sidebar.button(label="Analyze Artwork")

if submit_button and image_url:
        st.image(image=image_url)
        
        artwork_critique = analyze_artwork_with_gpt4_vision(image_url)

        # Display the critique ('artwork_critique' contains the AI-generated text)
        st.markdown("### Artwork Critique")
        st.write(artwork_critique)
