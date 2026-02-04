# Scrapy_Samples

## Items 

Exemplo do uso de Items (items.py) para escrapear elementos do mesmo tipo de páxinas diferentes. No exemplo, libros (title, author, isbn), das páxinas web de dúas editoriais diferentes: Capitán Swing e Libros del KO.
- capitanswing_book.py
- librosdelko_book.py

## Follow links

Exemplo de como utilizar "follow" e diferentes "parsers" para escrapear páxinas ás que apunta a "start_url".
- capitanswing_bigdata.py
- librosdelko_futbol.py

Exemplo de como buscar a "next_page" cando escrapeamos páxinas con "pagination".
- librosdelko.py

## Pipelines

Uso de pipelines (pipelines.py) para a limpeza e transformación de datos. 
- settings.py: é necesario descomentar as últimas liñas para activar as pipelines.