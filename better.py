import requests
import pandas as pd
import lxml.html as lh

req = requests.get("https://awt.cbp.gov/Home/OpenExcel?port=A272&rptFrom=05%2F01%2F2019&rptTo=05%2F24%2F2019");
doc = lh.fromstring(req.content)
table = doc.xpath('//table')
print(table[0][2].text_content())
df = pd.read_html('http://awt.cbp.gov/Home/OpenExcel?port=A272&rptFrom=05%2F01%2F2019&rptTo=05%2F24%2F2019')

