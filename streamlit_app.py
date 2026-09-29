import streamlit as st
from app.image_generator import generate_image
from pathlib import Path

st.set_page_config(
    page_title="ComicCraft AI",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 ComicCraft AI")
st.subheader("Create Your Own AI Comic")

story_idea = st.text_area(
    "📖 Story Idea",
    placeholder="Enter your story idea..."
)

main_character = st.text_input(
    "🧑 Main Character",
    placeholder="Example: A brave young girl"
)

setting = st.text_input(
    "🌍 Setting",
    placeholder="Example: A magical forest"
)

pages = st.slider(
    "📄 Number of Pages",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("✨ Generate Comic", type="primary"):

    if not story_idea or not main_character:
        st.warning("Please enter a story idea and main character.")
    else:
        st.write("Generating your comic...")

        for i in range(1, pages + 1):
            prompt = (
                f"Comic book page {i}. "
                f"Main character: {main_character}. "
                f"Story: {story_idea}. "
                f"Setting: {setting}. "
                f"Create a colorful comic illustration."
            )

            filename = f"page_{i}.png"

            try:
                image_path = generate_image(prompt, filename)

                if Path(image_path).exists():
                    st.image(
                        image_path,
                        caption=f"Comic Page {i}",
                        use_container_width=True
                    )

            except Exception as e:
                st.error(f"Error generating page {i}: {e}")

        st.success("🎉 Comic generation completed!")
