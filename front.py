'''
Copyright (c) 2026 peek8.io

Created Date: Tuesday, June 30th 2026, 11:12:54 am
Author: Md. Asraful Haque

'''
import gradio as gr
from website_brochure import create_brochure

name_input = gr.Textbox(label="Company Name", info="Enter the company name")
url_input = gr.Textbox(label="Company URL", info="Enter the company URL")

output = gr.Markdown(label="Brochure:")

gr.Interface(
    fn=create_brochure,
    inputs=[name_input, url_input],
    outputs=output,
    title="Company Brochure Generator",
    description="This is a simple Gradio app that generates company brochures.",
    flagging_mode="never",
    theme="default").launch()