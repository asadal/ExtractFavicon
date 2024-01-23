import streamlit as st
import requests
from io import BytesIO
from PIL import Image


def favicon_app():
    st.set_page_config(
        page_title="Extract Favicon",
        page_icon="https://freepngimg.com/thumb/world_wide_web/99120-www-free-hd-image.png"
        )

    st.title("Extract Favicon")

    url = st.text_input("Input URL", placeholder="https://www.google.com")

    # 파비콘 크기 선택
    size = st.radio("Favicon Size...", ["16", "32", "48"])

    # 파비콘 찾기 버튼 클릭 시 동작
    if st.button("Find Favicon"):
        # URL에 쿼리 적용
        api_url = "https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={}&size={}".format(url, size)

        try:
            # API 요청 및 응답 처리
            response = requests.get(api_url)
            response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴

            # 이미지 출력
            img = Image.open(BytesIO(response.content))
            st.image(img, caption='gotcha', use_column_width=False)

            # 다운로드 버튼 생성
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            st.download_button(
                label="Download",
                data=buffer.getvalue(),
                file_name="favicon.png",
                mime="image/png",
            )
        except requests.exceptions.RequestException as e:
            st.write("An error occurred :", e)

if __name__ == "__main__":
    favicon_app()
