# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pathlib
from fillpdf import fillpdfs


def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value = haystack[key]
        except:
            continue
        if key == needle:
            return value
        if isinstance(value, dict):
            x = findInDict(needle, value)
            if x is not None:
                return x


def main():
    base = pathlib.Path(__file__).parent.absolute()
    pdf_template = str(base) + '/source.pdf'
    pdf_output = str(base) + "/output.pdf"
    pdf_locked_output = str(base) + "/locked_output.pdf"

    # Get available form fields
    fields = fillpdfs.get_form_fields(pdf_template)
    print(fields)

    data_dict = {
        'name': 'Dragomir',
        'email': 'bogdean@bogdan.ccc',
    }
    # Fill fields from dict.
    fillpdfs.write_fillable_pdf(pdf_template, pdf_output, data_dict)
    # Make document not editable.
    fillpdfs.flatten_pdf(pdf_output, pdf_locked_output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
