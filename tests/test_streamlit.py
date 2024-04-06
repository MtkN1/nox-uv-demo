import nox_uv_demo


def test_streamlit():
    assert nox_uv_demo.st_version()
