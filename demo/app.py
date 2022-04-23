import spacy_streamlit
import streamlit as st

MODELS = [
    # Tagalog models
    "tl_ud_tl_trg",
    "tl_ud_tl_ugnayan",
    # Foreign models
    "id_ud_id_gsd",
    "vi_ud_vi_vtb",
    "uk_ud_uk_iu",
    "ro_ud_ro_rrt",
    "ca_ud_ca_ancora",
]

text = st.markdown(
    """
    This demo helps visualize how each model we trained from the Tagalog (and
    some foreign) treebanks perform on a given sentence. Try changing the model
    in the sidebar (languages are abbreviated by a [two-letter
    code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), with 'tl' as
    Tagalog), and inspect how accurate its dependency parser and POS tagger are.
    """
)


default_text = "Kapag nilahad ang damdamin, sana hindi magbago ang pagtingin."
spacy_streamlit.visualize(
    models=MODELS,
    default_text=default_text,
    default_model="tl_ud_tl_trg",
    visualizers=["parser", "tokens"],
)
