from docx import Document

def remove_all_headers(doc_path):
    doc = Document(doc_path)

    for section in doc.sections:
        section.header.clear()

    doc.save(doc_path)

# Thay 'your_document.docx' bằng tên tệp của bạn
remove_all_headers('tải xuống (1).docx')
