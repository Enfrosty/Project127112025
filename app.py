import streamlit as st

st.set_page_config(page_title="File Echo App", layout="centered")

st.title("File Echo App")
st.write("Upload file apa saja, lalu download kembali persis sama tanpa diubah.")

st.markdown("---")

uploaded_files = st.file_uploader(
    "Pilih satu atau lebih file untuk di-upload:",
    accept_multiple_files=True
)

if uploaded_files:
    st.subheader("File yang kamu upload:")
    for i, uploaded_file in enumerate(uploaded_files, start=1):
        file_bytes = uploaded_file.getvalue()

        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{i}. {uploaded_file.name}**")
            st.write(f"- Size: {len(file_bytes)} bytes")
            st.write(f"- MIME type: {uploaded_file.type or 'application/octet-stream'}")

        with col2:
            st.download_button(
                label="Download lagi",
                data=file_bytes,
                file_name=uploaded_file.name,
                mime=uploaded_file.type or "application/octet-stream",
                key=f"download_{i}"
            )
else:
    st.info("Belum ada file yang di-upload. Silakan pilih file di atas.")
