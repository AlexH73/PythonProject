from docx.enum.text import WD_ALIGN_PARAGRAPH

def apply_table_styles(table):
    """Применяет стили и выравнивание для таблицы."""
    table.style = "Table Grid"
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
