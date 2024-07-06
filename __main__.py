import etl_code as etl

etl.logging_time('ETL Job started')

etl.logging_time('Extract process started')
extracted_data = etl.extract()
etl.logging_time('Extraction complete')

etl.logging_time('Transform process started')
transformed_data = etl.transform(extracted_data)
etl.logging_time('Transformation completed')

etl.logging_time('Load process started')
etl.load_data(transformed_data)
etl.logging_time('Loading Completed')

etl.logging_time('ETL Job ended')