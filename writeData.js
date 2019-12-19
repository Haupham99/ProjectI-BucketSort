uriContent = "data:application/octet-stream," + encodeURIComponent(JSON.stringify(resultArray));
newWindow = window.open(uriContent, 'neuesDokument');