
const fetch = require('node-fetch');

let endpoint = "https://awt.cbp.gov/Home/OpenExcel?port=A272&rptFrom=05%2F01%2F2019&rptTo=05%2F24%2F2019";

const getData = async () => {
    const data = fetch(endpoint, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/csv',
            'Content-disposition': "attachment;filename=myfilename.csv",
        }
    }).then(response => response.text()).then(text => text);
    console.log(await data);

}

getData();