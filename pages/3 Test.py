import streamlit as st

def enlarge_image(image_url):
    st.markdown(
        f"""
        <style>
        .enlarge {{
            transition: transform 0.2s;
            cursor: pointer;
        }}
        .enlarge:hover {{
            transform: scale(3);
        }}
        .enlarge.active {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(2);
            z-index: 9999;
        }}
        </style>
        <img id="enlarge-image" class="enlarge" src="{image_url}" width="300">
        """,
        unsafe_allow_html=True,
    )

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFRmWtO1zrO6tt35ewAJOE9NpAb8yiwhbrBWyxjVQCZw&s"
enlarge_image(image_url)

# Add a click event listener to toggle the active class
st.markdown(
    """
    <script>
    const image = document.getElementById("enlarge-image");
    image.addEventListener("click", () => {
        image.classList.toggle("active");
    });
    </script>
    """,
    unsafe_allow_html=True,
)