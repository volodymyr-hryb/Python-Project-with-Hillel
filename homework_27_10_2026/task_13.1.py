def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding = 'utf-8') as file:
        html = file.read()
        switch = True
        cleaned_text = ""
        for char in html:
            if char == '<':
                switch = False
            elif char == '>':
                switch = True
            else:
                if switch:
                    cleaned_text += char
    with open(result_file, 'w', encoding ='utf-8') as file:
        file.write(cleaned_text)


delete_html_tags("draft.html")